import pandas as pd
df = pd.read_json("read.json")
df = df[['title','showUnit','startDate','endDate']]
df.to_csv('write.csv',header=False,index=False)