import pymongo
# 创建客户端

client = pymongo.MongoClient('localhost')
# 创建数据库
db = client['zrsy']
# 创建表
table = db['zrsy_list']