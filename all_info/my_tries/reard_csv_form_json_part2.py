import csv
import json


csv_file_path = 'D:\python\project\python\lection_3\cars.csv'
json_list = []


with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        json_list.append(row)


with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(json_list, jsonfile, ensure_ascii=False, indent=2)

print("check 'output.json' file")
