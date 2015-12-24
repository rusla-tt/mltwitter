#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import MeCab

MECAB_MODE = '-Owakati -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd'
PARSE_TEXT_ENCODING = 'utf-8'


class Wakachi(object):

    def main(self,text):
        word_dic = self.__parse(text)
        return word_dic
    def __parse(self,unicode_string_text):
        tagger = MeCab.Tagger(MECAB_MODE)
        text = unicode_string_text.encode(PARSE_TEXT_ENCODING)
        node = tagger.parseToNode(text)
        words = []
        while node:
            pos = node.feature.split(",")[0]
            word = node.surface.decode("utf-8")
            node = node.next
            if pos == "名詞" or pos == "動詞" or pos == "形容詞":
                words.append(word)
        word_dic = words[1:-1]
        return word_dic
