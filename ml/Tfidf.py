#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from math import log
import wakachi

class Tfidf(object):
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

    def TfidfMain(self,docs,data,N):
        tf = {}
        df = {}
        for text in docs:
            df_list = []
#            print(text)
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
        for d in range(len(data)):
            df_list = []
#            print(data[d][0])
            words = wakachi.Wakachi().main(data[d][0].decode('utf-8'))
            for word in words:
                try:
                    if word in df_list:
                        continue
                    df[word] = df[word] + 1
                except KeyError:
                    df[word] = 1
        tfidf = {}
        keys = []
        for key,value in self.getTopKeywords(tf, 100):
#            print "TF : " + tf[key]
#            print "DF : " + df[key]
            tfidf[key] = self.calcTFIDF(N, tf[key], df[key])
        for k,v in self.getTopKeywords(tfidf,100):
            keys.append(k)
        return keys
