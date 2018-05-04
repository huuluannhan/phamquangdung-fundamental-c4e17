from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
