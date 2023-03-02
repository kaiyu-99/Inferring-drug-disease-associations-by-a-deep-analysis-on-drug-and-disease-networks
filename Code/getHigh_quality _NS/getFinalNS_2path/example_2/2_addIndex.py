#对2-邻居权值*权值那一列数据增加指数指数f=a*l(p) a=2.26 l(p)为步长2 4.52  0.760974
import pandas as pd
df=pd.read_csv('D:/drug_disease_project/try/example_2/final_neighbor1.csv')
print(df)
# 增加指数 幂运算
df['indexResult']=df['multiply_value']**4.52
print(df.head())
df.to_csv('D:/drug_disease_project/try/example_2/final_neighbor.csv',index=None)

# 再和之前计算的1path的score相加，得到2-path的final negative samples（4_add1path.py）