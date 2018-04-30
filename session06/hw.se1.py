from gmail import *
from random import choice
from datetime import datetime
n=datetime.now().time()
max=datetime.now().time().replace(hour=9,minute=0,second=0,microsecond=0)
min=datetime.now().time().replace(hour=7,minute=0,second=0,microsecond=0)
while min<n and n<max:
    p=input("Moi nhap password: ")
    gmail = GMail('giacatdoccocaubai@gmail.com',p)
    n='''<p>Em ch&agrave;o <span style="color: #ff0000;"><strong>sếp!</strong></span></p>
    <p>H&ocirc;m nay trời&nbsp;đẹp, nắng l&ecirc;n cao. Em thức dậy thấy {{sickness}} qu&aacute;. Sếp cho em nghỉ kẻo l&acirc;y {{sickness}} cả c&ocirc;ng ty!!</p>
    '''
    sickness_list=["Thương hàn","Kiết lị","tiêu chảy","động kinh"]
    sickness=choice(sickness_list)
    msg = Message('Test Message',to='c4e.201708@gmail.com',html=n.replace("{{sickness}}",sickness))
    gmail.send(msg)
    break
else:
    print("Ngủ tiếp đê!!")
