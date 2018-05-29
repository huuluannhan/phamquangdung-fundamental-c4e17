from models.service import Service
import mlab
mlab.connect()
id_to_find="5af59ceaca927407f470eb6e"
hera=Service.objects.with_id(id_to_find)

# print(hera.to_mongo())
if hera is not None:
    # hera.delete()
    print(hera.address)
    hera.update(set__address="Trần Duy Hưng")
    hera.reload()
    print(hera.address)
else:
    print("Service not found")
# all_service = Service.objects(gender=1)
# for index,service in enumerate(all_service):
#     print(service['name'])
#     if index==9:
#         break
