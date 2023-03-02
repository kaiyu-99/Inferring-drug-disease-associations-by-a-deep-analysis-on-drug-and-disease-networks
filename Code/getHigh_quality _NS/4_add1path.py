#结合2-邻居+1-邻居的scores 得到最后得分
#再按照同样的steps按照正负样本 1:1 1:2 1:3 且阈值为[0,0.05]、[0,0.1]提取负样本
import pandas as pd
#1-邻居得分
df1=pd.read_csv('D:/drug_disease_project/divideFiles/all_choosed_negativesamples/'
                'all_nResults_new_1.0.csv')
#2-邻居得分
df2=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/drugs_Neighbor.csv')
print(df1)
print(df2)
# 外连接 values+indexResult
link=pd.merge(df1,df2,left_on='DrugID',right_on='start_list',how='outer')
print(link)
link['mix_value']=link['values']+link['indexResult']
print(link)
link.to_csv('D:/drug_disease_project/Lab2_detail_NS/all_nResults.csv',index=None)

