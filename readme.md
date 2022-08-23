### Simple yet powerful tools for managing and querying emoji list.


## 📦 [npm Package](https://github.com/jacksalici/emoji-helper/tree/main/npm-package)

```
npm i emoji-random-list
```

```javascript
var emoji = require("emoji-random-list")
console.log(emoji.random({n: 5, group: 'objects'}))
//[ '🪒', '📕', '🔋', '🔩', '💷' ]
```

#### [Go to the docs 📦🗂](https://github.com/jacksalici/emoji-helper/tree/main/npm-package)

## 🐍 [Python API](https://github.com/jacksalici/emoji-helper/tree/main/python-api)

```python
import requests
import json

data=requests.get('https://emoji.deta.dev/random?n=10&skintones=False&nogroup=Symbols,Flags')
print(json.loads(data.text))
 
# ["☔","🤵‍♀️","🤍","🗿","🎥","👴","🏃","🥄","🧃","✌️"]
```

#### [Go to the docs 🐍🗂](https://github.com/jacksalici/emoji-helper/tree/main/python-api)