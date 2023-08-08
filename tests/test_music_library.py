from unittest.mock import Mock
from lib.music_library import MusicLibrary

'''When multiple tracks added and keyword searched for, tracks that match that keyword are returned'''
def test_searches_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("Dub") == [fake_matching]
