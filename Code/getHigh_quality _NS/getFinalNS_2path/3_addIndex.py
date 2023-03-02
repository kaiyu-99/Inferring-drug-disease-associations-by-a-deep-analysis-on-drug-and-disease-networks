#对2-邻居权值*权值那一列数据增加指数指数
import pandas as pd
df=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/Neighbor.csv')
print(df)
# 增加指数 幂运算
df['indexResult']=df['multiply_value']**4.52
print(df.head())
df.to_csv('D:/drug_disease_project/Lab2_detail_NS/drugs_Neighbor.csv',index=None)
