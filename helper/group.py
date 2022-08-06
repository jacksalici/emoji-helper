import json

data = json.load(open('src/emoji.json', 'r'))
groups = {}

for elem in data:
    if elem.get("group") not in [groups.keys]:
        groups[elem.get("group")] = []

for elem in data:
    if elem.get("subgroup") not in groups[elem.get("group")]:
        test = groups[elem.get("group")].append(str(elem.get("subgroup")))

print(json.dumps(groups))