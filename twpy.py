#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" machine learning twitter timeline.

Usage: 
	python twpy.py -h
	python twpy.py --config
	python twpy.py --train
	python twpy.py
options:
	-h, --help	show this help message and exit
	--config	liketw cli configure setting
	--train		liketw training
"""

from docopt import docopt
import yaml
#import common.makeConfig

if __name__ == "__main__":
	args = docopt(__doc__)
	if args["--config"]:
#		mc = makeConfig.makeConfig()
		print "input mongodb connect IP"
		mdb = raw_input()
		print "input twitter api Consumer Key"
		ck = raw_input()
		print "input twitter api Consumer Secret"
		cs = raw_input()
		print "input twitter api Access Token"
		at = raw_input()
		print "input twitter api Access Token Secret"
		ats = raw_inpit()
#		mc.Create(mdb,ck,cs,at,ats)
	elif args["--train"]:
		print("train")
	else:
		print("main")
