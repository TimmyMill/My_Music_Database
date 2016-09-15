import database
import sys
from album import *

genres = ('Alternative', 'Blues', 'Classical', 'Country', 'Dance', 'Electronic', 'Hip-Hop/Rap', 'Jazz', 'Pop',
          'R&B/Soul', 'Reggae', 'Rock')
formats = ('8-Track', 'Cassette', 'CD', 'Digital', 'Vinyl')


def create_album(artist, title, genre, audio_format):
    return Album(artist, title, genre, audio_format)


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
    artist = get_artist()
    title = get_album()
    genre = get_genre()
    audio_format = get_format()
    database.add_music(create_album(artist, title, genre, audio_format))


def get_artist():
    return is_empty_field('Artist Name', 'Artist Name: ')


def get_album():
    return is_empty_field('Album Title', 'Album Title: ')


def display_genres():
    option_number = 0
    # iterate list of genres to print out a list of options for the user to choose from
    for genre in genres:
        option_number += 1
        # if the option_number is < 10, use the second print statement to add a space in front of the number
        # otherwise, use the first print statement
        (lambda: print(str(option_number) + ') ' + genre), lambda: print(' ' + str(option_number) + ') ' + genre))[
            option_number < 10]()


def get_genre():
    genre = ''
    while True:
        display_genres()
        try:
            genre_choice = int(input('Genre: '))
            genre_list_length = len(genres)
            if genre_choice in range(1, genre_list_length + 1):
                genre = genres[genre_choice - 1]  # gets the element from the list using the elements index number
                break
            else:
                print('Select an option 1-' + str(genre_list_length))

        except ValueError:
            print('Select a number')

    return genre


def display_formats():
    option_number = 0
    for audio_format in formats:
        option_number += 1
        print(str(option_number) + ') ' + audio_format)


def get_format():
    audio_format = ''
    while True:
        display_formats()
        try:
            format_choice = int(input('Format: '))
            formats_list_length = len(formats)
            if format_choice in range(1, formats_list_length + 1):
                audio_format = formats[format_choice - 1]
                break
            else:
                print('Select an option 1-' + str(formats_list_length))

        except ValueError:
            print('Select a number')

    return audio_format


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
