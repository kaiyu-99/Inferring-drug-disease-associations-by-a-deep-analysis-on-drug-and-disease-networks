# 对这些潜在负样本评分结果按照评分排序后取需要的样本数
# 对这些潜在负样本score相似值进行排序后取 1:2取126944个
# 对这些潜在负样本score相似值进行排序后取 1:3取190416个
# 当取不够，则按实际取，约等于1:3
import pandas as pd

data1=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/all_nResults.csv')
print(data1)
#所有可能的负样本里面找阈值为[0.0.05]的药物-疾病对，按照正负样本1：1
# print(data1.iloc[63474])  
df = data1.iloc[0:166760]
#df = data1.iloc[0:260638]
print(df)
#data2 = df.sample(n=126944, replace=False, axis=0)  # 随机抽样1：2
#data2 = df.sample(n=190416, replace=False, axis=0)  # 随机抽样1：3
data2 = df.sample(n=63472, replace=False, axis=0)  # 随机抽样1：1
print(data2)
data3 = data2.loc[:, ['DrugID', 'DiseaseID']]
print(data3)
data3.to_csv('D:/drug_disease_project/Lab2_detail_NS/final_NS/11_final_NS_1_2.csv',index=None)

