import pandas as pd
import openpyxl

data = {
    "직접 넣을 데이터들"
}

df = pd.DataFrame(data)


df.to_excel("data.xlsx", index=False)
print("엑셀 파일이 저장되었습니다.")