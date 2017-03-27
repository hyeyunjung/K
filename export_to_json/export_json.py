#-*- coding: utf-8 -*-
# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv
import json

# 파일명
input_file_name_activity_1 = '경기여고_자율.csv'
input_file_name_activity_2 = '경기여고_동아리.csv'
input_file_name_activity_3 = '경기여고_봉사.csv'
input_file_name_activity_4 = '경기여고_진로.csv'
input_file_name_activity_5 = '경기여고_봉사실적.csv'

# list 선언
dict_list_prize = []
dict_list_activity_1 = []
dict_list_activity_2 = []
dict_list_activity_3 = []
dict_list_activity_4 = []
dict_list_activity_5 = []

with open(input_file_name_activity_1, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_1.append(row)

with open(input_file_name_activity_2, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_2.append(row)

with open(input_file_name_activity_3, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_3.append(row)

with open(input_file_name_activity_4, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_4.append(row)

with open(input_file_name_activity_5, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_5.append(row)
"""
print(dict_list_activity_1)
print(dict_list_activity_2)
print(dict_list_activity_3)
print(dict_list_activity_4)
print(dict_list_activity_5)

"""



# json Start
creative_experiential_activities = {'activity': {'autonomy': dict_list_activity_1,
                     'club': dict_list_activity_2,
                     'service': dict_list_activity_3,
                     'career': dict_list_activity_4,
                     'service_record': dict_list_activity_5
                     }
        }

# JSON 인코딩

with open('creative_experiential_activities.json', 'w') as write_file:
    write_file.write(json.dumps(creative_experiential_activities, sort_keys=True, indent=4))


print(creative_experiential_activities)
