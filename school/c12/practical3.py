import pandas as pd
import numpy as np
arr1 = np.arange(5,11)
s1 = pd.Series(arr1,index=['a','b','c','d','e','f'])
s2=pd.Series([12.5,18.0,-2.5],index=['a','c','f'])
print(s1)
print(s1.add(s2,fill_value=10))
print(s1.sub(s2))
print(s1.mul(s2))
print(s1.div(s2,fill_value=5))
print(s1.head(3),s2.tail(1))
print(s1.size,s2.size)