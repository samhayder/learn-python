from ytmusicapi import YTMusic

ytmusic = YTMusic(r"0_UDEMY_ANGELA_YU/3_projects/41_50_projects/46_spotify_playlish_musical_timemachine/browser.json")

playlistId = ytmusic.create_playlist("test", "test description")
search_results = ytmusic.search("Oasis Wonderwall")
print(ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']]))