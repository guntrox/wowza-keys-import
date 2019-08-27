#!/usr/bin/env python3

import json
import sys

key = sys.argv[1]

with open('wowza.json') as json_file:
  map = json.load(json_file)
  print("Key", key)
  print("-=-=-=-=-=-=-")
  print(map[key])

with open('Server.license', 'w') as outfile:
  outfile.write(map[key])
  outfile.write("\n")

print("Key:", key, "written to Server.license file")
