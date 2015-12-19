#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import common.Config as Config
from requests_oauthlib import OAuth1Session
import json

class TimeLine(object):

	def __init__(self):
		conf = Config.Config()
		self.ck = conf.getCK()
		self.cs = conf.getCS()
		self.at = conf.getAT()
		self.ats = conf.getATS()

	def getLikeKeyTweet(self,keyword,max_id=-1,since_id=-1):
		url = "https://api.twitter.com/1.1/search/tweets.json"
		query = {
				"q":keyword,
				"count":'100'
			}
		twitterAccess = OAuth1Session(self.ck,self.cs,self.at,self.ats)
		if max_id != -1:
			query['max_id'] = max_id
		if since_id != -1:
			query['since_id'] = since_id
		req = twitterAccess.get(url,params=query)
		if req.status_code == 200:
			return_result = {}
			tw = []
			timeline = json.load(req.text)
			return_result["meta"] = timeline['search_metadata']
			return_result["status"] = timeline['statuses']
			return_result["limit"] = req.headers['x-rate-limit-remaining'] if 'x-rate-limit-remaining' in request.headers else 0
			return_result["reset"] = req.headers['x-rate-limit-reset'] if 'x-rate-limit-reset' in request.headers else 0
			return_result["result"] = True
			for txt in timeline:
				tw.append(text["txt"])
			return_result["txt"] = tw
			return return_result
		else:
			print("ERROR: %d" % req.status_code)
			return {"result":False, "status_code":req.status_code}

	def getTimeLine(self,max_id=-1,since_id=-1):
		min_id = 0
		url = "htpps://api.twitter.com/1.1/statuses/public_timeline.json"
		query = {"count":100}
		if max_id != -1:
			query["max_id"] = max_id
		if since_id != -1:
			query["since_id"] = since_id
		twitterAccess = OAuth1Session(self.ck,self.cs,self.at,self.ats)
		req = twitterAccess.get(url,params=query)
		if req.status_code == 200:
			return_result = {}
			tw = []
			timeline = json.load(req.text)
			return_result["limit"] = req.headers['x-rate-limit-remaining'] if 'x-rate-limit-remaining' in request.headers else 0
			return_result["reset"] = req.headers['x-rate-limit-reset'] if 'x-rate-limit-reset' in request.header else 0
			return_result["result"] = True
			for txt in timeline:
				tw.append(txt["text"])
			for minid in timeline:
				if tmp_id > minid:
					tmp_id = minid -1
			return_result["max_id"] = tmp_id
			return_result["txt"] = tw
			return return_result
		else:
			print("ERROR: %d" % req.status_code)
			return {"result":False, "status_code":req.status_code}
