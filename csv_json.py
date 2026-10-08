import csv
import json

with open("students.csv", "r") as file:
    data = list(csv.DictReader(file))

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)