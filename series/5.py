# 自訂int索引
import pandas as pd
myindex = [3, 5, 7]
price = [100, 200, 300]
s4 = pd.Series(price, index=myindex)
print(s4)
