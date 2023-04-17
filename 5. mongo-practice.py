import pymongo
from bson.objectid import ObjectId #載入ObjectId物件

#連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:Asd12345@cluster0.qbrnymz.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite #選擇操作 mywebsite 資料庫
collection = db.users #選擇操作 users 集合

# #篩選集合中的文件資料
# doc = collection.find_one({
#     "e-mail": "julia@julia.com"
# })
# #複合篩選條件
# doc = collection.find_one({
#     "$and":[
#     {"e-mail": "julia@julia.com"},
#     {"password": "123"}
#     ]
# })

#篩選結果排序
cur = collection.find({
    "$or":[
    {"e-mail": "julia@julia.com"},
    {"level": 4}
    ]
}, sort=[
    ("level", pymongo.ASCENDING)
])
for doc in cur:
    print("取得的資料 ", doc)



# #刪除集合中的一筆文件資料
# result= collection.delete_one(
#     {
#     "email":"test3@test3.com"
#     }
# )

# result= collection.delete_many(
#     {
#     "level": 5
#     }
# )
# print("實際上刪除的資料有幾筆:", result.deleted_count)
# #刪除集合中的多筆文件資料




#更新集合中的一筆文件資料
# result = collection.update_one({"e-mail":"julia@julia.com"
# },{
#     "$mul":{
#     "level": 0.5
#     }
# })
#更新集合中的多筆文件資料
# result = collection.update_many({"level": 2
# },{
#     "$set":{
#     "level": 4
#     }
# })

# print("符合條件的文件數量: ", result.matched_count)
# print("實際更新的文件數量: ", result.modified_count)

#取得集合中的第一筆文件資料
# data = collection.find_one()
# print(data)
#根據 ObjectID 取得文件資料
# data = collection.find_one(ObjectId("64393ad6449b4aba54fb6bf4"))
# print(data)
#取得文件資料中的欄位
# print(data["_id"])
# print(data["e-mail"])
#一次取得多筆文件
# cursor = collection.find()
# print(cursor)
# for doc in cursor:
#     print(doc["name"])


#一次新增多筆資料，取得多筆資料的編號
# result = collection.insert_many([
# {
#     "name": "JOHN",
#     "e-mail": "john@john.com",
#     "password": "john",
#     "level": 2
# },{
#     "name": "MARY",
#     "e-mail": "mary@mary.com",
#     "password": "mary",
#     "level": 3
# }
# ])
# print("資料新增成功")
# print(result.inserted_ids)


# #把資料新增到集合中,取得新增資料的編號
# result = collection.insert_one(
# {
#     "name": "SHIEN",
#     "e-mail": "shien@shien.com",
#     "password": "shien",
#     "level": 2
# }
# )
# print("資料新增成功")
# print(result.inserted_id)