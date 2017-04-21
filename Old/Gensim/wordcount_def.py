#-*- coding: utf-8 -*

# **********************************************************************
# csv 형식을 사용할 수 있게 하는 라이브러리 불러오기
import csv


# ----------------------------------------------------------------------
# csv 데이터 읽는 함수 정의
list_read_cav = []
def read_csv_data(filename):
    csvfile = open(filename, 'r')
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_read_cav.append(row)
    csvfile.close()
    return list_read_cav
# ----------------------------------------------------------------------


# 파일명
CreativeExperActivity_1 = '2014년 학교생활기록부 003_창체.csv'
CreativeExperActivity_2 = '2014년 학교생활기록부 004_창체.csv'
CreativeExperActivity_3 = '2014년 학교생활기록부 005_창체.csv'
CreativeExperActivity_4 = '2014년 학교생활기록부 006_창체.csv'
CreativeExperActivity_5 = '2014년 학교생활기록부 007_창체.csv'

# list 선언
list_CreExpAct1 = []
list_CreExpAct2 = []
list_CreExpAct3 = []
list_CreExpAct4 = []
list_CreExpAct5 = []

# csv 데이터 읽는 함수 사용하여 데이터 불러오기
list_CreExpAct1 = read_csv_data(CreativeExperActivity_1)
list_CreExpAct2 = read_csv_data(CreativeExperActivity_2)
list_CreExpAct3 = read_csv_data(CreativeExperActivity_3)
list_CreExpAct4 = read_csv_data(CreativeExperActivity_4)
list_CreExpAct5 = read_csv_data(CreativeExperActivity_5)

# **********************************************************************

# **********************************************************************
# 형태소 분석하는 konlpy 라이브러리 불러오기
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter
from konlpy.tag import Hannanum
from konlpy.tag import Mecab

# konlpy 안에 내장되어 있는 5가지 형태소 분석기 사용선언
kkma = Kkma()
komoran = Komoran()
twitter = Twitter()
hannanum = Hannanum()
mecab = Mecab()


# ----------------------------------------------------------------------
# konlpy 중 kkma 사용해서 명사 추출하는 함수 정의
dict_kkma = {}
list_kkma = []
def kkma_nouns_count(filename):
    nouns_kkma = kkma.nouns(filename)
    frequency_kkma_nouns = {}
    for word in nouns_kkma:
        count = frequency_kkma_nouns.get(word, 0)
        frequency_kkma_nouns[word] = count + 1
    frequency_kkma_list_nouns = frequency_kkma_nouns.keys()
    for words in frequency_kkma_list_nouns:
        dict_kkma = {words: frequency_kkma_nouns[words]}
        list_kkma.append(dict_kkma)
    return list_kkma
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# konlpy 중 komoran 사용해서 명사 추출하는 함수 정의
dict_komoran = {}
list_komoran = []
def komoran_nouns_count(filename):
    nouns_komoran = komoran.nouns(filename)
    frequency_komoran_nouns = {}
    for word in nouns_komoran:
        count = frequency_komoran_nouns.get(word, 0)
        frequency_komoran_nouns[word] = count + 1
    frequency_komoran_list_nouns = frequency_komoran_nouns.keys()
    for words in frequency_komoran_list_nouns:
        dict_komoran = {words: frequency_komoran_nouns[words]}
        list_komoran.append(dict_komoran)
    return list_komoran
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# konlpy 중 twitter 사용해서 명사 추출하는 함수 정의
dict_twitter = {}
list_twitter = []
def twitter_nouns_count(filename):
    nouns_twitter = twitter.nouns(filename)
    frequency_twitter_nouns = {}
    for word in nouns_twitter:
        count = frequency_twitter_nouns.get(word, 0)
        frequency_twitter_nouns[word] = count + 1
    frequency_twitter_list_nouns = frequency_twitter_nouns.keys()
    for words in frequency_twitter_list_nouns:
        dict_twitter = {words: frequency_twitter_nouns[words]}
        list_twitter.append(dict_twitter)
    return list_twitter
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# konlpy 중 hannanum 사용해서 명사 추출하는 함수 정의
dict_hannanum = {}
list_hannanum = []
def hannanum_nouns_count(filename):
    nouns_hannanum = hannanum.nouns(filename)
    frequency_hannanum_nouns = {}
    for word in nouns_hannanum:
        count = frequency_hannanum_nouns.get(word, 0)
        frequency_hannanum_nouns[word] = count + 1
    frequency_hannanum_list_nouns = frequency_hannanum_nouns.keys()
    for words in frequency_hannanum_list_nouns:
        dict_hannanum = {words: frequency_hannanum_nouns[words]}
        list_hannanum.append(dict_hannanum)
    return list_hannanum
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# konlpy 중 mecab 사용해서 명사 추출하는 함수 정의
dict_mecab = {}
list_mecab = []
def mecab_nouns_count(filename):
    nouns_mecab = mecab.nouns(filename)
    frequency_mecab_nouns = {}
    for word in nouns_mecab:
        count = frequency_mecab_nouns.get(word, 0)
        frequency_mecab_nouns[word] = count + 1
    frequency_mecab_list_nouns = frequency_mecab_nouns.keys()
    for words in frequency_mecab_list_nouns:
        dict_mecab = {words: frequency_mecab_nouns[words]}
        list_mecab.append(dict_mecab)
    return list_mecab
# ----------------------------------------------------------------------

print(mecab_nouns_count(list_CreExpAct1[0]))



"""
text1 = "학급 학예부원(2012.03.02-2013.02.28)으로서 자율형 공립고 출범식 및 교내 체육대회(2012.05.10)에서 학급 단합을 위해 헌신적으로 활동하여 학급의 인화 단결에 기여하였음. 학교 폭력 예방 및 대책 교육(2012.03.22, 울진경찰서), 학교 폭력 예방 교육(2012.09.11), 성교육(2012.09.25, 경북여성통합상담소), 학교 폭력예방 캠페인 1차(2012.10.08), 학교 폭력 예방 캠페인 2차(2012.10.12), 학교 폭력 예방 연극 관람(2012.09.06) 등의 행사에 적극적으로 참여하여 학교 폭력의 부당성에 대한 이해의 폭을 넓히고, 학생 정서 행동 발달 선별 검사(2012.04.25)에 참여하여 자신의 정서 행동 발달 정도를 파악하는 계기를 마련하였음. 재난 대응 안전 한국 훈련(2012.04.26), 정전대비 전국민 훈련(2012.06.20), 나라사랑 마음교육(2012.10.23), 소방 교육(2012.11.12) 등에 적극적으로 참여하여 각종 재난 대비에 대한 교육을 이수하였음. 사제동행 ‘코리아’ 영화관람(2012.06.07), 도서관 시화 전시회(2012.06.01-06.09), 독서의 달 행사(2012.09.10-09.19), 독도의 날 행사(2012.10.22-10.26), 교내 문예 백일장(2012.10.24), 신나는 예술여행 문화체험 활동(2012.11.09), 교내 축제 ‘연호제’ (2012.12.21-12.24)에 적극적으로 참여하여 다양한 문화체험 활동의 기회를 가졌음."
"""
"""
print("kkma")
print(kkma_nouns_count(text1))
print(komoran_nouns_count(text1))
print(twitter_nouns_count(text1))
print(hannanum_nouns_count(text1))
print(mecab_nouns_count(text1))
"""
"""
m = 0
for i in list_CreExpAct1:
    Specials = (i)['Specials']

"""
"""

mecab_nouns_count(Specials)

"""

"""
# ----------------------------------------------------------------------
# csv 데이터 내보내는 함수 정의
list_write_csv = []
def write_csv_data(filename, data_list):
    csvfile = open(filename, 'w', newline='')
    csv_columns = ['word', 'count']
    writer = csv.DictWriter(csvfile, filedname=csv_columns)
    writer.writeheader()
    for row in list_write_csv:
        writer.writerow(row)
    csvfile.close()
    return list_write_csv
# ----------------------------------------------------------------------

write_csv_data(mecab_nouns_count(Specials))
"""

"""
with open(output_file_name_csv_komo, 'w', newline='') as csvfile:
    fieldnames = ['morpheme', 'prat_of_speech']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in pos_text_komoran:
        mor = (i)[0]
        pos = (i)[1]
        writer.writerow({'morpheme': mor, 'prat_of_speech': pos})



m = 0
for i in list_CreExpAct1:
    Specials = (i)['Specials']
    pos_mecab = mecab.pos(Specials)
    list_dic = []
    for j in pos_mecab:
        mor = (j)[0]
        pos = (j)[1]
        dic = {'morpheme': mor, 'part_of_speech': pos}
        list_dic.append(dic)
    list_CreExpAct1[m]['pos_anal'] = list_dic
    m += 1


"""