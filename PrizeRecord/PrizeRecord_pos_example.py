#-*- coding: utf-8 -*-
# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv

# 형태소 분석하는 konlpy 라이브러리 불러오기
#from konlpy.tag import Kkma
#from konlpy.tag import Komoran
#from konlpy.tag import Twitter
#from konlpy.tag import Hannanum
from konlpy.tag import Mecab

# konlpy 안에 내장되어 있는 4가지 형태소 분석기 사용선언
#kkma = Kkma()
#komoran = Komoran()
#twitter = Twitter()
#hannanum = Hannanum()
mecab = Mecab()

# 파일명
input_file_name_prize_personal_record = '수원고등학교_학교생활기록부_수상경력_utf1.csv'
input_file_name_prize_school_record = '수원고등학교_교내시상내역_utf1.csv'

# list 선언
dict_list_personal = []
dict_list_school = []
dict_list_personal1 = []
dict_list_school1 = []

# csv 데이터 읽기
with open(input_file_name_prize_personal_record, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_personal.append(row)

with open(input_file_name_prize_school_record, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_school.append(row)

with open(input_file_name_prize_personal_record, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_personal1.append(row)

with open(input_file_name_prize_school_record, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_school1.append(row)

for i in dict_list_personal:
    prize_name = (i)['수상명']
    prize_sc = (i)['수상일자']
    for j in dict_list_school:
        award_name = (j)['시상명']
        if prize_name==award_name:
            k = [prize_name, prize_sc, award_name]
            break


m = 0
for i in dict_list_personal:
    prize_name = (i)['수상명']
    pos_mecab = mecab.pos(prize_name)
    list_dic = []
    for j in pos_mecab:
        mor = (j)[0]
        pos = (j)[1]
        dic = {'morpheme': mor, 'part_of_speech': pos}
        list_dic.append(dic)
    dict_list_personal1[m]['pos_anal'] = list_dic
    m += 1

m = 0
for i in dict_list_school:
    award_name = (i)['시상명']
    pos_mecab = mecab.pos(award_name)
    list_dic = []
    for j in pos_mecab:
        mor = (j)[0]
        pos = (j)[1]
        dic = {'morpheme': mor, 'part_of_speech': pos}
        list_dic.append(dic)
    dict_list_school1[m]['pos_anal'] = list_dic
    m += 1

c = 0
for i in dict_list_personal1:
    pos_personal = (i)['pos_anal']
    print('------------------')
    print(pos_personal)
    print('------------------')
    for j in dict_list_school1:
        pos_school = (j)['pos_anal']
        print('------------------')
        print(pos_school)
        print('------------------')
        if pos_personal==pos_school:
            dict_list_personal1[c]['ppp'] = j
            print('oK')
            break
    c += 1




list_pos = []
list_pos2 = []
list_pos3 = []
list_mecab = []
list_poss = []
doct_list_pos = []

"""
for i in dict_list_personal:
    prize_name = (i)['수상명']
    print(prize_name)
    pos_mecab = mecab.pos(prize_name)
    list_mecab = [prize_name, pos_mecab]
    list_pos2.append(list_mecab)
    for k in list_pos2:
        pos_to = (k)[1]
        for j in pos_to:
            mor = (j)[0]
            pos = (j)[1]
            dic = {'morpheme': mor, 'part_of_speech': pos}
            doct_list_pos = [dic]
    list_pos = [prize_name, pos_mecab, doct_list_pos]
    list_pos3.append(list_pos)
print(list_pos3)


"""

"""
for i in dict_list_personal:
    print(i)
    prize_name = (i)['수상명']
    print(prize_name)
    pos_mecab = mecab.pos(prize_name)
    for j in pos_mecab:
        print(j)
        mor = (j)[0]
        pos = (j)[1]
        dic = [mor, pos]
        list_pos = list_mecab.append(dic)
    list_mecab = [prize_name, list_pos]
    list_pos2.append(list_mecab)
print(list_pos2)

def mecab_for(dict_list_personal):
    for i in dict_list_personal:
        prize_name = (i)['수상명']
        pos_mecab = mecab.pos(prize_name)
        for j in pos_mecab:
            mor = (j)[0]
            pos = (j)[1]
            dic = {'morpheme': mor, 'part_of_speech': pos}
            list_pos[i][j] = list_mecab.append(dic)
        list_pos2.append(prize_name)
        list_poss.append(list_pos[i][j])
    return (list_pos2, list_poss)
doct_list_pos = mecab_for(dict_list_personal)
print(doct_list_pos)
"""
"""
# komoran 출력
def komoran_for(pos_text_komoran):
    for i in pos_text_komoran:
        mor = (i)[0]
        pos = (i)[1]
        dic = {'morpheme': mor, 'part_of_speech': pos}
        list_komoran.append(dic)
    return list_komoran
dict_list_komoran=komoran_for(pos_text_komoran)
"""

"""
# mecab 출력
with open(output_file_name_csv_komo, 'w', newline='') as csvfile:
    fieldnames = ['morpheme', 'prat_of_speech']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in pos_text_komoran:
        mor = (i)[0]
        pos = (i)[1]
        writer.writerow({'morpheme': mor, 'prat_of_speech': pos})
"""
"""

# json Strat
poss = {#'Kkma': dict_list_kkma,
        'komoran': dict_list_komoran
        #'twitter': dict_list_twitter,
        #'hannanum_pos': dict_list_hannanum_pos
        }

# JSON 인코딩
#jsonS = json.dumps(poss, sort_keys=True, indent=4)

with open('pos.json', 'w') as write_file:
    write_file.write(json.dumps(poss, sort_keys=True, indent=4))
"""
