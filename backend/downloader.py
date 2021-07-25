"""
    Downloader for fmserver
"""

from youtube_dl import YoutubeDL
import os

from .settings import DOWNLOADER_OPTIONS_AUDIO, DOWNLOADER_OPTIONS_VIDEO, DOWNLOADER_OPTIONS_YT_MUSIC, DESTINATION
from .utils import rename_file


def download_url(url: str, download_type: str, auto_rename: bool) -> str:

    if (download_type == 'audio'):
        options = DOWNLOADER_OPTIONS_AUDIO
    elif (download_type == 'video'):
        options = DOWNLOADER_OPTIONS_VIDEO
    elif (download_type == 'yt_music'): 
        options = DOWNLOADER_OPTIONS_YT_MUSIC
        # Youtube Music options already have automatic renaming and tagging
        auto_rename = False

    with YoutubeDL(params=options) as dl:
        os.chdir(DESTINATION)
        
        name = dl.prepare_filename(
            dl.extract_info(url, download=True))

    if auto_rename:
        new_name = rename_file(name)
        os.rename(name, new_name)
        name = new_name

    return name

