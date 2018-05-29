import mongoengine
# mongo ds157584.mlab.com:57584/video -u <dbuser> -p <dbpassword>
host="ds157584.mlab.com"
port=57584
db_name="video"
user_name="admin"
password="admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
