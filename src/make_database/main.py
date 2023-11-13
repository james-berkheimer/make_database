import redis
from redis.cluster import RedisCluster


def main():
    # r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    r = redis.Redis(decode_responses=True)
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    print(r.get("Bahamas"))
