# 将ddfp_Value1.txt里面的药物以及其药物之间的相似度得分创建为矩阵形式，以便下一步筛选负样本
import numpy as np
import pandas as pd

dataset = pd.read_table('D:/drug_disease_project/drug-disease/ddfp_Value1.txt', header=None, sep='\t')
print(dataset)
# 创建一个空列表存储所有的药物名称
drug_names = []
# 通过循环将所有的药物名存储进列表
for i in range(2658):
    drug_names.append(dataset.iloc[i, 1])
# print(drug_names)
# 创建n*n维数组并存储在Dataform数据类型中
datas = pd.DataFrame(np.random.rand(2658, 2658), index=drug_names, columns=drug_names)
print(datas)
# 将药物之间的相似值替换矩阵原来的数据
for j in range(2658):
    datas.loc[dataset.iloc[j, 1]] = list(dataset.iloc[j * 2658:j * 2658 + 2658, 2])
print(datas)
datas.to_csv('drugs_Matrix.csv')
print('over')

