"""This tool dumps data from the redis db into a csv file.
   Originally written for processing in MATLAB.
"""
import redis
import argparse
import os
import sys
from hackystone_app.utils import config_parser
from hackystone_app.models.measurement import Measurement
from hackystone_app.models.anchor import Anchor

parser = argparse.ArgumentParser(description='Tool to init redis DB with data.')
parser.add_argument('--type', required=True, type=str,
                    help='either \'tags\' or \'anchors\' specifying what is in the file.')
parser.add_argument('--id', type=str,
                    help='if type is tag, id is required to know which tag to dump to csv file')

r = redis.Redis(host=config_parser.get_redis_config('host'), port=config_parser.get_redis_config('port'), db=0)

def dump_measurement_data(id):
    """Inserts tag measurement data from the given file into redis of the current configuration.
    """
    print(Measurement.toCsv(r, id))

def dump_anchors():
    print(Anchor.toCsv(r))

def main(filetype, id):
    if filetype == 'tags':
        if id == None:
            return 1
        dump_measurement_data(id)
        return 0
    elif filetype == 'anchors':
        dump_anchors()
        return 0
    return 1

def check_flags(args):
    if args.type != 'tags' and args.type != 'anchors':
        parser.print_help()
        return 1
    if args.type == 'tags' and args.id == None:
        print("Received --type=tags\n--id=<str> flag is required.")
        parser.print_help()
        return 1
    return 0

if __name__ == "__main__":
    args = parser.parse_args()
    if check_flags(args):
        sys.exit(1)
    if main(args.type, args.id):
        print("Something went wrong?")
        sys.exit(1)