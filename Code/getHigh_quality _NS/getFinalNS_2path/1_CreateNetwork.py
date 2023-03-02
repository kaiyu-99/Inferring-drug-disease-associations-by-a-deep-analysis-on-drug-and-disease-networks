#将药物之间相似度（矩阵）构建成网络，以便后面更细分负样本
import pandas as pd
import numpy as np
dataset = pd.read_table('D:/drug_disease_project/drug-disease/ddfp_Value1.txt', header=None, sep='\t')
print(dataset.head())
dataset1=pd.DataFrame(dataset)
print(dataset1.head())
#构造起始顶点：
#构造终点
#构造边的权重
dataset1.columns["start_list","end_list","value_list"]
# dataset1.rename(columns={"0": "start_list", "end_list": "1","value_list": "2"})
print(dataset1.head())
dataset1.to_csv('D:/drug_disease_project/Lab2_detail_NS/Drugs_value_Network.csv')

