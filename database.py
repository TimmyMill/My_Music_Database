import traceback
from sqlite3 import *


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
        search.execute('SELECT * FROM my_music WHERE ' + column + ' LIKE ?', ('%' + keyword + '%',))
        # column_names = get_column_names()
        rows = search.fetchall()
        search_results = [row for row in rows]
        # noinspection PyTypeChecker
        search_results.insert(0, get_column_names())
        return search_results

        # return [column_names, (row for row in rows)]
        # print(column_names[0], column_names[1], column_names[2], column_names[3])
        #
        # for row in rows:
        #     print(row)

    except Error as e:
        print('Error: ', e, 'occurred')
        traceback.print_exc()

    finally:
        db.close()


def get_column_names():
    db = connect('my_music_library.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM my_music')
    column_names = [cn[0].upper() for cn in cur.description]
    db.close()
    return column_names


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


def remove_music(title):
    db = connect('my_music_library.db')
    delete = db.cursor()
    try:
        delete.execute('DELETE FROM my_music WHERE album=?', (title, ))
        db.commit()

    except Error as e:
        print('Error ', e, ' occurred. Your album might not be saved')
        traceback.print_exc()
        db.rollback()

    finally:
        db.close()
