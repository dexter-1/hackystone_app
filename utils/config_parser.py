"""Methods to retrieve current configuration.
"""
from ConfigParser import SafeConfigParser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

configuration = os.path.join(dir_path, '../configurations/local.cfg')

parser = SafeConfigParser()
parser.read(configuration)

def get_redis_config(key):
    return parser.get('redis', key)