# 如果想用非int標籤，需用字串格式
import pandas as pd
fruits = ['Orange', 'Banana', 'Apple']
price = [100, 200, 300]
s5 = pd.Series(price, index=fruits)
'''
可改寫為s5 = pd.Series(price, index=['Orange', 'Banana', 'Apple'])
'''
print(s5)
