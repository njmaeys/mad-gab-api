import pandas as pd
from utility import random_num

def read_json_gabs():
  data = pd.read_json('gabs.json')
  data = data.to_dict()
  return data

def get_all_gabs():
  data = read_json_gabs()
  return {'data': data}, 200

def get_one_gab():
  single_gab = {}
  data = read_json_gabs()

  gab_index = random_num(len(data["gab"]))

  single_gab["gab"] = data["gab"][gab_index] 
  single_gab["gabValue"] = data["gabValue"][gab_index] 

  return {'data': single_gab}, 200
