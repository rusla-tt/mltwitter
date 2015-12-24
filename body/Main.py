#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
import twitter.tw as tw
import ml.Tfidf as TFIDF
import ml.Bayes as Bayes
import common.Config as Config
import csv
from os import path
import random
import time

class Main(object):
    def __init__(self):
        self.twitter = tw.Tw()
        self.tfidf = TFIDF.Tfidf()
        self.bayes = Bayes.Bayes()
        self.conf = Config.Config()
        self.conf.loadConfig()

    def train(self,likes):
        """
        配列切ってメソッドで管理しても良いかも？
        """
        f = open(path.dirname(path.abspath(__file__))+"/../csv/interest.csv","ab")
        intcsv = csv.writer(f)
        keyf = open(path.dirname(path.abspath(__file__))+"/../csv/likeskey.csv","ab")
        keydoc = csv.writer(keyf)
        allf = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","wb")
        alldoc = csv.writer(allf)
        training_list = []
        likeword = likes.split(",")
        training_list.append(self.twitter.homeTweetMain())
        training_list.append(self.twitter.searchTweetMain(keywordlist=likeword))
        sampling = []
        for group in training_list:
            for tex in group:
                sampling.append(tex)
        if self.conf.getUseMongo():
            pass
        else:
            displist = random.sample(sampling,200)
            for teacher in sampling:
                inputtext = []
                inputtext.append(teacher.encode('utf-8'))
                alldoc.writerow(inputtext)
            allf.close()
            alld = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","rb")
            data = csv.reader(alld)
            alldata = []
            for d in data:
                alldata.append(d)
            print(alldata[0])
            count = 0
            for display in displist:
                print str(count) + ":" + str(display.encode('utf-8'))
                count = count + 1
            print "please likes tweet No. input:"
            likeno = raw_input()
            nolist = likeno.split(",")
            likedoc = []
            for no in nolist:
                likedoc.append(displist[int(no)])
                displist[int(no)] = ""
        #   for no in nolist:
        #       del displist[int(no)]
            for doc in likedoc:
                tmp_csv = []
                tmp_csv.append("like")
                tmp_csv.append(doc.encode('utf-8'))
                intcsv.writerow(tmp_csv)
            for doc in displist:
                tmp_csv = []
                tmp_csv.append("dislike")
                tmp_csv.append(doc.encode('utf-8'))
                intcsv.writerow(tmp_csv)
            getkey = self.tfidf.TfidfMain(docs=likedoc,data=alldata,N=len(alldata))
            for get in range(len(getkey)):
                i = []
                i.append(getkey[get].encode('utf-8'))
                keydoc.writerow(i)
            print "Training OK"

    def likesTweet(self):
        print "reloaded time two min"
        """
        method切って配列で管理してもいいかも？
        """
        f = open(path.dirname(path.abspath(__file__))+"/../csv/likeskey.csv",'rb')
        dataRead = csv.reader(f)
        allf = open(path.dirname(path.abspath(__file__))+"/../csv/all.csv","rb")
        alldata = csv.reader(allf)
        inst = open(path.dirname(path.abspath(__file__))+"/../csv/interest.csv","rb")
        instdata = csv.reader(inst)
        teacher = {}
        for value in instdata:
            teacher[value[0]] = value[1]
        for k,v in teacher:
            self.bayes.train(k,v)
        keyword = []
        for row in dataRead:
            keyword.append(row)
        while(True):
            samples = []
            get = self.twitter.searchTweetMain(keywordlist=random.sample(keyword,10))
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
