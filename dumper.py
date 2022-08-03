from base64 import encode
import requests as req
import re
import json


res = req.get('https://unicode.org/Public/emoji/15.0/emoji-test.txt')
data = res.text
emojiDict = []
group=''
subgroup=''

for line in data.splitlines():
    
    if re.search('# subgroup:', line):
        subgroup=re.split('# subgroup: ', line)[1]
    elif re.search('# group: ', line):
        group=re.split('# group: ', line)[1]
    elif re.search("(.+); (.+) # (.+) (E[0-9]+.[0-9]+) (.+)", line):
        
        match = re.match("(.+); (.+) # (.+) (E[0-9]+.[0-9]+) (.+)", line)
        e = {
                'emoji': match.group(3).strip(),
                'description': match.group(5).strip(),
                'group': group,
                'subgroup': subgroup,
                'code': match.group(1).strip(),
                'status': match.group(2).strip(),
                'version': match.group(4).strip(),
            }
        emojiDict.append(e)

try:
    fp = open("emoji.json", 'w')
    json.dump(emojiDict,fp,ensure_ascii=False,indent=4)
except e:
    print(e)
        
        

