from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(uri)
db=client.get_default_database()
blog=db["posts"]
post={
"title":"My spoil for Avenger 4",
"author":"Quang Dũng",
"content":"Captain Marvel will appear with overwhelming power, cooperate with Adam Warlock to defeat stupid velvet potato then have first meeting with Prof.X. Cap, IM will die due to end of contract kkk"
}
blog.insert_one(post)
