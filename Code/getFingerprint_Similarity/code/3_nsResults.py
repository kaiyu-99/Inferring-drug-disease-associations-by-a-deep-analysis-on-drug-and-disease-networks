#通过矩阵和潜在可能的负样本，计算出相似值 （因为潜在的可能负样本文件太大，为了提高计算效率，分为很多子文件在不同的pc上分开进行计算 ）
import numpy as np
import pandas as pd
from collections import ChainMap

for n in range(1,95):
        matrix = pd.read_csv('D:/drug_disease_project/drug-disease/drugs_Matrix.csv', index_col=0)
        print(matrix)
        A = pd.read_csv('D:/drug_disease_project/divideFiles/divide/divide1/file_'+str(n)+'.csv')
        print(A.head())

        def negative_sample(a):
            drug_diseases = {}
            drug_set = set(a.loc[:, 'DrugID'])
            drug_list = list(drug_set)
            a = a.set_index(['DrugID', 'DiseaseID'])
            for i in range(len(drug_set)):
                drug_sample = drug_list[i]
                diseases = set(a.loc[drug_sample].index)
                drug_diseases[drug_sample] = list(diseases)

            return drug_diseases, drug_list


        drug_diseases, drugs = negative_sample(A)
        print('药物与疾病：', drug_diseases)
        print('药物:', drugs)


        def positive_sample(a, drug_diseases, drugs, matrix):
            similarity_score = {}
            a = a.set_index(['DrugID', 'DiseaseID'])
            print(a)
            for i in range(len(drugs)):
                # b = []
                for j in range(len(drug_diseases[drugs[i]])):
                    b = []
                    data = np.array(a.loc[drugs[i]].loc[drug_diseases[drugs[i]][j]]).reshape(-1, 1)
                    for k in range(data.shape[0]):
                        b.append(data[k, 0])
                    similarity_score[drugs[i] + '|' + drug_diseases[drugs[i]][j]] = round(
                        matrix.loc[drugs[i]][matrix.loc[drugs[i]].index.isin(b)].sum(), 3)

            print(similarity_score)
            list1 = [similarity_score]
            print(list1)
            df = pd.DataFrame.from_dict(ChainMap(*list1), orient='index').reset_index()
            df.columns = ['keys', 'values']
            print(df.head())
            df['DrugID'] = df['keys'].map(lambda x: x.split('|')[0])
            df['DiseaseID'] = df['keys'].map(lambda x: x.split('|')[1])
            print(df.head())
            df.to_csv('D:/drug_disease_project/divideFiles/divide/divide1/negative_results_'+str(n)+'.csv', index=None)
            print('over')


        positive_sample(A, drug_diseases, drugs, matrix)
