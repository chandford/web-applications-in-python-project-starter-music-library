
# /albums Route Design Recipe

## 1. Design the Route Signatures
```
POST /albums
    title: string (body parameter)
    release_year: int (body parameter)  
    artist_id: int (body parameter)
Expected response: 200 OK
Returns: No content


GET /albums 
Expected response: 200 OK
Returns: list of records (albums)
```

## 2. Create Examples as Tests

```python
# GET /albums
#  Expected response (200 OK):
"""
Album(1, Doolittle, 1989, 1 )
Album(2, Surfer Rosa, 1988, 1 )
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, Lover, 2019, 3)
Album(7, Folklore, 2020, 3)
Album(8, I Put a Spell on You, 1965, 4)
Album(9, Baltimore, 1978, 4)
Album(10, Here Comes the Sun, 1971, 4)
Album(11, Fodder on My Wings, 1982, 4)
Album(12, Ring Ring, 1973, 2)
"""

# POST /albums
# Body parameters:
#     title=Voyage
#     release_year=2022
#     artist_id=2
#  Expected response: 200 OK
"""
(No content)

Then... GET /albums should return... 

Album(1, Doolittle, 1989, 1 )
Album(2, Surfer Rosa, 1988, 1 )
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, Lover, 2019, 3)
Album(7, Folklore, 2020, 3)
Album(8, I Put a Spell on You, 1965, 4)
Album(9, Baltimore, 1978, 4)
Album(10, Here Comes the Sun, 1971, 4)
Album(11, Fodder on My Wings, 1982, 4)
Album(12, Ring Ring, 1973, 2)
Album(13, Voyage, 2022, 2) => New record
"""

# POST /albums
# (Missing body parameters)
# Expected response (400 Bad Request):
"""
Exception raised: "New albums must have a title, release_year, and artist_id"
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /albums
Expected response (200 OK):
  Album objects 
"""
# def test_get_albums(web_client):
#     response = web_client.get('/albums')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == all albums 

"""
POST /albums
  Parameters (in body):
      title: Voyage
      release_year: 2022
      artist_id: 2
Expected response (200 OK)
"""
def test_post_album(web_client):
    response = web_client.post('/submit', data={
      'title': 'Voyage',
      'release_year': 2022,
      'artist_id': 2
      })
    assert response.status_code == 200
    # Additional assert ? - after running GET
