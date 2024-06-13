import json
csv_file_path = 'D:\\python\\project\\python\\all_info\\my_tries\\output.json'
with open(csv_file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()
parsed_json = json.loads(file_content)
print(parsed_json)
