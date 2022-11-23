import json

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
  jsFiles = []
  for id in catName:
    file = open("raw_11_"+id+".json","r",encoding='utf8')
    data = json.load(file)
    jsFiles.extend(data)
  
  with open("Nov_11_raw.json","w") as file:
    json.dump(jsFiles,file)
    file.close()
  
    
main()