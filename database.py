import _sqlite3


def create_music_table():
    db = _sqlite3.connect('my_music_library.db')
    print('DB opened')

    db.execute(('''
CREATE TABLE IF NOT EXISTS my_music(
artist TEXT UNIQUE NOT NULL,
album TEXT NOT NULL,
genre TEXT NOT NULL,
format TEXT NOT NULL);'''))
    db.close()
    print('DB closed')


def search_music():
    pass


def add_music():
    pass
