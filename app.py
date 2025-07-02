import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository

app = Flask(__name__) # Create a Flask application instance for managing the entire lifecycle of an HTTP request

# == New Routes Here ==

@app.route('/albums', methods=['POST'])
def post_album():
    if 'title' not in request.form \
            or 'release_year' not in request.form \
            or 'artist_id' not in request.form:
        return "You need to submit title, release_year and artist_id", 400 # tuple (response_body, status_code) 
    
    else:
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        album = Album(
            None,
            request.form['title'],
            request.form['release_year'],
            request.form['artist_id']
        )
        print(f"Creating album: {album}")
        repository.create(album)
        return "", 200 # tuple (response_body, status_code) 
    

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join(f"{album}" for album in albums)



@app.route('/artists', methods=['GET'])
def get_artists():
    connection =  get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return "\n".join(f"{artist}" for artist in artists)





if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

