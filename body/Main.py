#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
import twitter.tw as tw
import ml.Tfidf as TFIDF
import ml.Bayes as Bayes
import common.Config as Config
import csv
from os import path

class Main(object):
	def __init__(self):
		self.twitter = tw.Tw()
		self.tfidf = TFIDF.Tfidf()
		self.bayes = Bayes.Bayes()
		self.conf = Config.Config()
		self.conf.loadConfig()

	def train(self,likes):
		f = open(path.dirname(path.abspath(__file__))+"/../csv/interest.csv","ab")
		intcsv = csv.writer(f)
		keyf = open(path.dirname(path.abspath(__file__))+"/../csv/likeskey.csv","ab")
		keydoc = csv.writer(keyf)
		allf = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","ab")
		alldoc = csv.writer(allf)
		training_list = []
		likeword = likes.split(",")
		training_list.append(twitter.homeTweetMain())
		training_list.append(twitter.searchTweetMain(keywordlist=likeword))
		sampling = []
		for group in trainig_list:
			for tex in group:
				sampling.append(tex)
		if self.conf.getUseMongo():
			pass
		else:
			displist = ramdom.sample(sampling,200)
			for teacher in displist:
				alldoc.writerow(teacher)
			allf.close()
			all = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","rb")
			data = csv.reader(all)
			count = 0
			for display in displist:
				print str(count) + ":" + str(display)
				count = count + 1
			print "please likes tweet No. input:"
			likeno = raw_input()
			nolist = likeno.split(",")
			likedoc = []
			for no in nolist:
				likedoc.append(displist[int(no)])
				displist[int(no)] = ""
			for no in nolist:
				del displist[int(no)]
			for doc in likedoc:
				tmp_csv = []
				tmp_csv.append("like")
				tmp_csv.append(doc)
				intcsv.writerow(tmp_csv)
			for doc in displist:
				tmp_csv = []
				tmp_csv.append("dislike")
				tmp_csv.append(doc)
				intcsv.writerow(tmp_csv)
			getkey = bayes.TfidfMain(docs=likedoc,data=data,N=len(data))
			keydoc.writerow(getkey)
			print "Training OK"

	def likeTweet(self):
		print "reloaded time two min"
		f = open(path.dirname(path.abspath(__file__))+"/../csv/likeskey.csv",'rb')
		dataRead = csv.reader(f)
		allf = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","rb")
		alldata = csv.reader(allf)
		teacher = {}
		for value in alldata:
			teacher[value[0]] = value[1]
		for k,v in teacher:
			self.bayes.train(k,v)
		keyword = []
		for row in dataReader:
			keyword.append(row)
		while(True):
			samples = []
			get = self.twitter.searchTweetMain(keywordlist=ramdom.sample(keyword,10))
			for doc in get:
				if self.bayes.classifier(doc) == "like":
					samples.append(doc)
			if len(samples) > 100:
				display = random.sample(get,100)
			else:
				display = get
			for cons in display:
				print str(cons)
			time.sleep(120)
