import redis
import config_parser
import csv
import argparse

parser = argparse.ArgumentParser(description='Tool to init redis DB with data.')
parser.add_argument('file', type=str,
                    help='file containing data to input into redis DB.')
parser.add_argument('--type', required=True, type=str,
                    help='either \'tags\' or \'anchors\' specifying what is in the file.')

r = redis.Redis(host=config_parser.get_redis_config('host'), port=config_parser.get_redis_config('port'), db=0)

def readcsv(file):
    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        columns = {}
        for header in headers:
            columns[header] = []
        for row in reader:
            for i in range(0, len(row)):
                columns[headers[i]].append(row[i])
    return columns

def insert_measurement_data(file):
    """Inserts tag measurement data from the given file into redis of the current configuration.
    """
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

insert_measurement_data('../data/mock_data1/tagdata.csv')


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)