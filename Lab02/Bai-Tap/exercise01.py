from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel
from youtube_dl import YoutubeDL


apple_html = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode('utf8')

url = "https://www.apple.com/itunes/charts/songs/"

soup = BeautifulSoup(apple_html, "html.parser")

song = soup.find('section', 'chart-grid')

li_list = song.find_all('li')

datas = []

for li in li_list:
    data = {}
    a = li.h4.a
    data["name song"] = li.h3.a.String
    data["artist"] = a.string
    data["link"] = url + a["href"]
    datas.append(data)

pyexcel.save_as(records=datas, dest_file_name="song-artist.xlsx")

options = {
        'default_search' :'ytsearch',
        'max_download' : 1,
        'format': 'bestaudio/mp3'
}
dl = YoutubeDL(options)
list = []
for song in data:
    list.append(url + a["href"])

dl.download(list)
