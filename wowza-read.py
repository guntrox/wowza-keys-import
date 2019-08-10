#!/usr/bin/env python3

import json

with open('wowza.json') as json_file:
  map = json.load(json_file)
  print("Key U622")
  print("-=-=-=-=-=-=-")
  print(map["U622"])
