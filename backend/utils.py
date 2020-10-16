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
    def rename_file(song: str) -> str:

        # remove quotes (double and single)
        song = song.replace('"', '').replace("'", '')

        # remove text inside parenthesis except for "feat" and "ft"
        song_index = 0
        no_match = False
        while not no_match:
            no_match = True
            try:
                # first try with round parenthesis
                paren_index = song.index('(', song_index)
                closing_paren = song.index(')')
                
            except ValueError:
                # try with square brackets instead
                try:
                    paren_index = song.index('[', song_index)
                    closing_paren = song.index(']')

                except ValueError:
                    continue
                
            no_match = False
            content = song[paren_index:closing_paren]

            if 'feat ' in content or 'ft ' in content.lower():
                song_index = closing_paren
            else:
                song = song[:paren_index] + song[closing_paren + 1:]
            
        
        # remove redundand spaces and trailing spaces, the  return
        return song.replace('  ', '').replace(' .', '.')


