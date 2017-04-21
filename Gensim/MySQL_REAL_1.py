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
                             db='student_career_oneschool',
                             charset='utf8')
# **********************************************************************


# **********************************************************************
# dict 형식을 여러 줄로 출력하는 pretty print 라이브러리 불러오기
from pprint import pprint
# **********************************************************************



try:
    with connection.cursor() as cursor:
        # DB에 있는 데이터 가져오기
        sql = "SELECT MOGIB1, MOGIB2, SOCIALNUMBER, SCHOOLCODE, SEQNUMBER, YEAR, GRADE, CONTENT, CONTENT2 " \
              "FROM 15_detailability LIMIT 1"
        cursor.execute(sql)
        CEA1 = cursor.fetchall()
        pprint(CEA1)
    # write 작업시 -> connection.commit()


finally:
    connection.close()



