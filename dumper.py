import requests as req
import re


res = req.get('https://unicode.org/Public/emoji/15.0/emoji-test.txt')
data = res.text

for line in data.splitlines():
    group=''
    subgroup=''
    if re.search('# subgroup:', line):
        subgroup=re.split('# subgroup: ', line)[1]
        print(subgroup)
    elif re.search('# group: ', line):
        group=re.split('# group: ', line)[1]
        print('GROUP '+group)

