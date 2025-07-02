# Test-drive a route POST /albums to create a new album
# New album should be present in the list of records returned by GET /albums

""" FEED IN PYTEST FIXTURES """
def test_something(db_connection, web_client):
        pass


def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)"
"""
When I call POST /albums with correct album info
I see it reflected in the list with GET /albums
# """

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post('/albums', data={
        'title': 'Voyage',
        'release_year': '2022',
        'artist_id': '2'}) # Note integers are in string form for requests
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Voyage, 2022, 2)"
    

def test_post_albums_with_no_data_produces_error(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
    "You need to submit title, release_year and artist_id"



    """ 
    Test-drive a route GET /artists, which returns the list of artists:
    # Request: GET /artists
    # Expected response (200 OK):
    Pixies, ABBA, Taylor Swift, Nina Simone
    """

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)"
    
    