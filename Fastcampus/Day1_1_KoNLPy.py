from konlpy.tag import Kkma, Twitter, Hannanum
from pprint import pprint

taggers = [('kkma', Kkma()), ('twitter', Twitter()), ('hannanum', Hannanum())]

for tagger in taggers:
    name = tagger[0]       # tagger라는 tuple의 0번째 요소
    tagger = tagger[1]     # tagger라는 tuple의 1번째 요소
    print('tagger name = %10s\tclass_name = %s' % (name, tagger.__class__))

'%.3f' % 1.3205533