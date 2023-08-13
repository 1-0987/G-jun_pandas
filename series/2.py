#修改資料
import pandas as pd
s1 = pd.Series([11, 22, 33, 44, 55])
print(f"修改前s1[1]={s1[1]}")
s1[1] = 20
print(f"修改後s1[1]={s1[1]}")