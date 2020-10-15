"""
    Useful functions for fmserver
"""

from socket import socket, AF_INET, SOCK_DGRAM
from backend import settings


if settings.USE_C_EXTENSIONS:
    import c_rename
    def rename_file(song: str) -> str:
        return c_rename.c_rename_file(song)

else:
    # substrings to remove from file name
    TO_REMOVE = (
        '(audio)',
        '(official audio)',
        ' lyrics',  # here the space is intentional
        '(lyrics)',
        '(official video)',
        '[official video]',
        '[official audio]',
        '[audio]',
        '[lyrics]',
        '(official music video)',
        '[official music video)',
        '"',
        "'",
        '  '
    )

    def rename_file(song: str) -> str:
        name = song.lower()
        no_match = False
        while not no_match:
            no_match = True
            for s in TO_REMOVE:
                try:
                    # if the substring to remove is fount inside the file name
                    # remove it
                    index = name.index(s)
                    song = song[:index] + song[index + len(s):]
                    # reduce name's size to speed up code execution
                    name = song.lower()
                    no_match = False
                except ValueError:
                    continue
        
        # replace trailing space before file extension
        return song.replace(' .', '.')

