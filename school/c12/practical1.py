import pandas as pd
# QUES:
# create a series with
# a) default indexing and day names of the week as values
# b) change default index and rename them as day1 day2 so on

# a)
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
series1 = pd.Series(days)
print(series1)

# b)
series1 = pd.Series(days , index=['Day 1','Day 2','Day 3','Day 4','Day 5','Day 6','Day 7'])
print(series1)