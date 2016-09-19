import traceback
from _sqlite3 import *


def create_music_table():
    db = connect('my_music_library.db')
    # print('DB opened')

    db.execute(('''
CREATE TABLE IF NOT EXISTS my_music(
artist TEXT NOT NULL,
album TEXT UNIQUE NOT NULL,
genre TEXT NOT NULL,
format TEXT NOT NULL );'''))
    db.close()
    # print('DB closed')


def search_music(column, keyword):
    db = connect('my_music_library.db')
    search = db.cursor()
    try:
        search.execute('SELECT * FROM my_music WHERE' + column + 'LIKE' + keyword)
        # search.execute('SELECT * FROM my_music WHERE' + column + 'LIKE', ('%' + keyword + '%', ))
        for albums in search.fetchall():
            print(albums)

    except Error as e:
        print('Error: ', e, 'occurred')
        traceback.print_exc()

    finally:
        db.close()


def add_music(album):
    db = connect('my_music_library.db')
    add = db.cursor()
    try:
        add.execute('INSERT INTO my_music VALUES (?,?,?,?)',
                    (album.artist, album.title, album.genre, album.audio_format))
        db.commit()

    except IntegrityError:
        print('This album already exists in your music library')
        db.rollback()

    except Error as e:
        print('Error ', e, ' occurred. Your album might not be saved')
        traceback.print_exc()
        db.rollback()

    finally:
        db.close()

