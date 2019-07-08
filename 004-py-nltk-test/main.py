# coding=utf-8

"""
Попытка вычленения грамматических классов на основе синтаксической структуры предложений

Примерная идея:
    * весь доступный текст разбиваем на предложения и токенизируем
    * предложения в виде текста сохраняем в БД
    * токены (словоформы) сохраняем в БД
    * составляем SWF1-граммы предложений (наборы токенов, составленные из предложений с ровно одним исключенным токеном)
      заметим, что токеном может быть как словоформа, так и граммема (см. далее)
        * конструируем из SWF1-грамм строки и считаем их md5
        * собираем dict:
            md5 -> (SWF1-грамма, [(token,token_index,sentence_id)] )
            --------md5 -> (SWF1-грамма, tokens={token1,token2,...}, {sentence_id1})
        * выкидываем все элементы в которых только один токен
    * ищем SWF1-грамму с максимальным количеством токенов
    * добавляем новую прото-граммему
        * TODO: что делать, если среди токенов есть граммемы
    * во всех SWF1-граммах заменяем токены из набора tokens на граммему. Полученные SWF1-граммы добавляем в dict

Структура базы данных:
    * loaded_texts      -- информация о загруженных текстах
        id
        filename
        filepath
    * sentences         -- все предложения из всех тектов
        id
        text_id
        sentence
    * wordforms         -- уникальные словоформы
        id
        wordform
    * grammemes         -- найденные (предполагаемые) граммемы. Только идентификаторы
        id
    * wfgrammemes
        grammeme_id
        wordform_id

"""

import lexdb
import text_loader
import text_processor

db = lexdb.LexDB(".temp/db.sql")

text_id = text_loader.load_text(db, "data/utf8_test_003.txt")
# text_id = text_loader.load_text(db, "data/utf8_test_004.txt")

processor = text_processor.TextProcessor(db)

processor.process_text(text_id)

pass
