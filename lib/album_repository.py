from lib.album import Album
# Test-drive an AlbumRepository class
# that has a method all that returns a list of Album objects.

class AlbumRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = [ Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows ]
        return albums

    # Find a single album by its id
    def find(self, album_id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [album_id])
        if rows:
            row = rows[0]
            return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        else:
            raise Exception("No matches found") 
        
    # Test-drive a create method for your AlbumRepository class.
    def create(self, album):
            self._connection.execute('INSERT INTO albums (title, release_year, artist_id)' \
                                        'VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
            rows = self._connection.execute('SELECT * from albums WHERE title = %s', [album.title])
            return rows[0]["id"]


    # Test-drive a delete method for your AlbumRepository class.
    def delete(self, album_id):
        if type(album_id) == int:
            self._connection.execute('DELETE FROM albums WHERE id = %s', [album_id])
        else: 
            raise TypeError("ID should be an integer")
