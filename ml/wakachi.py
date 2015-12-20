#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import Mecab

MECAB_MODE = '-Owakachi -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/'
PARSE_TEXT_ENCODING = 'utf-8'

class Wakachi(object):
	def main(self,text):
		word_dic = self.__parse(text)
		return word_dic
	def __parse(self,unicode_string_text):
		tagger = MeCab.Tagger(MECAB_MODE)
		text = unicode_string_text.encode(PARSE_TEXT_ENCODING)
		node = tagger.parseToNode(text)
		word = []
		while node:
			word = node.surface.decode("utf-8")
			node = node.next
			words.append(word)
		word_dic = words[1:-1]
		return word_dic
