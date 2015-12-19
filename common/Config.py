#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import yaml
from os import path

class Config():
	mongoIP = ""
	mongoPort = 0
	ConsumerKey = ""
	ConsumerSecret = ""
	AccessToken = ""
	AccessTokenSecret = ""
	def __init__(self):
		self.loadConfig()

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

	def writeConfig(self):
		data = dict(
			mongoip = str(self.getMongoDB()),
			mongoport = int(self.getMongoPort()),
			ck = str(self.getCK()),
			cs = str(self.getCS()),
			at = str(self.getAT()),
			ats = str(self.getATS())
		)
		with open(path.dirname(path.abspath(__file__))+"/../config/config.yaml",'w') as outfile:
			outfile.write(yaml.dump(data,default_flow_style=True))
	def getMongoDB():
		return self.mongoIP
	def getMongoPort():
		return self.mongoPort
	def getCK():
		return self.ConsumerKey
	def getCS():
		return self.ConsumerSecret
	def getAT():
		return self.AccessToken
	def getATS():
		return self.AccessTokenSecret
	def setMongoDB(loadmongoip):
		self.mongoIP = loadmongoip
	def setMongoPort(loadPort):
		self.mongoPort = loadPort
	def setCK(loadCosumerKey):
		self.ConsumerKey = loadConsumerKey
	def setCS(loadConsumerSecret):
		self.ConsumerSecret = loadConsumerSecret
	def setAT(loadAccessToken):
		self.AccessToken = loadAccessToken
	def setATS(loadAccessTokenSecret):
		self.AccessTokenSecret = loadAccessTokenSecret
