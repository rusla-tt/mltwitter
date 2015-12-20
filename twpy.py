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
import body.Main as Main


if __name__ == "__main__":
	mc = Config.Config()
	main = Main.Main()
	try:
		mc.loadConfig()
	except:
		print("Configure File Not Found")
	args = docopt(__doc__)
	if args["--config"]:
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
		print "default db is csv file. If you want to use the mongodb, please change the settings file"
	elif args["--train"]:
		print "input like keyword for examples: foo,bar"
		likes = raw_input()
		main.train(likes)
	else:
		print "likes tweet start!"
		main.likesTweet()
