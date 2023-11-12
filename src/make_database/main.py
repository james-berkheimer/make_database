import redis
from redis.cluster import RedisCluster


def main():
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    r.set("foo", "bar")
    print(r.get("foo"))
    r.hset(
        "user-session:123",
        mapping={"name": "John", "surname": "Smith", "company": "Redis", "age": 29},
    )
    print(r.hgetall("user-session:123"))
    # rc = RedisCluster(host="127.0.0.1", port=6379)
    # print(rc.get_nodes())
