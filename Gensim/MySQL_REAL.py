# **********************************************************************
#-*- coding: utf-8 -*
# **********************************************************************


# **********************************************************************
# MySQL 연동하는 라이브러리 사용선언
import pymysql.cursors
# **********************************************************************

# **********************************************************************
# MySQL Connection 연결
connection = pymysql.connect(host='192.168.1.1',
                             user='grit',
                             password='grit2017',
                             db='studentcareer',
                             charset='utf8')
# **********************************************************************


# **********************************************************************
# dict 형식을 여러 줄로 출력하는 pretty print 라이브러리 불러오기
from pprint import pprint
# **********************************************************************




"""
try:
    with connection.cursor() as cursor:
        # DB에 있는 데이터 가져오기
        sql = "SELECT MOGIB1, MOGIB2, SOCIALNUMBER, SCHOOLCODE, SEQNUMBER, YEAR, GRADE, SUBJECT, STRDATE, SPECIALS " \
              "FROM creativeexperactivity " \
              "WHERE SOCIALNUMBER=%s AND SCHOOLCODE=%s"
        cursor.execute(sql, ('0006903916614DC9984EB7B820DED63E', '8C4BB9B717FE11E787B62C4D549840AA'))
        CEA = cursor.fetchall()
        print(CEA)

    connection.commit()




"""
try:
    with connection.cursor() as cursor:
        # DB에 있는 데이터 가져오기
        sql = "SELECT MOGIB1, MOGIB2, SOCIALNUMBER, SCHOOLCODE, SEQNUMBER, YEAR, GRADE, SUBJECT, STRDATE, SPECIALS " \
              "FROM 10_creativeexperactivity " \
              "WHERE SOCIALNUMBER=%s AND SCHOOLCODE=%s"
        data = (
            ('0006903916614DC9984EB7B820DED63E', '8C4BB9B717FE11E787B62C4D549840AA',),
        )
        cursor.executemany(sql, data)
        CEA = cursor.fetchall()
        pprint(CEA)

    connection.commit()



finally:
    connection.close()



