import traceback
import sqlite3
import database
import sys


def display_main_menu():
    print('1) Search your library')
    print('2) Add to library')
    print('3) Delete from library')
    print('4) Exit')


def main_menu():
    print('My Music Library')
    while True:
        display_main_menu()
        menu_choice = input('Select an option: ')
        if menu_choice == '1':
            pass

        elif menu_choice == '2':
            add_to_library()

        elif menu_choice == '3':
            pass

        elif menu_choice == '4':
            sys.exit()

        else:
            print('Please select a valid option\n')


def search_library():
    pass


def add_to_library():
    # artist = ''
    # album = ''
    # genre = ''
    # audio_format = ''

    artist = get_artist()
    album = get_album()
    genre = input('Genre: ')
    audio_format = input('Format: ')

    # try:
    #     artist = input('')
    #
    # except Exception:
    #     print('No')


def get_artist():
    return is_empty_field('Artist Name', 'Artist Name: ')


def get_album():
    return is_empty_field('Album Title', 'Album Title: ')


def get_genre():
    pass


def get_format():
    pass


def is_empty_field(name, message):
    field = ''
    while True:
        field = input(message)
        if len(field) == 0:
            print(name + ' cannot be left blank\n')
        else:
            break

    return field


def main():
    # create_music_table()
    database.create_music_table()
    main_menu()

main()
