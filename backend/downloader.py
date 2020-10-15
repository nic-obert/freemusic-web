"""
    Downloader for fmserver
"""

from youtube_dl import YoutubeDL
from os import chdir, rename

from .settings import DOWNLOADER_OPTIONS, DESTINATION
from .utils import rename_file


def download_url(url: str) -> str:

    with YoutubeDL(params=DOWNLOADER_OPTIONS) as dl:
        chdir(DESTINATION)
        # TODO add automatic file renaming and tagging
        name = dl.prepare_filename(
            dl.extract_info(url, download=True))

    new_name = rename_file(name)
    rename(name, new_name)
    
    return new_name

