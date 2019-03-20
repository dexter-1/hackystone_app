import os
import redis
from measurement import Measurement
from hackystone_app.utils import config_parser

dir_path = os.path.dirname(os.path.realpath(__file__))

r = redis.Redis(host=config_parser.get_redis_config('host'), port=config_parser.get_redis_config('port'), db=0)

def test_readcsv():
    mock_data1_file = os.path.join(dir_path, '../data/mock_data1/tagdata.csv')
    measurements = Measurement.readcsv(mock_data1_file)
    # based on manual inspection
    assert(measurements[-1].tagId == "1")
    assert(measurements[-1].anchorId == "4")
    assert(measurements[-1].rssi == "-90.375")
    assert(measurements[-1].timestamp == "60")
    assert(len(measurements) == 240)

def test_zrangebyscore():
    fakeAnchorId = "fakeAnchorId"
    fakeTagId = "fakeTagId"
    fakeRssi = "0"
    fakeTimestamp = 0
    Measurement.zremrangebyrank(r, fakeTagId, 0, -1)
    fake_measurement = Measurement(fakeAnchorId, fakeTagId, fakeRssi, fakeTimestamp)
    fake_measurement.save(r)
    measurements = Measurement.zrangebyscore(r, fakeTagId, fakeTimestamp, fakeTimestamp)
    assert(len(measurements) == 1)
    assert(measurements[0].rssi == fakeRssi)
    assert(measurements[0].tagId == fakeTagId)
    assert(measurements[0].timestamp == fakeTimestamp)
    assert(measurements[0].anchorId == fakeAnchorId)

def run():
    test_readcsv()
    test_zrangebyscore()

if __name__ == "__main__":
    run()    
