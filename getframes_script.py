# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))

import sys
from os.path import basename
import os
print(sys.argv[1:])
print(os.environ["PATH"])
import sh
for f in sys.argv[1:]:
	bf = os.path.splitext(basename(f))[0]
	try:
		sh.mkdir(bf)
	except:
		pass
	print("This happened")
	ff = sh.Command("/usr/bin/ffmpeg")
	print(ff)
	ff('-i',f,bf+".mp3",_out=sys.stdin,_err=sys.stderr)
	ff('-i',f,bf+'/'+bf+"\%d.jpg",_out=sys.stdin,_err=sys.stderr)
