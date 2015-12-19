#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import TimeLine

class Tw(object):
	def searchTweetMain(self,keywordlist,lim=2,sleeptime=20):
		tw = TimeLine()
		tl = []
		for key in keywordlist:
			sid = -1
			mid = -1
			count = 0
			while(True):
			 count = count + 1
			 res = tw.getLikeKeytweet(key,max_id=mid,since_id=sid)
			 if res['result'] == False:
				print "status_code", res['status_code']
				break
			 if int(res['limit']) == 0:
				print "limit api"
				diff_sec = int(res['reset']) - now_unix_time()
				print "stopping get tweet : %d" % (diff_sec+5)
				if diff_sec > 0:
					time.sleep(diff_sec + 5)
			 elif count > lim:
				break
			 else:
				tl.append(res["txt"])
				if len(res['status']) == 0:
					print('statuses is none')
				elif 'next_results' in res['metadata']:
					next_url = res['metadata']['next_results']
					pattern = r".*max_id=([0-9]*)\&.*"
					ite = re.finditer(pattern,next_url)
					for i in ite:
						mid = i.group(1)
						break
				else:
					print("key:"+key+"next is none")
					break
		result = []
		for group in tl:
			for tx in group:
				result.append(tx)
		return result

	def homeTweetMain(self,loop=2):
		tw = TimeLine()
		tl = []
		result = []
		max_id = -1
		for i in range(0, loop):
			res = tw.getTimeLine(max_id=mid)
			tl.append(res["txt"])
			max_id = int(res["max_id"])
		for group in tl:
			for tx in group:
				result.append(tx)
		return result
