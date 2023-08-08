from lib.music_library import MusicLibrary

'''When multiple tracks added and keyword searched for, tracks that match that keyword are returned'''
def test_searches_by_keyword():
    library = MusicLibrary()
    fake_matching = FakeMatchingTrack()
    library.add(fake_matching)
    fake_not_matching = FakeNotMatchingTrack()
    library.add(fake_not_matching)
    assert library.search("Dub") == [fake_matching]

class FakeMatchingTrack():
    def matches(self, keyword):
        return True
    
class FakeNotMatchingTrack():
    def matches(self, keyword):
        return False