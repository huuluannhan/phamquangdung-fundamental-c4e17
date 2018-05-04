from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])
