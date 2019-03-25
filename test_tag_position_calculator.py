import redis
from hackystone_app.utils import config_parser
from hackystone_app import tag_position_calculator

r = redis.Redis(host=config_parser.get_redis_config('host'), port=config_parser.get_redis_config('port'), db=0)

def test_compute_tag_position():
    tagPositionCalculator = tag_position_calculator.TagPositionCalculator(r)
    predictedPos = tagPositionCalculator.compute_tag_position(r, "1", 20)
    assert((predictedPos != [None, None]).all())

def run():
    test_compute_tag_position()

if __name__ == "__main__":
    run() 
