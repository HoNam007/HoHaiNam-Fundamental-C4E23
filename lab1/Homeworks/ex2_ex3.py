from pymongo import MongoClient
uri= "mongodb://admin:admin2@ds119150.mlab.com:19150/c4e23-blog"
client= MongoClient(uri)
data_base= client.get_database()
posts=data_base["posts"]
new_post= {
    "title": "Mãi yêu",
    "author": "Bruce Wayne",
    "content":'''
    Mọi thứ về tương lai đều không chắc chắn, nhưng có một điều chắc chắn: 
    Thượng đế đã sắp đặt ngày mai của tất cả chúng ta. Hiện tại chúng ta phải tin tưởng Người và trong vấn đề này, bạn phải hết sức kiên nhẫn.
    ''',
}
posts.insert_one(new_post)
client.close()
