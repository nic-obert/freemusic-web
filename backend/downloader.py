"""
    Downloader for fmserver
"""

from youtube_dl import YoutubeDL
import os

from .settings import DOWNLOADER_OPTIONS_AUDIO, DOWNLOADER_OPTIONS_VIDEO, DESTINATION
from .utils import rename_file


def download_url(url: str, download_type: str, auto_rename: bool) -> str:

    if (download_type == 'audio'): options = DOWNLOADER_OPTIONS_AUDIO
    elif (download_type == 'video'): options = DOWNLOADER_OPTIONS_VIDEO

    with YoutubeDL(params=options) as dl:
        os.chdir(DESTINATION)
        # TODO add automatic file tagging
        name = dl.prepare_filename(
            dl.extract_info(url, download=True))

    if auto_rename:
        new_name = rename_file(name)
        os.rename(name, new_name)
        name = new_name

    return name

