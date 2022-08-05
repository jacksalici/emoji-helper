from fastapi import FastAPI
import random
import json

app = FastAPI()

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
    excludegroup: str = "",
    ):
    fp = open("emoji.json", "r")
    data = json.load(fp)
    emoji = []
    i=0
    groups = group.split(',')
    print(groups)
    index = -1
    while i<n:
            
        index = int(random.random()*(len(data) - 1))

        print (index)
        
        if data[index].get("status")!="fully-qualified" and allstatus==False:    
            continue

        if len(groups) != 0:
            eligible = False
            for g in groups:
                print(data[index].get("group") )
                print(g)
                if data[index].get("group") == g:
                    
                    eligible = True
                    print (data[index])
            
            if not eligible:
                continue

        if len(subgroup) != 0:
            eligible = False
            for s in subgroup:
                if data[index].get("group") == s:
                    eligible = True
            
            if not eligible:
                continue
        


        emoji.append(data[index])
        i+=1

    
    return emoji
