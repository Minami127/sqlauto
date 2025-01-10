import pandas as pd
import mysql.connector
import openpyxl

try:
    excel_file = "C:/Users/hea31/Documents/GitHub/sqlauto/auto/data.xlsx"
    df = pd.read_excel(excel_file, engine="openpyxl")

    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="3728",
        database="test"
    )

    cursor = db.cursor()
    row_count = 0

    for index, row in df.iterrows():
        query = "INSERT INTO test (name, age, team) VALUES (%s, %s, %s)"
        values = (row["name"], row["age"], row["team"])
        cursor.execute(query, values)
        row_count += cursor.rowcount

    db.commit()
    print(f"{row_count}개의 데이터가 삽입되었습니다.")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()