import pandas as pd

df = pd.read_html('read.html')
df = df[1]
df.to_csv('write.csv',index=False,encoding='utf-8',float_format='%.3f')