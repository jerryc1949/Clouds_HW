import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

res1=pd.read_csv('res1_stats_history.csv')
res2=pd.read_csv('res2_stats_history.csv')
res3=pd.read_csv('res3_stats_history.csv')
res4=pd.read_csv('res4_stats_history.csv')

res1=res1['Requests/s'].to_numpy()
res2=res2['Requests/s'].to_numpy()
res3=res3['Requests/s'].to_numpy()
res4=res4['Requests/s'].to_numpy()

time=len(res1)
x=list(range(time))
plt.xlabel('req/s')
plt.ylabel('time/s')
plt.plot(x, res1,label='i')
plt.plot(x, res2,label='ii')
plt.plot(x, res3,label='iii')
plt.plot(x, res4,label='iv')
plt.legend()
plt.show()