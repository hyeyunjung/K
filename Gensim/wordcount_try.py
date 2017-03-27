#-*- coding: utf-8 -*
"""
# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv

# 형태소 분석하는 konlpy 라이브러리 불러오기
#from konlpy.tag import Kkma
#from konlpy.tag import Komoran
from konlpy.tag import Twitter
#from konlpy.tag import Hannanum
from konlpy.tag import Mecab

# konlpy 안에 내장되어 있는 4가지 형태소 분석기 사용선언
#kkma = Kkma()
#komoran = Komoran()
twitter = Twitter()
#hannanum = Hannanum()
mecab = Mecab()

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

# csv 데이터 읽기
with open(CreativeExperActivity_1, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_CreExpAct1.append(row)

with open(CreativeExperActivity_2, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_CreExpAct2.append(row)

with open(CreativeExperActivity_3, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_CreExpAct3.append(row)

with open(CreativeExperActivity_4, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_CreExpAct4.append(row)

with open(CreativeExperActivity_5, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_CreExpAct5.append(row)
"""
"""
print(list_CreExpAct1)
print(list_CreExpAct2)
print(list_CreExpAct3)
print(list_CreExpAct4)
print(list_CreExpAct5)
"""



"""
# 형태소 분석
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

print(list_CreExpAct1)
"""

"""
k = 0
for i in list_CreExpAct1:
    Specials = (i)['Specials']
    pos_mecab = mecab.nouns(Specials)
    list_dic = []
    for j in pos_mecab:
        nouns = (j)
        dic = {'nouns': nouns}
        list_dic.append(dic)
    list_CreExpAct1[k]['nouns_anal'] = list_dic
    k += 1
"""
"""

k = 0
for i in list_CreExpAct1:
    Specials = (i)['Specials']
    pos_twitter = twitter.morphs(Specials)
    list_dic = []
    for j in pos_twitter:
        mor = (j)
        dic = {'morpheme': mor,}
        list_dic.append(dic)
    list_CreExpAct1[k]['pos_twitter_anal'] = list_dic
    k += 1

"""

# 자율활동 (Self_governing_Activity)
# 동아리활동 (Club_Activity)
# 봉사활동 (Voluntary_Activity)
# 진로활동 (Career_Activity)
"""
k = 0
for i in list_CreExpAct1:
    Subject = (i)['Subject']
    list_dic = []
    if Subject == '자율활동':
        Self_governing_Activity = 'Self_governing_Activity'
        list_dic.append(Self_governing_Activity)
    list_CreExpAct1[k]['Activity'] = list_dic
    k += 1

print(list_CreExpAct1)


import nltk
nltk_cea1 = nltk.Text(list_CreExpAct1['pos_twitter_anal'])
print(nltk_cea1)

"""










# 형태소 분석하는 konlpy 라이브러리 불러오기
#from konlpy.tag import Kkma
#from konlpy.tag import Komoran
from konlpy.tag import Twitter
#from konlpy.tag import Hannanum
from konlpy.tag import Mecab

# konlpy 안에 내장되어 있는 4가지 형태소 분석기 사용선언
#kkma = Kkma()
#komoran = Komoran()
twitter = Twitter()
#hannanum = Hannanum()
mecab = Mecab()



text1 = "학급 학예부원(2012.03.02-2013.02.28)으로서 자율형 공립고 출범식 및 교내 체육대회(2012.05.10)에서 학급 단합을 위해 헌신적으로 활동하여 학급의 인화 단결에 기여하였음. 학교 폭력 예방 및 대책 교육(2012.03.22, 울진경찰서), 학교 폭력 예방 교육(2012.09.11), 성교육(2012.09.25, 경북여성통합상담소), 학교 폭력예방 캠페인 1차(2012.10.08), 학교 폭력 예방 캠페인 2차(2012.10.12), 학교 폭력 예방 연극 관람(2012.09.06) 등의 행사에 적극적으로 참여하여 학교 폭력의 부당성에 대한 이해의 폭을 넓히고, 학생 정서 행동 발달 선별 검사(2012.04.25)에 참여하여 자신의 정서 행동 발달 정도를 파악하는 계기를 마련하였음. 재난 대응 안전 한국 훈련(2012.04.26), 정전대비 전국민 훈련(2012.06.20), 나라사랑 마음교육(2012.10.23), 소방 교육(2012.11.12) 등에 적극적으로 참여하여 각종 재난 대비에 대한 교육을 이수하였음. 사제동행 ‘코리아’ 영화관람(2012.06.07), 도서관 시화 전시회(2012.06.01-06.09), 독서의 달 행사(2012.09.10-09.19), 독도의 날 행사(2012.10.22-10.26), 교내 문예 백일장(2012.10.24), 신나는 예술여행 문화체험 활동(2012.11.09), 교내 축제 ‘연호제’ (2012.12.21-12.24)에 적극적으로 참여하여 다양한 문화체험 활동의 기회를 가졌음."



#print(nouns_twitter)
#print(nouns_mecab)

print("twitter")
print("twitter_nouns")
nouns_twitter = twitter.nouns(text1)
frequency_twitter_nouns = {}
for word in nouns_twitter:
    count = frequency_twitter_nouns.get(word, 0)
    frequency_twitter_nouns[word] = count + 1
frequency_twitter_list_nouns = frequency_twitter_nouns.keys()
for words in frequency_twitter_list_nouns:
    print(words, frequency_twitter_nouns[words])


print("twitter_morphs")
morphs_twitter = twitter.morphs(text1)
frequency_twitter_morphs = {}
for word in morphs_twitter:
    count = frequency_twitter_morphs.get(word, 0)
    frequency_twitter_morphs[word] = count + 1

frequency_twitter_list_morphs = frequency_twitter_morphs.keys()

for words in frequency_twitter_list_morphs:
    print(words, frequency_twitter_morphs[words])



print("mecab")
print("mecab_nouns")
nouns_mecab = mecab.nouns(text1)
frequency_mecab_nouns = {}
for word in nouns_mecab:
    count = frequency_mecab_nouns.get(word, 0)
    frequency_mecab_nouns[word] = count + 1
frequency_mecab_list_nouns = frequency_mecab_nouns.keys()
for words in frequency_mecab_list_nouns:
    print(words, frequency_mecab_nouns[words])


print("mecab_morphs")
morphs_mecab = mecab.morphs(text1)
frequency_mecab_morphs = {}
for word in morphs_mecab:
    count = frequency_mecab_morphs.get(word, 0)
    frequency_mecab_morphs[word] = count + 1
frequency_mecab_list_morphs = frequency_mecab_morphs.keys()
for words in frequency_mecab_list_morphs:
    print(words, frequency_mecab_morphs[words])


