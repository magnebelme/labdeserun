# Assume 'lyrics' is a list and 'album' is a variable containing the album name
lyrics = []

def add_album_info_to_lyrics(album):
    lyrics.append(f'[al:{album}]')

# Adding album information to the lyrics
album_name = "Greatest Hits"
add_album_info_to_lyrics(album_name)

# Now 'lyrics' might contain: ['[al:Greatest Hits]']
