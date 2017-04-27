#-*- coding: utf-8 -*
# **********************************************************************

# **********************************************************************
# dict 형식을 여러 줄로 출력하는 pretty print 라이브러리 불러오기
from pprint import pprint
# **********************************************************************


from konlpy.tag import Kkma, Twitter, Hannanum, Komoran, Mecab
taggers = [('kkma', Kkma())]
"""
taggers = [('kkma', Kkma()), ('twitter', Twitter()), ('hannanum', Hannanum()),
           ('komoran', Komoran()), ('mecab', Mecab())]
"""

"""
for name, tagger in taggers:
    print('tagger name = %10s\tclass_name = %s' % (name, tagger.__class__))
"""


# csv 형식으로 출력하는 csv 라이브러리 불러오기
import csv

# 파일명
input_file_name = '창의적체험활동_05_진로활동_02_융합형인재전형_total.csv'

# list 선언
dict_list_activity_1 = []

with open(input_file_name, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict_list_activity_1.append(row)






import time
tokens = []
for name, tagger in taggers:

    process_time = time.time()
    _tokens = []

    for i in dict_list_activity_1:
        specials = (i)['SPECIALS']
        _tokens += tagger.pos(specials)

    process_time = time.time() - process_time
    tokens.append(_tokens)

    print('input file name = %s' % input_file_name)
    print('tagger name = %10s, %.3f secs' % (name, process_time))

from collections import Counter
for (name, _), _tokens in zip(taggers, tokens):
    print('\n\nPart of speech tagger: %s' % name)
    counter = Counter(_tokens)
    counter = {word:freq
               for word, freq in counter.items()
               if (freq >= 1000) and (word[1][:2] == 'VV')}
    pprint(sorted(counter.items(), key=lambda x:x[1], reverse=True))
print('end')