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
#import common.makeConfig

if __name__ == "__main__":
	args = docopt(__doc__)
	print("samples:"+str(args["--config"]))
	if args["--config"]:
#		mc = makeConfig.makeConfig()
		print "input mongodb connect IP:"
		mdb = raw_input()
		print "input twitter api Consumer Key:"
		ck = raw_input()
		print "input twitter api Consumer Secret:"
		cs = raw_input()
		print "input twitter api Access Token:"
		at = raw_input()
		print "input twitter api Access Token Secret:"
		ats = raw_inpit()
#		mc.Create(mdb,ck,cs,at,ats)
	elif args["--train"]:
		print("train")
	else:
		print("main")
