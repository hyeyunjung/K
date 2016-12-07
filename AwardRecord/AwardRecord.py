#-*- coding: utf-8 -*-
# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv



# 파일명
input_file_name_suwon = '수원고등학교_학교생활기록부_수상경력_utf.csv'
input_file_name_suwon1 = '수원고등학교_교내시상내역_utf.csv'


# list 선언
dict_list_suwon = []
dict_list_suwon1 = []


# csv 데이터 읽기
with open(input_file_name_suwon, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_suwon.append(row)

with open(input_file_name_suwon1, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_suwon1.append(row)



suwon = {'suwon': dict_list_suwon,
         'ww': dict_list_suwon1}





"""



# 파일명
input_file_name_csv_kkma = 'output_sr_kkma1.csv'
input_file_name_csv_komo = 'output_sr_komo1.csv'
input_file_name_csv_twit = 'output_sr_twit1.csv'
input_file_name_csv_hpos = 'output_sr_hpos1.csv'
# ---------------------------------------------------------
# list 선언
dict_list_kkma = []
dict_list_komo = []
dict_list_twit = []
dict_list_hpos = []
# ---------------------------------------------------------

# csv 데이터 읽기
with open(input_file_name_csv_kkma, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_kkma.append(row)

with open(input_file_name_csv_komo, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_komo.append(row)

with open(input_file_name_csv_twit, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_twit.append(row)

with open(input_file_name_csv_hpos, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_hpos.append(row)
# ---------------------------------------------------------

# dictionary 로 저장
poss = {'Kkma': dict_list_kkma,
        'komo': dict_list_komo,
        'twit': dict_list_twit,
        'hpos': dict_list_hpos
        }
# ---------------------------------------------------------

# JSON 인코딩
jsonS = json.dumps(poss, sort_keys=True, indent=4)
print(jsonS)

"""