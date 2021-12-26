#!/usr/bin/python3

# {
#     "recommendations": [
#         "shardulm94.trailing-spaces",
#                ...
#         "wraith13.bracket-lens"
#     ]
# }
import sys
import json

extensions_json = sys.argv[1]
with open(extensions_json, "r") as fin:
    data = json.load(fin)
    recommendations = data.get("recommendations", [])
    for recommendation in recommendations:
        print("code --install-extension "+ recommendation)
