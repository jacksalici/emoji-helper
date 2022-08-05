from xmlrpc.client import Boolean
from fastapi import FastAPI
import random
import json
app = FastAPI()

@app.get("/")
async def root():
    fp = open("emoji.json", "r")

    return json.load(fp)

@app.get("/random")
async def root(n: int = 1, all: Boolean = False):
    fp = open("emoji.json", "r")
    data = json.load(fp)
    emoji = []

    for i in range (0,n):
        while (1):
            index = int(random.random()*(len(data) - 1))
            if data[index].get("status")=="fully-qualified" or all==True:
                emoji.append(data[index])
                break

    return emoji
