# '''
# 【项目01】  商铺数据加载及存储
#
# 作业要求：
# 1、成功读取“商铺数据.csv”文件
# 2、解析数据，存成列表字典格式：[{'var1':value1,'var2':value2,'var3':values,...},...,{}]
# 3、数据清洗：
# ① comment，price两个字段清洗成数字
# ② 清除字段缺失的数据
# ③ commentlist拆分成三个字段，并且清洗成数字
# 4、结果存为.pkl文件
#
# '''

#数据读取

f = open("D:\\科研数据处理\\立方数据学社\\python基础\\《Python基础》课程资料\\课程数据\\任务9：项目实战\\关卡1：商铺数据的加载及数据清洗\\商铺数据.csv","r",encoding="utf8")
# for i in f.readlines()[:100]:
    # print(i.split(",")[6])
    # print(i.split(",")[2]) #按行显示数据，以逗号分割显示，显示索引为2的前10条的评论数统计

# 创建comment、price、commentlist清洗函数
# 函数式编程

def fcm(s):
    if "条" in s:
        return int(s.split(" ")[0])
    else:
        return "缺失数据"
# 评论数清洗查看
# f.seek(0)
# for i in f.readlines()[:20]:
#     cm = fcm(i.split(",")[2])
#     print(cm)

def fpr(s):
    if "￥" in s:
        return int(s.split("￥")[-1])
    else:
        return "缺失数据"
#价格清洗查看
# f.seek(0)
# for i in f.readlines()[:20]:
#     pr = fpr(i.split(",")[4])
#     print(pr)

def fcl(s):
    if" " in s:
        quality = float(s.split("                                ")[0][2:])
        environment = float(s.split("                                ")[1][2:])
        service = float(s.split("                                ")[2][2:])
        return [quality,environment,service]
    else:
        return "缺失数据"
#评论列表清洗查看
# f.seek(0)
# for i in f.readlines()[:20]:
#     cl = fcl(i.split(",")[6])
#     print(cl)

# 数据清洗
datalst = [] #创建空列表

f.seek(0)
n = 0 # 创建计数变量
for i in f.readlines()[1:]: #第一行是标题不做数据清洗
    data = i.split(",")
    # print(data)
    classify = data[0]                    #提取分类
    name = data[1]                        #提取店铺名称
    comment_count = fcm(data[2])          #提取评论数量
    star = data[3]                        #提取星级
    price = fpr(data[4])                  #提取价格
    add = data[5]                         #提取地址
    qua = fcl(data[6])[0]                 #提取质量评分
    env = fcl(data[6])[1]                 #提取环境评分
    ser = fcl(data[6])[2]                 #提取服务评分
    if "缺失数据" not in [comment_count,price,qua]: #用于判断是否有确实数据
        n += 1
        data_re = [["class",classify],
                   ["name",name],
                   ["comment_count",comment_count],
                   ["star",star],
                   ["price",price],
                   ["address",add],
                   ["quality",qua],
                   ["environment",env],
                   ["service",ser]]
        datalst.append(dict(data_re))#生成字典，并存入datalst
        print("成功加载了%i条数据" %n)
    else:
        continue
print(datalst)
print("共加载了%i条数据" %n)