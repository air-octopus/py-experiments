# coding=utf-8

import lexdb
import nltk
import collections

from swfngramm import *


def parse_sentence(sentence):
    tokens = [t.lower() for t in nltk.word_tokenize(sentence) if t not in [
        ',', '.', '!', '?', '...', ';', ':', '-', '"', "'", '(', ')', '[', ']', '{', '}'
    ]]
    return tokens


class TextProcessor(object):
    def __init__(self, db : lexdb.LexDB):
        self.db = db
        self.stored_wordforms = db.get_all_wordforms()
        self.wordforms_in_process = set()

    def find_sentence_parts(self, text_id):
        sentences = self.db.get_sentences(text_id)

        swfgramm_dict = {}
        for sentence_id, sentence in sentences:
            tokens = parse_sentence(sentence)
            self.wordforms_in_process.update(tokens)

            swfgramms = [tokens[:i] + tokens[i+1:] for i in range(0, len(tokens))]

            for i, swfg_text in enumerate(swfgramms):
                swfg = SWFNgramm(swfg_text)
                if swfg.md5 not in swfgramm_dict:
                    swfgramm_dict[swfg.md5] = (swfg_text, collections.defaultdict(list))

                swfgramm_info = swfgramm_dict[swfg.md5]
                if swfgramm_info[0] != swfg_text:
                    raise Exception("Different tokens (%s, %s) have same checksum (%s)" % (swfgramm_info[0], swfg_text, swfg.md5.hexdigest()))

                swfgramm_info[1][(tokens[i], i)].append(sentence_id)
                # swfgramm_info[1].append((tokens[i], i, sentence_id))

        ooo = [(o_md5, o[0], o[1]) for o_md5, o in swfgramm_dict.items() if len(o[1]) > 1]

        # пример того, что получается
        # ---------------------------------------------------------------
        # [02] = {tuple} <class 'tuple'>: ('6fb9fdc07741e213d758bb6c2239b661', ['как', 'же'], defaultdict(<class 'list'>, {('а', 0): [60, 384, 1231], ('знаю', 2): [647], ('помню', 2): [702], ('мертвый', 2): [1252]}))
        #      0 = {str} '6fb9fdc07741e213d758bb6c2239b661'
        #      1 = {list} <class 'list'>: ['как', 'же']
        #      2 = {defaultdict} defaultdict(<class 'list'>, {('а', 0): [60, 384, 1231], ('знаю', 2): [647], ('помню', 2): [702], ('мертвый', 2): [1252]})
        #       ('а', 0) (139736621942536) = {list} <class 'list'>: [60, 384, 1231]
        #       ('знаю', 2) (139736616910536) = {list} <class 'list'>: [647]
        #       ('помню', 2) (139736616384456) = {list} <class 'list'>: [702]
        #       ('мертвый', 2) (139736611277064) = {list} <class 'list'>: [1252]
        #       __len__ = {int} 4
        #       default_factory = {type} <class 'list'>
        #      __len__ = {int} 3
        # ---------------------------------------------------------------
        # тут:
        #       1 = {list} <class 'list'>: ['как', 'же']
        #           -- постоянная структура
        #       ('а', 0) (139736621942536) = {list} <class 'list'>: [60, 384, 1231]
        #           -- модификации (добавляется 'а' в позицию 0; полученное предложение встречается 3 раза; id предложений: 60, 384, 1231)
        # т.е. алгоритм нашел следующие предложения:
        #   а как же
        #     как же, знаю
        #     как же, помню
        #     как же, мертвый

        pass
