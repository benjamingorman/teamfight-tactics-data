import json
import itertools
from collections import defaultdict

CLASS_LINK_MIN_CHAMPS = 2

with open('database.json', 'r') as data:
    champs = json.load(data)

class_lookup = defaultdict(lambda: [])

for champ in champs:
    name_with_cost = "{} {}".format(champ["name"], champ["cost"])
    for claz in champ["classes"]:
        class_lookup[claz].append(name_with_cost)

# Reverse lookup - class to champion list
with open("class_lookup.json", "w") as f:
    json.dump(class_lookup, f, indent=4, sort_keys=True)

# Iterate over every pair of classes and find ones with shared champions
with open("linked_classes.txt", "w") as f:
    for (class_a, class_b) in itertools.combinations(sorted(class_lookup.keys()), 2):
        # if class_a == class_b:
        #     continue
        (set_a, set_b) = set(class_lookup[class_a]), set(class_lookup[class_b])
        common = set_a.intersection(set_b)

        if len(common) >= CLASS_LINK_MIN_CHAMPS:
            print(class_a, "<->", class_b, common, file=f)

