from mongoengine import *
import mlab
mlab.connect()
Docs.objects.get(id='5af5a897ca927424fc5cb657')
print(Docs)
