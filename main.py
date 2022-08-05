from fastapi import FastAPI
import random
import json

app = FastAPI()

def isEligible(list, list_name):
    eligible = False
    for element in list:
        if str(list_name).lower() == str(element.lower()).replace("-"," ").replace("and","&"):
            eligible = True
    return eligible

@app.get("/")
async def root():
    fp = open("emoji.json", "r")

    return json.load(fp)

@app.get("/random")
async def root(
    n: int = 1,
    allstatus: bool = False,
    group: str = "", 
    subgroup: str = "", 
    nogroup: str = "",
    nosubgroup: str = "",
    ):
    fp = open("emoji.json", "r")
    data = json.load(fp)
    emoji = []

    

    while len(emoji)<n:

        if len(data) == 0:
            break

        index = int(random.random()*(len(data) - 1))

        if data[index].get("status")!="fully-qualified" and allstatus==False:
            data.pop(index)    
            continue

        if len(group) != 0:
            if not isEligible(group.split(','), data[index].get("group")):
                data.pop(index)    
                continue

        if len(subgroup) != 0:
            if not isEligible(subgroup.split(','), data[index].get("subgroup")):
                data.pop(index)    
                continue
        
        if len(nogroup) != 0:
            if isEligible(nogroup.split(','), data[index].get("group")):
                data.pop(index)    
                continue
        
        if len(nosubgroup) != 0:
            if isEligible(nosubgroup.split(','), data[index].get("subgroup")):
                data.pop(index)    
                continue

        emoji.append(data[index])

    
    return emoji
