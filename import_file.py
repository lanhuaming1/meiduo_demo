import redis

sr = redis.StrictRedis(host='172.20.10.14',)

result = sr.set(23,23)

print(result)
rt = sr.keys('*')
print(rt)