class Song:
    count = 0
    genres =[]
    artists =[]
    genre_count = {}
    artist_count = {}
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genre(genre)
        Song.add_to_artists(artist)
         
    @classmethod
    def add_song_to_count(cls, count = 1):
        cls.count += count
    @classmethod
    def add_to_genre(cls,genre):   
        cls.genres.append(genre)
        Song.add_to_genre_count()
    @classmethod
    def add_to_artists(cls, artist):
         
              cls.artists.append(artist)
              Song.add_to_artist_count()
    @classmethod
    def add_to_genre_count(cls):
        genre_count = {}
        for genre in cls.genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        cls.genre_count = genre_count
    @classmethod
    def add_to_artist_count(cls):
        artist_count = {}
        for artist in cls.artists:
            artist_count[artist] = artist_count.get(artist, 0) + 1
        cls.artist_count = artist_count    