#-*- coding: utf-8 -*-
# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv

# Datetime 객체로 만드는 라이브러리 불러오기
import datetime

# 파일명
input_file_name_suwon = '수원고등학교_학교생활기록부_수상경력_utf.csv'
input_file_name_suwon1 = '수원고등학교_교내시상내역_utf.csv'


# list 선언
list_suwon = []
list_suwon1 = []
dict_list_suwon = []
dict_list_suwon1 = []


# csv 데이터 읽기
with open(input_file_name_suwon, 'r', encoding='utf-8') as csvfile:
    fieldnames = ['a', 'b', 'c', 'd', 'e', 'f']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        dict_list_suwon.append(row)

with open(input_file_name_suwon1, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_suwon1.append(row)



#dict_list_suwon[0]['prize_name'] = dict_list_suwon.pop[0]('수상명')

suwon = {'suwon': dict_list_suwon,
         'suwon1': dict_list_suwon1}


print(suwon)

"""
d = dict_list_suwon[0]
#print(d['수상일자'])

"""
"""
def suwonaward(aaward):
    for i in aaward:
        mor = (i)[0]
        pos = (i)[1]
        dic = {'morpheme': mor, 'part_of_speech': pos}
        list_suwon.append(dic)
    return list_suwon
dict_list_suwon = suwonaward(aaward)

"""
"""
date_string = '2014.07.09'
date_ob = datetime.datetime.strptime(d['수상일자'], '%Y.%m.%d').date()
d['수상일자'] = date_ob
print(date_ob)
print(dict_list_suwon)

"""