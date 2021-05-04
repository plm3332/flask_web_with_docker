import pymongo

MONGO_HOST = 'mongodb'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % MONGO_HOST)
db = MONGO_CONN.blog_session_db

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % MONGO_HOST)
        blog_ab = db.blog_ab
    
    return blog_ab
