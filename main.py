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


def display_search_menu():
    print('\tSearch by ')
    print('\t---------')
    option_number = 0
    # iterate search options list to display a formatted menu
    for option in search_options:
        option_number += 1
        print('\t' + str(option_number) + ') ' + option)


# used by the search method to determine what the user wants to search by (artist, album, genre, format)
# calls the method using the given "search type", gets user input, and returns a keyword to pass to the database
def get_search_keyword(search_type, keyword):
    if search_type == 'Artist':
        keyword = get_artist().upper()
    if search_type == 'Album':
        keyword = get_album().upper()
    if search_type == 'Genre':
        keyword = get_genre()
    if search_type == 'Format':
        keyword = get_format()

    return keyword


def search_library():
    print('Search Menu\n')
    search_option = ''
    keyword = ''
    while True:
        display_search_menu()
        try:
            search_choice = int(input('>'))
            search_options_length = len(search_options)  # number of elements in the search options list

            # determines what to search the database by, then uses the method to get user input and return a keyword
            if search_choice in range(1, search_options_length + 1):
                search_option = search_options[search_choice - 1]
                keyword = get_search_keyword(search_option, keyword)
                break

            else:
                print('Select an option 1-' + str(search_options_length) + '\n')

        except ValueError:
            print('Enter your choice as a number\n')

    # Use search method from database class, passing in the column to search and the keyword to search for
    display_search_results(database.search_music(search_option, keyword))


def display_search_results(results):
    column_max_size = get_columns_max_size(results)
    for result in results:
        artist = result[0]
        album = result[1]
        genre = result[2]
        album_format = result[3]
        format_results(column_max_size, artist, album, genre, album_format)


def get_columns_max_size(results):
    artist_length = 0
    album_length = 0
    genre_length = 0
    format_length = 0

    for result in results:
        artist_length = len(result[0]) + 1 if len(result[0]) > artist_length else artist_length + 1
        album_length = len(result[1]) + 1 if len(result[1]) > album_length else album_length + 1
        genre_length = len(result[2]) + 1 if len(result[2]) > genre_length else genre_length + 1
        format_length = len(result[3]) + 1 if len(result[3]) > format_length else format_length + 1

    return [artist_length, album_length, genre_length, format_length]


def format_results(column_max_size, artist, album, genre, album_format):
    if len(artist) < column_max_size[0]:
        artist += " " * (column_max_size[0] - len(artist))

    if len(album) < column_max_size[1]:
        album += " " * (column_max_size[1] - len(album))

    if len(genre) < column_max_size[2]:
        genre += " " * (column_max_size[2] - len(genre))

    if len(album_format) < column_max_size[3]:
        album_format += " " * (column_max_size[3] - len(album_format))

    print(artist + album + genre + album_format)


def add_to_library():
    artist = get_artist().upper()
    title = get_album().upper()
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
    database.create_music_table()
    main_menu()


main()
