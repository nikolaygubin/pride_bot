from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from urllib.parse import urlparse

import os

# storage = MemoryStorage()
result = urlparse(os.environ.get('REDIS_URL'))
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
storage = RedisStorage2(host=hostname, port=port, password=password)
# storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')
bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot = bot, storage = storage)

