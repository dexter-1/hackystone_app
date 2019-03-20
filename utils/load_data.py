"""This tool helps insert data into a redis db.
"""
import redis
import config_parser
import argparse
import os
from hackystone_app.models.measurement import Measurement
from hackystone_app.models.anchor import Anchor

parser = argparse.ArgumentParser(description='Tool to init redis DB with data.')
parser.add_argument('file', type=str,
                    help='file containing data to input into redis DB.')
parser.add_argument('--type', required=True, type=str,
                    help='either \'tags\' or \'anchors\' specifying what is in the file.')

r = redis.Redis(host=config_parser.get_redis_config('host'), port=config_parser.get_redis_config('port'), db=0)

def insert_measurement_data(file):
    """Inserts tag measurement data from the given file into redis of the current configuration.
    """
    measurements = Measurement.readcsv(file)
    for measurement in measurements: 
        measurement.save(r)

def insert_anchor_data(file):
    anchors = Anchor.readcsv(file)
    hset = "anchors"
    for anchor in anchors:
        key = anchor.anchorId
        value = anchor.X + ":" + anchor.Y
        r.hset(hset, key, value) # TODO(rqureshi): change to anchor.redis_write()

def main(filetype, file):
    if filetype == 'tags':
        insert_measurement_data(file)
        return 0
    elif filetype == 'anchors':
        insert_anchor_data(file)
        return 0
    return 1

def check_flags(args):
    if args.type != 'tags' and args.type != 'anchors':
        parser.print_help()
        return 1
    return 0

if __name__ == "__main__":
    args = parser.parse_args()
    if check_flags(args):
        os.exit(1)
    if main(args.type, args.file):
        print("Something went wrong?")
        os.exit(1)