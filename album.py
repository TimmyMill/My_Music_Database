

class Album:

    def __init__(self, artist, title, genre, audio_format):
        self.artist = artist
        self.title = title
        self.genre = genre
        self.audio_format = audio_format

    def __repr__(self):
        self.str_repr = self.artist + '\t' + self.title + '\t' + self.genre + '\t' + self.audio_format
        return self.str_repr
