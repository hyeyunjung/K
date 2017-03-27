# MySQL 연동하는 라이브러리 사용선언
import pymysql.cursors
from konlpy.tag import Mecab
mecab = Mecab()



# MySQL Connection 연결
connection = pymysql.connect(host='192.168.1.1',
                             user='grit',
                             password='grit2017',
                             db='grit',
                             charset='utf8')
"""
try:
    with connection.cursor() as cursor:
        # creativeexperactivity_1 선택
        #sql = "SELECT * FROM creativeexperactivity_1"
        sql = "SELECT Year, Grade, Subject, strDate, Specials FROM creativeexperactivity_1 WHERE Subject=%s"
        cursor.execute(sql, ('자율활동',))
        result = cursor.fetchall()
        print(result)
    #connection.commit()
"""


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





try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO CEA1_WORDCOUNT(SEQ, WORD, COUNT) VALUES (, %S, %S)"
        cursor.execute(sql, )








finally:
    connection.close()






for i in list_CreExpAct1:
    Specials = (i)['Specials']



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








"""
try:
   with connection.cursor() as cursor:
       # Create a new record
       sql = "INSERT INTO TEST_USER(EMAIL, PASSWD, NAME) VALUES (%s, %s, %s)"
       cursor.execute(sql, ('webmaster@python.org', 'very-secret', 'webmaster'))

   connection.commit()

   with connection.cursor() as cursor:
       # Read a single record
       sql = "SELECT ID, EMAIL, PASSWD, NAME FROM TEST_USER WHERE EMAIL=%s"
       cursor.execute(sql, ('webmaster@python.org',))
       result = cursor.fetchone()
       print(result)
"""

