import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
url="https://www.apple.com/itunes/charts/songs"
conn=urlopen(url)
raw_data=conn.read()
text=raw_data.decode("UTF8")
soup=BeautifulSoup(text,"html.parser")
section=soup.find("section","section chart-grid")
li_list=section.find_all("li")
itune_list=[]
for li in li_list:
    song=li.h3.a.string
    artist=li.h4.a.string
    item={
    "Song":song,
    "Artist":artist
    }
    itune_list.append(item)
pyexcel.save_as(records=itune_list,dest_file_name="Itunetopsong.xlsx")
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl=YoutubeDL(options)
for i in range(len(itune_list)):
    dl.download(itune_list[i]["Song"])
