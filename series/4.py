import pandas as pd
import numpy as np
# start,stop(=end-1<和range用法一樣>)),step,(dtype=None)
s3 = pd.Series(np.arange(0, 8, 2))
print(s3)
