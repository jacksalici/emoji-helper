from fastapi import FastAPI, Response
import random
import json
import requests as req
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def isIn(list, list_name):
    isIn = False
    for element in list:
        if str(list_name).lower() == str(element.lower()).replace("-", " ").replace("and", "&"):
            isIn = True
    return isIn


def returnHelper(emoji, verbose):
    if not verbose:
        e = []
        for el in emoji:
            e.append(el.get("emoji"))
        return e
    return emoji


def jsonOpener():
    # r = req.get('https://raw.githubusercontent.com/jacksalici/emoji-list-api/main/emoji.json')
    # return json.loads(r.text)
    fp = open('emoji.json', 'r')
    return json.load(fp)


def isEligible(element, emoji, noduplicates, skintones, allstatus, group, subgroup, nogroup, nosubgroup, search, maxversion):

    if element in emoji and noduplicates:
        return False

    if not skintones and "skin tone" in str(element.get("description")):
        return False

    if element.get("status") != "fully-qualified" and allstatus == False:
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

    if len(search) != 0:

        if search not in str(element.get("description")):
            return False

    if float(element.get("version").split("E")[1]) > maxversion:
        return False

    return True


@app.get("/")
async def root(
    n: int = 0,
    allstatus: bool = False,
    noduplicates: bool = True,
    group: str = "",
    subgroup: str = "",
    nogroup: str = "",
    nosubgroup: str = "",
    skintones: bool = False,
    v: bool = False,
    search: str = "",
    maxversion: float = 14.0
):

    data = jsonOpener()
    emoji = []

    for elem in data:

        if n != 0 and len(emoji) == n:
            break

        if not isEligible(elem, emoji, noduplicates, skintones, allstatus, group, subgroup, nogroup, nosubgroup, search, maxversion):
            continue

        emoji.append(elem)

    return returnHelper(emoji, v)


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
    v: bool = False,
    search: str = "",
    maxversion: int = 14.0

):

    data = jsonOpener()
    emoji = []

    while len(emoji) < n:

        if len(data) == 0:
            break

        index = int(random.random()*(len(data) - 1))

        if not isEligible(data[index], emoji, noduplicates, skintones, allstatus, group, subgroup, nogroup, nosubgroup, search, maxversion):
            data.pop(index)
            continue

        emoji.append(data[index])

    return returnHelper(emoji, v)


@app.get("/groups")
async def root():
    data = jsonOpener()
    groups = {}

    for elem in data:
        if elem.get("group") not in [groups.keys]:
            groups[elem.get("group")] = []

    for elem in data:
        if elem.get("subgroup") not in groups[elem.get("group")]:
            test = groups[elem.get("group")].append(str(elem.get("subgroup")))

    return groups
