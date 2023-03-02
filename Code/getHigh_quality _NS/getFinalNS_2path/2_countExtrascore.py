#因为步长为1和2结合时文件数据过大，一亿多，故需要把步长为1的划分为很多子文件，再和第二个结合
import pandas as pd

df = pd.read_csv('D:\drug_disease_project\Lab2_detail_NS\Drugs_value.csv', header=None,chunksize=150000)
# print(df)
count = 1
for chunk in df:
    chunk.columns = ['start_list','end_list','value_list']
    name = 'Lab2_detail_NS/divideValue/file_%s.csv' % (count)
    chunk.to_csv(name, index=None)
    print(count)
    count += 1
    #对于每一个潜在负样本（目标药物-目标疾病），计算目标疾病的每一个邻居的每一个邻居药物的权值成绩a*b，
# 取大的作为细分结果
#先找第一个邻居，再找第二个邻居
#距离为1的邻居药物的权值其实就是该网络D:\drug_disease_project\Lab2_detail_NS\Drugs_value_Network_new.csv
#再找距离为2的药物（邻居的邻居）笛卡尔积找出所有可能性
for i in range(1,36,1):
    print(i)
    df=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/divideValue/file_'+str(i)+'.csv')
    print(df.head())
    df_demo=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/Demo.csv')
    #筛选:aa = mix[-((mix['start_list']==data1['end']))]
    # aa = mix[((mix['start_list']！=data1['end'])&(mix['end_list']==data1['start']))]
    # 两个步长相乘2
    # 删去重复项，按条件保留 权值最大的3
    # 和之前的合并
    print("running")
    mix=pd.merge(df,df_demo,left_on='end_list',right_on='start',how='outer')
    print(mix.head())
    #筛选:
    aa = mix[-((mix['start_list']==mix['end']))]
    bb = aa[((aa['end_list']==aa['start']))]
    bb.to_csv('D:/drug_disease_project/Lab2_detail_NS/neighbor/neighbor'+str(i)+'.csv',index=None)


#将子文件中两个步长相乘
for i in range(1,36,1):
    print(i)
    df=pd.read_csv('D:/drug_disease_project/Lab2_detail_NS/neighbor/neighbor'+str(i)+'.csv')
    # 增加一列作为两个权重的乘积列multiply_value
    df['multiply_value']=df['value_list']*df['value']
    print(df.head())
    df.to_csv('D:/drug_disease_project/Lab2_detail_NS/neighbor/new_neighbor'+str(i)+'.csv',index=None)
# 起点相同，按权重乘积降序排序
    df.sort_values(by=['multiply_value'], inplace=True, ascending=False)
    # df2=df.orderBy(df('multiply_value').desc)
    #     删除重复的行，保留上一个（第一个权值乘积为最大的）
    df1 = df.drop_duplicates('start_list', keep='first')
    # df1.to_csv('D:/drug_disease_project/Lab2_detail_NS/newneighbor/final_neighbor'+str(i)+'.csv',index=None)
    df1.to_csv('C:/temp/final_neighbor' + str(i) + '.csv', index=None)
    # 对这些子文件合并，检查是否有重复行（看第一列）