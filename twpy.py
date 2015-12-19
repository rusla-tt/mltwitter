#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""Usage: twpy.py [-hcts]
twpy.py --config
twpy.py --train
twpy.py --start
Options:
 -h --help
 -c --config
 -t --train
 -s --start

"""

from docopt import docopt
import yaml
import common.Config as Config

if __name__ == "__main__":
	args = docopt(__doc__)
	print("samples:"+str(args["--config"]))
	if args["--config"]:
		mc = Config.Config()
		print "input mongodb connect IP:"
		mdb = raw_input()
		mc.setMongoDB(mdb)
		print "input mongodb connect Port:"
		port = raw_input()
		mc.setMongoPort(port)
		print "input twitter api Consumer Key:"
		ck = raw_input()
		mc.setCK(ck)
		print "input twitter api Consumer Secret:"
		cs = raw_input()
		mc.setCS(cs)
		print "input twitter api Access Token:"
		at = raw_input()
		mc.setAT(at)
		print "input twitter api Access Token Secret:"
		ats = raw_inpit()
		mc.setATS(ats)
		mc.writeConfig()
	elif args["--train"]:
		print("train")
	else:
		print("main")
