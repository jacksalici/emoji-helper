# emoji-random-list package
Simple yet powerful npm package for querying emoji. Note: the project could be unstable since it's stil wip.

## Example
```
npm i emoji-random-list
```

```javascript
var emoji = require("emoji-random-list")
console.log(emoji.random({n: 5, group: 'objects'}))
//[ '🪒', '📕', '🔋', '🔩', '💷' ]
```

## Usage
### Functions:
| Function | Description |
|--|--|
|`list`| Get list of emoji|
| `random` | Get random lists of emoji|

### Parameters:
Valid for both `list` and `random` functions.

|Parameter: type |Description | Default value |
|-|-|-|
|`n: int`| Number of emoji to retrieve | `1` for `random` function, `0` (means all) for `list` function
|`allstatus: bool`| By default only emoji with status "fully-qualified" are retrieved. | `false`
|`noduplicates: bool`| In the retrieved list no duplicates are allowed by default. This means that the n value must be considered as a massimum value. | `true`
|`group: string`| Groups of emoji allowed*| `""` (all groups are allowed)
|`subgroup: string` | Subgroups of emoji allowed* | `""` (all subgroups are allowed)
|`nogroup: string` | Groups of emoji not allowed* | `""` (all groups are allowed)
|`nosubgroup: string` |  Subgroups of emoji not allowed* | `""` (all subgroups are allowed)
|`skintones: bool` | Skintones where present. | `false` for `list` function, `true` for `listrandom` function
|`v: bool` | If the request is verbose, a dictionary is retrieved. | `false`
|`search: string` | Filter by search terms. | `""` (no filter is applied)
|`maxversion: number` | Max version of the emoji | `14.0`
|`genders: bool` | If true, all genders of people are allowed, neutral gender only otherwise | `false`
|`offset: number` | Offset between the first emoji and the start of the return list. (avaible only for the `list` function)  | `0`


*concatenate more terms with `,`. See below for the list of groups and subgroups

## Data Source
The data is parsed from https://unicode.org/Public/emoji/15.0/emoji-test.txt into a JSON list of dictionaries from which the emoji are retrieved. The list, created with the `helper/dumper.py` script, is updated with the very version of Unicode emoji.
Each dictionary presents several information reguarding an emoji, and can be retrieved using the verbose `v=true` parameter. An example is reported.
The file [emoji.json](https://raw.githubusercontent.com/jacksalici/emoji-helper/main/helper/emoji.json) can be also used for new API.

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
    "Flags": ["flag", "country-flag", "subdivision-flag"]
    }
```

## Licence and contributing
The code is released under MIT Licence.
Feel free to open issues and PRs and suggest new ideas.
Please star 🌟 the repo if you find it useful!

