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

    def process_text(self, text_id):
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

        pass
