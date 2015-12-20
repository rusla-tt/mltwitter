#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from math import log

class Tfidf(onject):
	"""
	検索用のキーワードを取得する(特徴語の抽出)
	最終的にランダム使って５キーワードくらいにすればいいか？
	"""
	def getTopKeywords(self,TF,n):
		list = sorted(TF.items(), key=lambda x:x[1], reverse=True)
		return list[0:n]

	def calcTFIDF(self,N,TF,DF):
		tfidf = TF * log( N / DF )
		return tfidf

	def TfidfMain(self,docs):
		tf = {}
		df = {}
		for i,text in docs:
			df_list = []
			words = wakachi.Wakachi().main(text)
			for word in words:
				try:
					tf[word] = tf[word] + 1
				except KeyError:
					tf[word] = 1
			for word in words:
				try:
					if word in df_list:
						continue
					df[word] = df[word] + 1
				except KeyError:
					df[word] = 1
		tfidf = {}
		for key,value in getTopKeywords(tf,100):
			tfidf[key] = calcTFIDF(N,tf[key],df[key])
		return tfidf

