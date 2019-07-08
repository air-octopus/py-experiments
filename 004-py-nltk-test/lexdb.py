

import sqlite3 as sql


class LexDB:

    def __init__(self, db_path):
        self.db_init(db_path)

    def db_init(self, db_path):
        self.db = sql.connect(db_path)
        c = self.c = self.db.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS loaded_texts      (
                  id            INTEGER PRIMARY KEY
                , filepath      TEXT
                , is_processed  BOOLEAN
            )
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS sentences         (
                  id            INTEGER PRIMARY KEY
                , text_id       INTEGER
                , sentence      TEXT
            )
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS wordforms         (
                  id            INTEGER PRIMARY KEY
                , wordform      TEXT
            )
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS grammemes         (
                  id            INTEGER PRIMARY KEY
            )
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS wfgrammemes       (
                  grammeme_id   INTEGER
                , wordform_id   INTEGER
            )
        """)

        c.execute('CREATE INDEX IF NOT EXISTS idx_loaded_texts_001  ON loaded_texts  (filepath)   ')
        c.execute('CREATE INDEX IF NOT EXISTS idx_sentences_001     ON sentences     (text_id )   ')

    def commit(self):
        self.db.commit()

    ###############################################################
    ##  ЗАГРУЗКА В БАЗУ

    def add_text(self, text_file_path):
        self.c.execute("INSERT INTO loaded_texts(filepath, is_processed) VALUES (?, ?)", (text_file_path, False))
        self.commit()
        return self.c.lastrowid

    def add_sentence(self, text_id, sentence):
        self.c.execute("INSERT INTO sentences(text_id, sentence) VALUES (?, ?)", (text_id, sentence))
        return self.c.lastrowid

    def add_sentences(self, text_id, sentences):
        self.c.executemany("INSERT INTO sentences(text_id, sentence) VALUES (?, ?)", [(text_id, sentence) for sentence in sentences])
        self.commit()

    def add_wordforms(self, text_id, wordforms):
        self.c.executemany("INSERT INTO wordforms(wordform) VALUES (?)", [wordform for wordform in wordforms])
        self.commit()

    ###############################################################
    ##  ИЗМЕНЕНИЕ БАЗЫ

    ###############################################################
    ##  ЧТЕНИЕ ИЗ БАЗЫ

    def find_text(self, text_file_path):
        d = self.c.execute("SELECT id, is_processed FROM loaded_texts WHERE filepath = '%s'" % text_file_path).fetchall()
        return d[0] if len(d) > 0 else None

    def get_sentences(self, text_id):
        return self.c.execute("SELECT id, sentence FROM sentences WHERE text_id = %d ORDER BY id" % text_id).fetchall()

    def get_all_wordforms(self):
        return self.c.execute("SELECT id, wordform FROM wordforms").fetchall()

