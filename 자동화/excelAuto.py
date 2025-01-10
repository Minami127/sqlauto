import pandas as pd
import mysql.connector
import openpyxl

excel_file = "엑셀 파일 경로 xlsx로 끝나는 파일"
df = pd.read_excel(excel_file, engine="openpyxl")

db = mysql.connector.connect(
    host = "mysql 주소",
    user = "사용자",
    password = "사용자 비밀번호",
    database="데이터베이스 스키마 이름"
)

cursor = db.cursor()

row_count = 0
for index, row in df.iterrows():
    
    query = "insert into test (name,age,email) values (%s, %s, %s)"
    values = (row["name"],row["age"],row["email"])
    cursor.execute(query,values)
    row_count += cursor.rowcount


db.commit()
print(f"{row_count}개의 데이터가 삽입되었습니다.")

cursor.close()
db.close()