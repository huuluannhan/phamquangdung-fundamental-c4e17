from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(uri)
db=client.get_default_database()
customers=db["customers"]
events=customers.find({"ref":"events"}).count()
wom=customers.find({"ref":"wom"}).count()
ads=customers.find({"ref":"ads"}).count()

from matplotlib import pyplot
machine_counts=[events,wom,ads]
machine_names=["events","word of mouth","advertisements"]
pyplot.pie(machine_counts,labels=machine_names,autopct="%.1f%%",shadow=True)
pyplot.title("POPULAR REFERRENCES")
pyplot.axis("equal")
pyplot.show()
