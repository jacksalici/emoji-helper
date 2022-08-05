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

    groups = group.split(',')
    subgroups = subgroup.split(',')
    
    indexlist = []


    while len(emoji)<n:


        if len(data) == 0:
            break

            
        
        index = int(random.random()*(len(data) - 1))

        print (index)

        if data[index].get("status")!="fully-qualified" and allstatus==False:
            data.pop(index)    
            continue

        if len(group) != 0:
            eligible = False
            for g in groups:
                print(data[index].get("group") )
                print(g)
                if str(data[index].get("group")).lower() == str(g.lower()).replace("-"," ").replace("and","&"):
                    eligible = True
                    print (data[index])
            
            if not eligible:
                data.pop(index)    
                continue

        if len(subgroup) != 0:
            eligible = False
            for s in subgroups:
                if data[index].get("subgroup") == s:
                    eligible = True
            
            if not eligible:
                data.pop(index)    
                continue
        


        emoji.append(data[index])

    
    return emoji
