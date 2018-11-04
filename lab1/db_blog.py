from pymongo import MongoClient

uri = "mongodb://admin:admin2@ds119150.mlab.com:19150/c4e23-blog"

# 1 Connect
client = MongoClient(uri)

# 2 Get default database
db = client.get_default_database()

# 3 Get collection
posts = db["posts"]
movies = db["movies"]

# 4 Create data
new_post = {
    "title": "Hôm nay trời mưa",
    "content": "Tôi vẫn ở nhà code",
}

new_movie = {
    "title": "Batman Arkam",
    "rating": 8.0
}

# 5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

# 5.1 Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    print(p["title"])
    print(p["content"])
    print("%%%%%%%%%%%%%%%%%%")

# 6 Close connectiom
client.close()