from redis import StrictRedis, ConnectionPool

# redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')
# redis.set('name', 'Bob')
# print(redis.get('name'))

# 使用ConnectionPool来连接
# ConnectionPool支持URL来构建
pool = ConnectionPool(host='localhost', port=6379, db=0, password='foobared')
redis = StrictRedis(connection_pool=pool)
