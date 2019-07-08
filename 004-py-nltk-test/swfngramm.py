# coding=utf-8

"""
класс для работы с swf-n-граммами. В отличие от n-грамм, которые составляются для слов,
эти n-граммы составляются из предложений с некоторыми выкинутыми словоформами.
Отсюда префикс swf (sentence, wordforms)
"""

import hashlib
from _md5 import md5


class SWFNgramm:
    def __init__(self, tokens):
        self.tokens = tokens
        self.str = ' '.join(tokens)
        self.md5_obj = hashlib.md5(self.str.encode())
        self.md5 = self.md5_obj.hexdigest()

