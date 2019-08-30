from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

db = client['tutorial']
col1 = db['articles']

doc1 = {
    "title": "article agfgbout mondfggodb and python",
    "author": "Akashfg Senta",
    "publication_date": datetime.utcnow(),
}

doc2 = {
    "title": "A article agfgbout mondfggodb and python",
    "author": "Akashfg Senta",
    "publication_date": datetime.utcnow(),
}

doc3 = {
    "title": "The article agfgbout mondfggodb and python",
    "author": "Akashfg Senta",
    "publication_date": datetime.utcnow(),
}
#doc_id = col1.insert_one(doc).inserted_id
#print(doc_id)

#my_doc = col1.find_one({'_id': doc_id})
#print(my_doc)

col1.insert_many([doc1,doc2,doc3])

many_docs = col1.find({'publication_date':{'$lt':datetime(2019,8,29)}})
for doc in many_docs:
    print(doc)