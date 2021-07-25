from youtube_dl import YoutubeDL, postprocessor
import json
import os

options = {
    'format': 'bestaudio[ext=m4a]',
    'quiet': True,
    'outtmpl': '%(artist)s - %(title)s.%(ext)s',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ]
}

URL = "https://music.youtube.com/watch?v=LvyHVgocP_0&feature=share"
DOWNLOAD = True

with YoutubeDL(params=options) as dl:

    info = dl.extract_info(URL, download=DOWNLOAD)
    
    name = dl.prepare_filename(info)

    #new_name = f'{info["tags"][0]} - {info["tags"][2]}'

    #os.rename(name, new_name)
    
print(name)