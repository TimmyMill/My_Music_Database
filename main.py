import database
import sys
from album import *

# lists containing data to use for print statements and user selection choices
genres = ('Alternative', 'Blues', 'Classical', 'Country', 'Dance', 'Electronic', 'Hip-Hop/Rap', 'Jazz', 'Pop',
          'R&B/Soul', 'Reggae', 'Rock')
formats = ('8-Track', 'Cassette', 'CD', 'Digital', 'Vinyl')
search_options = ('Artist', 'Album', 'Genre', 'Format')


def create_album(artist, title, genre, audio_format):
    return Album(artist, title, genre, audio_format)


def display_main_menu():
    print('Main Menu')
    print('\t1) Search your library')
    print('\t2) Add to library')
    print('\t3) Delete from library')
    print('\t4) Exit')


def main_menu():
    print('My Music Library')
    # print('\tSelect an option: ')
    while True:
        display_main_menu()
        # menu_choice = input('Select an option: ')
        menu_choice = input('>')
        if menu_choice == '1':
            search_library()

        elif menu_choice == '2':
            add_to_library()

        elif menu_choice == '3':
            pass

        elif menu_choice == '4':
            sys.exit()

        else:
            print('Please select a valid option\n')


def search_menu():
    print('\tSearch by ')
    print('\t---------')
    option_number = 0
    for option in search_options:
        option_number += 1
        print('\t' + str(option_number) + ') ' + option)


def search_library():
    print('Search Menu\n')
    search_option = ''
    while True:
        search_menu()
        try:
            search_choice = int(input('>'))
            search_options_length = len(search_options)
            if search_choice in range(1, search_options_length + 1):
                search_option = search_options[search_choice - 1]
                break

            else:
                print('Select an option 1-' + str(search_options_length) + '\n')

        except ValueError:
            print('Enter your choice as a number\n')

    database.search_music(search_option)


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
                print('Select an option 1-' + str(genre_list_length) + '\n')

        except ValueError:
            print('Enter your choice as a number\n')

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
