# coding=utf-8

import nltk
import pymorphy2
import os

class Word:
    def __init__(self, word):
        self.word = word
        self.definition_inds = set()
        self.level = 0


os.makedirs("../temp", exist_ok=True)

morph = pymorphy2.MorphAnalyzer()
words = []
word2ind = {}

# t0 = os.times().elapsed

def append_word_to_array(word):
    if word not in word2ind:
        word2ind[word] = len(words)
        words.append(Word(word))

def load_from_source(dict_path):
    with open(dict_path) as f:
        dict_data = f.readlines()

    print("%parsing dict... ")

    iter_num = 0
    for word_topic in dict_data:
        if iter_num % 100 == 0:
            print(iter_num)
        iter_num += 1

        word_topic_parsed = word_topic.split('|')
        if len(word_topic_parsed) < 6:
            continue
        word = word_topic_parsed[0]
        word_desc = word_topic_parsed[5]
        # разбор определения слова
        defs = nltk.sent_tokenize(word_desc)
        for sent in defs:
            tokens = nltk.word_tokenize(sent)
            tokens_norm = [morph.parse(word)[0].normal_form for word in tokens]
            # tokens_norms_all = [morph.normal_forms(word) for word in tokens]

            append_word_to_array(word)
            # if word not in word2ind:
            #     word2ind[word] = len(words)
            #     words.append(Word(word))
            w = words[word2ind[word]]

            for tok in tokens_norm:
                append_word_to_array(tok)

            w.definition_inds.update({word2ind[tok] for tok in tokens_norm})

        pass

def save_parsed_data(data_path):
    print("saving...")
    with open(data_path, "w") as f:
        # level index word defs...
        dict_data = f.writelines(
            ["%d %d %s %s\n" % (w.level, i, w.word,
                              " ".join(str(d) for d in w.definition_inds))
             for i, w in enumerate(words)]
        )

load_from_source("../data/ozhegov_utf8.txt")

save_parsed_data("../temp/parsed_dict.dat")

pass