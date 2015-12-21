#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import wakachi

class GetWords(object):
	def getwords(self,doc):
		wakachi_obj = wakachi.Wakachi()
		words = [s.lower() for s in wakachi_obj.main(doc)]
		return tuole(w for w in words)
