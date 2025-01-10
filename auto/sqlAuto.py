import pandas as pd
import openpyxl

data = {
    "name": ["Lebron", "Curry", "Durant"],
    "age": [40, 36, 36],
    "team": ["LAL", "GSW", "PHX"]
}

df = pd.DataFrame(data)


df.to_excel("data.xlsx", index=False)
print("엑셀 파일이 저장되었습니다.")