"""
    Settings file for fmserver
"""

from os import getenv, getcwd, listdir
from os.path import join
from sys import argv


# whether to use optmized C funcions
USE_C_EXTENSIONS = getenv('FMCEXTENSIONS') == 'TRUE'

# arguments to pass to the youtube-dl downloader
DOWNLOADER_OPTIONS_AUDIO = {
    'format': 'bestaudio[ext=m4a]',
    'quiet': True,
    'outtmpl': '%(title)s.%(ext)s'
}

DOWNLOADER_OPTIONS_YT_MUSIC = {
    'format': 'bestaudio[ext=m4a]',
    'quiet': True,
    'outtmpl': '%(artist)s - %(title)s.%(ext)s',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ]
}

DOWNLOADER_OPTIONS_VIDEO = {
    'format': 'best',
    'quiet': True,
    'outtmpl': '%(title)s.%(ext)s'
}


# get the destination to download the files to
if '-d' in argv:
    DESTINATION = argv[argv.index('-d') + 1]
elif 'music' in listdir(getcwd()):
    DESTINATION = join(getcwd(), 'music')
else:
    DESTINATION = getenv('FMDESTINATION')
    if not DESTINATION:
        DESTINATION = getcwd()
