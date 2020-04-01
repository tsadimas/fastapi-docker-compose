from fastapi import FastAPI
import redis
import os

app = FastAPI()
redis_server=os.getenv("REDIS_SERVER", default="localhost")
redis_pass=os.getenv("REDIS_PASS", default="")
print("REDIS_SERVER = {}".format(redis_server))
print("REDIS_PASS = {}".format(redis_pass))
r = redis.StrictRedis(host=redis_server, port=6379,
        password=redis_pass,charset="utf-8", decode_responses=True)

@app.get("/")
async def root():
    if r.exists('visits') == 1: 
        visits = r.get("visits")
        print("Read {} visits".format(visits))
    else:
        visits = 0
    print("Save {} visits".format(int(visits) +1))
    r.set("visits", int(visits)+1)
    return {"message": "Hello World, visits {}".format(str(visits))}
