from youtube_dl import YoutubeDL

#1
dl = YoutubeDL()
url01 = ['https://www.youtube.com/watch?v=WHK5p7JL7g4']
dl.download(url01)


urls =['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic']
for url in urls:
    dl.download(url)

#2
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

#3
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])

#4
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
