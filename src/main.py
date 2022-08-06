from fastapi import FastAPI
import random
import json
import requests as req
app = FastAPI()


def isIn(list, list_name):
    isIn = False
    for element in list:
        if str(list_name).lower() == str(element.lower()).replace("-", " ").replace("and", "&"):
            isIn = True
    return isIn


def jsonOpener():
    # r = req.get('https://raw.githubusercontent.com/jacksalici/emoji-list-api/main/emoji.json')
    # return json.loads(r.text)
    fp = open('emoji.json', 'r')
    return json.load(fp)


def isEligible(element, emoji, noduplicates, skintones, allstatus, group, subgroup, nogroup, nosubgroup):

    if element in emoji and noduplicates:
        return False

    if not skintones and "skin tone" in str(element.get("description")):
        return False

    if element.get("status")!="fully-qualified" and allstatus==False:
        return False

    if len(group) != 0:
        if not isIn(group.split(','), element.get("group")):
            return False

    if len(subgroup) != 0:
        if not isIn(subgroup.split(','), element.get("subgroup")):
            return False

        
    if len(nogroup) != 0:
        if isIn(nogroup.split(','), element.get("group")):
            return False

        
    if len(nosubgroup) != 0:
        if isIn(nosubgroup.split(','), element.get("subgroup")):
            return False
    
    return True



@app.get("/")
async def root():
    return jsonOpener()

@app.get("/random")
async def root(
    n: int = 1,
    allstatus: bool = False,
    noduplicates: bool = True,
    group: str = "", 
    subgroup: str = "", 
    nogroup: str = "",
    nosubgroup: str = "",
    skintones: bool = True,
    ):

    
    data = jsonOpener()
    emoji = []

    

    while len(emoji)<n:

        if len(data) == 0:
            break

        index = int(random.random()*(len(data) - 1))

        if not isEligible(data[index], emoji, noduplicates, skintones, allstatus, group, subgroup, nogroup, nosubgroup):
            data.pop(index)
            continue

        emoji.append(data[index])

    
    return emoji
