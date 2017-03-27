#-*- coding: utf-8 -*
from konlpy.tag import Mecab

mecab = Mecab()

# 파일명
input_file_name = 'mecab.txt'


# 데이터 읽기
with open(input_file_name, 'r') as read_file:
    text = read_file.read()



pos_text_mecab = mecab.pos(text)

print(pos_text_mecab)