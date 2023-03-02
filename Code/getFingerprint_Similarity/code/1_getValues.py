# 通过指纹，转化为0-1向量，再用谷本系数计算两个药物之间的相似度
# -------------读取文件-------------------------
def read_file(filename, list2):
    f1 = open(filename, "r")
    list1 = f1.readlines()
    len1 = len(list1)
    for i in range(len1):
        list2.append(list1[i].strip("\n").split("\t"))


# ----------------计算两向量余弦--------------
def cosVector(x, y):
    if (len(x) != len(y)):
        print('error input,x and y is not in the same space')
        return
    result1 = 0.0
    result2 = 0.0
    result3 = 0.0
    for i in range(len(x)):
        result1 += x[i] * y[i]  # sum(X*Y)
        result2 += x[i] ** 2  # sum(X*X)
        result3 += y[i] ** 2  # sum(Y*Y)

    return (str(result1 / ((result2 * result3) ** 0.5)))


# -----------------将列表元素str转换成int------------------
def change_int(string, list_int):
    list_int = []
    for i in range(len(string)):
        list_int.append(int(string[i]))
    return (list_int)


# -----------------------------------------------
cid_ecfp = []
# read_file("FPrint1.txt", cid_ecfp)
read_file("FPrint1.txt", cid_ecfp)

int_list1 = []
int_list2 = []
cid_vector_value = []
for i in range(len(cid_ecfp)):
    for j in range(len(cid_ecfp)):
        cid1 = cid_ecfp[i]
        cid2 = cid_ecfp[j]
        values = float(cosVector(change_int(cid_ecfp[i][1], int_list1), change_int(cid_ecfp[j][1], int_list2)))
        v = str(round(values, 6))
        cid_vector_value.append(cid_ecfp[i][0] + "\t" + cid_ecfp[j][0] + "\t" + v)

fw = open("ddfp_Value1.txt", "w")
for line in range(len(cid_vector_value)):
    fw.writelines(cid_vector_value[line] + "\n")
fw.close()
print("save")

