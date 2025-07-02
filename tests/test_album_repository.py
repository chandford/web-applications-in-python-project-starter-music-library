from lib.album_repository import AlbumRepository
from lib.album import Album
import pytest


"""
When we call AlbumRepository.all
We get a list of Album objects reflecting the seed data
"""

def test_get_all_records(db_connection): # DatabaseConnection object as Pytest fixture
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository instance

    albums = repository.all() # Get all albums

    # Assert on the results
    assert type(albums) == list
    assert len(albums) == 12
    assert albums[0] == Album(1, 'Doolittle', 1989, 1)
    assert albums[5] == Album(6, 'Lover', 2019, 3)
    assert albums[-1] == Album(12, 'Ring Ring', 1973, 2)

def test_find_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    expected_album = Album(1, "Doolittle", 1989, 1)
    assert album == expected_album

def test_find_raises_exception_when_no_match_found(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.find(70)
    error_message = str(err.value)
    assert error_message == "No matches found"



def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(13, "Test Title", 2025, 201))
    result = repository.all()
    assert str(result[-1]) == "Album(13, Test Title, 2025, 201)"

def test_create_record_throws_exception(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    with pytest.raises(TypeError) as err: 
        repository.create([13, "Test Title", 2025, 201])
    error_message = str(err.value)
    assert error_message == "Requires an Album object"

def test_create_record_returns_new_record_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.create(Album(13, "Test Title", 2025, 201)) == 13
    assert repository.create(Album(14, "Second Test Title", 2025, 105)) == 14

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert str(result[0]) == "Album(2, Surfer Rosa, 1988, 1)"

def test_delete_record_rasies_exception_when__match_found(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    with pytest.raises(TypeError) as err: 
        repository.delete("one")
    error_message = str(err.value)
    assert error_message == "ID should be an integer"