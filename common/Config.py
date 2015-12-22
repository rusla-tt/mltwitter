#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import yaml
from os import path

"""
 Configure Class Singleton
"""
class Config(object):
	mongoIP = ""
	mongoPort = 0
	mongo_use = False
	ConsumerKey = ""
	ConsumerSecret = ""
	AccessToken = ""
	AccessTokenSecret = ""
	_instance = None
	def __new__(cls, *a, **kw):
		if cls._instance is None:
			cls._instance = object.__new__(cls, *a, **kw)
		return cls._instance
	def loadConfig(self):
		f = open(path.dirname(path.abspath(__file__)) + "/../config/config.yaml").read()
		f = f.decode('utf8')
		c = yaml.load(f)
		self.setMongoDB(str(c["mongoip"]))
		self.setMongoPort(int(c["mongoport"]))
		self.setCK(str(c["ck"]))
		self.setCS(str(c["cs"]))
		self.setAT(str(c["at"]))
		self.setATS(str(c["ats"]))
		self.setUseMongo(c["mongo_use"])

	def writeConfig(self):
		data = dict(
			mongoip = str(self.getMongoDB()),
			mongoport = int(self.getMongoPort()),
			ck = str(self.getCK()),
			cs = str(self.getCS()),
			at = str(self.getAT()),
			ats = str(self.getATS()),
			mongo_use = False
		)
		with open(path.dirname(path.abspath(__file__))+"/../config/config.yaml",'w') as outfile:
			outfile.write(yaml.dump(data,default_flow_style=True))
	def getMongoDB(self):
		return self.mongoIP
	def getMongoPort(self):
		return self.mongoPort
	def getUseMongo(self):
		return self.mongo_use
	def getCK(self):
		return self.ConsumerKey
	def getCS(self):
		return self.ConsumerSecret
	def getAT(self):
		return self.AccessToken
	def getATS(self):
		return self.AccessTokenSecret
	def setMongoDB(self,loadmongoip):
		self.mongoIP = loadmongoip
	def setMongoPort(self,loadPort):
		self.mongoPort = loadPort
	def setUseMongo(self,loadUseMongo):
		self.mongo_use = loadUseMongo
	def setCK(self,loadConsumerKey):
		self.ConsumerKey = loadConsumerKey
	def setCS(self,loadConsumerSecret):
		self.ConsumerSecret = loadConsumerSecret
	def setAT(self,loadAccessToken):
		self.AccessToken = loadAccessToken
	def setATS(self,loadAccessTokenSecret):
		self.AccessTokenSecret = loadAccessTokenSecret
