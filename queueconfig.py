from huey import RedisHuey

huey = RedisHuey('distributor', host='localhost')
