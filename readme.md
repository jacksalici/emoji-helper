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

### Parameters:
Valid for both the routes.

|Parameter: type |Description | Default value |
|-|-|-|
|`n: int = 1`| Number of emoji to retrieve | `1` if /random, `0` (means all) if /
|`allstatus: bool`| By default only emoji with status "fully-qualified" are retrieved. | `False`
|`noduplicates: bool`| In the retrieved list no duplicates are allowed by default. This means that the n value must be considered as a massimum value. | `True`
|`group: str`| Groups of emoji allowed*| `""` (all groups are allowed)
|`subgroup: str` | Subgroups of emoji allowed* | `""` (all subgroups are allowed)
|`nogroup: str` | Groups of emoji not allowed* | `""` (all groups are allowed)
|`nosubgroup: str` |  Subgroups of emoji not allowed* | `""` (all subgroups are allowed)
|`skintones: bool` | Skintones where present. | `False` for /, `True` for /random
|`v: bool` | If the request is verbose, a dictionary is retrieved. | `False`
|`search: str = ""` | Filter by search terms. | `""` (no filter is applied)

*concatenate more terms with `,`.

## Data Source
WIP