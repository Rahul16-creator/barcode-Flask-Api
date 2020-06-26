import pymongo

from resources.data import myList
from resources.data import detail_list

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = myclient["Items"]
mycol = mydb["productsDetails"]
# mycol.insert_many(myList)

mycols = mydb["ItemsDetails"]
# mycols.insert_many(detail_list)





