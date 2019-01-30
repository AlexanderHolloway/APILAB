from PGDatabase import Database
from Lyrics_Scraper import Artist, Album, Song

newDatabase = Database()
newDatabase.delete_song_table()
newDatabase.create_song_table()

# 'SONG_NAME, ARTIST, ALBUM_TYPE, ALBUM_NAME, ALBUM_YEAR, LYRICS'

artistList = ['journey']


songInfo = []

for artist in artistList:
    if len(songInfo) > 0:
        break
    artistObj = Artist(artist)
    artistAlbums = artistObj.get_album_infos()
    for albumInfo in artistAlbums:
        if len(songInfo) > 0:
            break
        albumType = albumInfo['type']  # string
        albumName = albumInfo['title']  # string
        albumYear = albumInfo['year']  # string
        album = Album(artist, albumInfo)
        songs = album.get_album_songs()
        for song in songs:
            if len(songInfo) > 0:
                break
            songObj = Song(artist, song)
            lyrics = songObj.get_lyrics()
            # print(lyrics)
            # lyrics = "These are the lyrics"
            songInfo = [song, artist, albumType, albumName, albumYear, lyrics]
            newDatabase.insert(songInfo)
