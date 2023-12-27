# f = open('./files/reading_file_example.txt')


# txt = f.read()
# print(txt)


# with open('./files/reading_file_example.txt','a') as f:
#     f.write('This text has to be appended at the end')

# import json
# # python dictionary
# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# with open('./files/json_example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)

import csv
with open('./files/demo.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')