from lib.music_library import MusicLibrary 
from lib.track import Track

'''When multiple tracks added, they are featured in the tracks list'''
def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

'''When multiple tracks added, and a track title is searched for, the matching track is returned'''

def test_searches_for_track_by_full_title():
    library = MusicLibrary()
    track_1 = Track("Nothing Compares 2 U", "Sinead O'Connor")
    track_2 = Track("Dub Be Good To Me", "Beats International featuring Lindy Layton")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Compares") == [track_1]


