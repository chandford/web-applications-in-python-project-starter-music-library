from lib.album import Album
"""
Album constructs with an attribute for each column in the albums table:
title, release_year, artist_id
"""

def test_album_constructs_with_correct_attributes():
    album = Album(1, 'Doolittle', 1989, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1


"""
We can format albums to strings nicely
"""

def test_album_repr_method_format():
    album = Album(1, 'Doolittle', 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"


"""
We can compare two identical albums
And have them be equal
"""

def test_album_eq_method_for_identical_albums():
    album_1 = Album(1, 'Doolittle', 1989, 1)
    album_2 = Album(1, 'Doolittle', 1989, 1)
    assert album_1 == album_2