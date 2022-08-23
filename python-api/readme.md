# Emoji List API 🏜
Simple yet powerful RESTful API for querying emoji.

```python
import requests
import json

data=requests.get('https://emoji.deta.dev/random?n=10&skintones=False&nogroup=Symbols,Flags')
print(json.loads(data.text))
 
# ["☔","🤵‍♀️","🤍","🗿","🎥","👴","🏃","🥄","🧃","✌️"]
```
## Query syntax

### Endpoint:
`GET`
### Routes:
| Routes | Description |
|--|--|
|`/`| Get list of emoji|
| `/random` | Get random lists of emoji|
| `/groups` | Get the groups hierarchy of the emoji.|

### Parameters:
Valid for both `/` and `/random` routes.

|Parameter: type |Description | Default value |
|-|-|-|
|`n: int`| Number of emoji to retrieve | `1` for `/random` route, `0` (means all) for `/` route
|`allstatus: bool`| By default only emoji with status "fully-qualified" are retrieved. | `False`
|`noduplicates: bool`| In the retrieved list no duplicates are allowed by default. This means that the n value must be considered as a massimum value. | `True`
|`group: str`| Groups of emoji allowed*| `""` (all groups are allowed)
|`subgroup: str` | Subgroups of emoji allowed* | `""` (all subgroups are allowed)
|`nogroup: str` | Groups of emoji not allowed* | `""` (all groups are allowed)
|`nosubgroup: str` |  Subgroups of emoji not allowed* | `""` (all subgroups are allowed)
|`skintones: bool` | Skintones where present. | `False` for `/` route, `True` for `/random` route
|`v: bool` | If the request is verbose, a dictionary is retrieved. | `False`
|`search: str` | Filter by search terms. | `""` (no filter is applied)
|`maxversion: float` | Max version of the emoji | `14.0`


*concatenate more terms with `,`. The terms must be written in kebab-case, "&" become "and". See below for the list of groups and subgroups

## Data Source
The data is parsed from https://unicode.org/Public/emoji/15.0/emoji-test.txt into a JSON list of dictionaries from which the emoji are retrieved. The list, created with the `helper/dumper.py` script, is updated with the very version of Unicode emoji.
Each dictionary presents several information reguarding an emoji, and can be retrieved using the verbose `?v=True` parameter. An example is reported.
The file [emoji.json](https://raw.githubusercontent.com/jacksalici/emoji-list-api/main/src/emoji.json) can be also used for new API.

```json
 {
        "emoji": "🌵",
        "description": "cactus",
        "group": "Animals & Nature",
        "subgroup": "plant-other",
        "code": "1F335",
        "status": "fully-qualified",
        "version": "E0.6"
    }
```
### Emoji Groups and Subgroups
Usable in the query parameters. Multi word terms must be formatted in kebab-case, "&" must be replaced with "and".

```json
{
    "Smileys & Emotion": ["face-smiling", "face-affection", "face-tongue", "face-hand", "face-neutral-skeptical", "face-sleepy", "face-unwell", "face-hat", "face-glasses", "face-concerned", "face-negative", "face-costume", "cat-face", "monkey-face", "emotion"], 
    "People & Body": ["hand-fingers-open", "hand-fingers-partial", "hand-single-finger", "hand-fingers-closed", "hands", "hand-prop", "body-parts", "person", "person-gesture", "person-role", "person-fantasy", "person-activity", "person-sport", "person-resting", "family", "person-symbol"], 
    "Component": ["skin-tone", "hair-style"], 
    "Animals & Nature": ["animal-mammal", "animal-bird", "animal-amphibian", "animal-reptile", "animal-marine", "animal-bug", "plant-flower", "plant-other"], 
    "Food & Drink": ["food-fruit", "food-vegetable", "food-prepared", "food-asian", "food-marine", "food-sweet", "drink", "dishware"], 
    "Travel & Places": ["place-map", "place-geographic", "place-building", "place-religious", "place-other", "transport-ground", "transport-water", "transport-air", "hotel", "time", "sky & weather"], 
    "Activities": ["event", "award-medal", "sport", "game", "arts & crafts"],
    "Objects": ["clothing", "sound", "music", "musical-instrument", "phone", "computer", "light & video", "book-paper", "money", "mail", "writing", "office", "lock", "tool", "science", "medical", "household", "other-object"], 
    "Symbols": ["transport-sign", "warning", "arrow", "religion", "zodiac", "av-symbol", "gender", "math", "punctuation", "currency", "other-symbol", "keycap", "alphanum", "geometric"],
    "Flags": ["flag", "country-flag", "subdivision-flag"]}
```
## Local testing
Clone the repo and install the requirements. Then run the local server using:
```bash
uvicorn main:app --reload  
```
## Licence and contributing
The code is released under MIT Licence.
Feel free to open issues and PRs and suggest new ideas.
Please star 🌟 the repo if you find it useful!

