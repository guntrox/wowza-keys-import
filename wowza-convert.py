#!/usr/bin/env python3

import pandas as pd
import json
import sys

map = {}

def convert(fn):
  df = pd.read_excel(fn)

  #print(df[['USB Device ID', 'Full License Key']])

  for index, row in df.iterrows():
    #  print(row['USB Device ID'], row['Full License Key'])
    map[row['USB Device ID']] = row['Full License Key']

def save_json():

  with open('wowza.json', 'w+') as outfile:
    json.dump(map, outfile)
    print("File converted to json")

for arg in sys.argv[1:]:
  convert(arg)

save_json()




