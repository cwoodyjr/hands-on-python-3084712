import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #converts csv dict to json
back_to_dict = json.loads(einstein_json) #converts json back to dict
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f: #brings in file in read mode
    reader = csv.DictReader(f) #creates a dict reader using f 
    laureates = list(reader) #create a list of dict items, each represents a laureate


with open("laureates.json", "w") as f: #opens file in write mode 
    json.dump(laureates, f, indent=2) #using json.dump(no 's') to create json file as f,
                                      #setting indent spaces to 2
