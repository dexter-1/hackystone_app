"""This tool helps insert data into a redis db.
"""
import redis
import config_parser
import argparse
import os
from hackystone_app.models.measurement import Measurement

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
    data = readcsv(file)
    N = len(data['tagId'])
    for i in range(0, len(data['tagId'])):
        key = 'tag' + data['tagId'][i] + '_data'
        score = int(data['timestamp'][i])

        dataId = r.incr('data_counter')
        anchorId = data['anchorId'][i]
        rssi = data['rssi'][i]
        element = anchorId + ":" + rssi + ":" + str(dataId)
        r.zadd(key, {element:score})

def insert_anchor_data(file):
    data = readcsv(file)
    N = len(data['anchorId'])
    hset = "anchors"
    for i in range(0, len(data['anchorId'])):
        key = data['anchorId'][i] 
        value = data['X'][i] + ":" + data['Y'][i]
        r.hset(hset, key, value)

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