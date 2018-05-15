from mongoengine import *
from models.service import Service
import mlab
mlab.connect()
n=Service.objects.get(id='5af5a897ca927424fc5cb657')
print(n['name'])
# other ways
# n=Service.objects.with_id('5af5a897ca927424fc5cb657')
# print(n['name'])
