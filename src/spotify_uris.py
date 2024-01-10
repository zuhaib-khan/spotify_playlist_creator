from billboard import get_billborad_songs
from spotify_auth import sp


#year = date.split('-')[0]
def get_spotify_uris(song_names):
    uris = []
    
    for song in song_names:
        
        result = sp.search(q=f"track:{song}", type="track")
        tracks = result['tracks']['items']
        
        if tracks:
            uris.append(tracks[0]['uri'])
        else:
            print(f"Song {song} not found on Spotify.")
            continue
        
    return uris

date = input('Enter the date in YYYY-MM-DD format: ')
song_list = get_billborad_songs(date_selection=date)
spotify_uris = get_spotify_uris(song_names=song_list)
user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)

sp.playlist_add_items(playlist_id= playlist['id'],items=spotify_uris)
print('playlist created!')

