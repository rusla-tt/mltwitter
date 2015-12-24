#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math
import sys
import getwords

class Bayes(object):
	def __init__(self):
		self.vocabularies = set()
		self.wordcount = {}
		self.catcount = {}
		self._getwords = getwords.GetWords()

	def reset(self):
		self.vocabularies = set()
		self.wordcount = {}
		self.catcount = {}

	def __wordcountup(self,word,cat):
		self.wordcount.setdefault(cat,{})
		self.wordcount[cat].setdefault(word,0)
		self.wordcount[cat][word] += 1
		self.vocabularies.add(word)

	def __catcountup(self,cat):
		self.catcount.setdefault(cat,0)
		self.catcount[cat] += 1

	def train(self,doc,cat):
		word = self._getwords.getwords(doc)
		for w in word:
			self.__wordcountup(w,cat)
		self.__catcountup(cat)

	def classifier(self,doc):
		best = None
		max = -sys.maxint
		word = self._getwords.getwords(doc)
		for cat in self.catcount.keys():
			prob = self.score(word,cat)
			if prob > max:
				max = prob
				best = cat
		return best

	def score(self,word,cat):
		score = math.log(self.__prioprob(cat))
		for w in word:
			score += math.log(self.__wordprob(w,cat))
		return score

	def __priorprob(self,cat):
		return float(self.__catcount[cat])/sum(self.catcount.values())

	def __incategory(self,word,cat):
		if word in (self.__wordcount[cat]):
			return float(self.wordcount[cat][word])
		return 0.0

	def __wordprob(self,word,cat):
		prob = (self.__incategory(
			word,cat) + 1.0) / (sum(
				self.wordcount[cat].values()) + len(self.vocabularies)*1.0)
		return prob
