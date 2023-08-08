from lib.track import Track 

'''With a title and an artist and a search keyword for the full title, the match returned is True'''
def test_matches_on_full_title():
    track = Track("Nothing Compares 2 U", "Sinead O'Connor")
    assert track.matches("Nothing Compares 2 U") == True

'''Given a title and an artist and a search keyword for a partial title, the match returned is True'''
def test_matches_on_partial_title():
    track = Track("Nothing Compares 2 U", "Sinead O'Connor")
    assert track.matches("Nothing") == True

'''Given a title and an artist and a search keyword for a full artist, the match returned is True'''
def test_matches_on_full_artist():
    track = Track("Nothing Compares 2 U", "Sinead O'Connor")
    assert track.matches("Sinead O'Connor") == True

'''Given a title and an artist and a search keyword for a partial artist, the match returned is True'''
def test_matches_on_partial_artist():
    track = Track("Nothing Compares 2 U", "Sinead O'Connor")
    assert track.matches("Sinead") == True

'''Given a title and an artist and a search keyword that does not match either, it returns False'''
def test_does_not_match_either_title_or_artist():
    track = Track("Nothing Compares 2 U", "Sinead O'Connor")
    assert track.matches("Blinded By The Lights") == False