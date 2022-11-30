import json
import pandas as pd


catName = [
    "women-clothing",
    "men-clothing",
    "cellphones-telecommunications",
    "computer-office",
    "consumer-electronics",
    "jewelry-accessories",
    "home-garden",
    "luggage-bags",
    "toys-hobbies",
    "sports-entertainment",
    "beauty-health",
    "automobiles-motorcycles",
    "tools",
]

def main():
  # jsFiles = []
  # for id in catName:
  #   file = open("raw_11_"+id+".json","r",encoding='utf8')
  #   data = json.load(file)
  #   jsFiles.extend(data)
  
  # with open("Nov_11_raw.json","w") as file:
  #   json.dump(jsFiles,file)
  #   file.close()
  clean()
  
    
    
def clean():
  with open("Nov_11_raw.json") as file:
  #  data = json.load(file)
   df =  pd.read_json("Nov_11_raw.json")
   df.drop_duplicates(subset=['productId'])
   print(df.describe())
   
     
    
main()