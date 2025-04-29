from tinytag import TinyTag as td

class MetaData(object):
    """Song metadata"""
    def __init__(self):
        # Song Metadata
        self.title = ""
        self.artist = ""
        self.album = ""
        self.genre = ""
        self.year = ""
        self.bit_rate = ""
        self.composer = ""
        self.file_size = ""
        self.album_artist = ""
        self.duration = ""
        self.track_total = ""
        self.cover = "./assets/t_dog_logo.png"
    
    def get_meta(self, directory_now, file_load):
        """Retrieve Metadata from Song Currently Playing."""
        if not isinstance(directory_now, str):
            raise ValueError("Directory and File to be loaded must be string type.")
        audio = td.get(directory_now + "/" + file_load)
        self.title = audio.title
        self.artist = audio.artist
        self.genre = audio.genre
        self.year = audio.year
        self.bit_rate = str(audio.bitrate)
        self.composer = audio.composer
        self.file_size = audio.filesize
        self.album_artist = audio.albumartist
        self.duration = str(audio.duration)
        self.track_total = str(audio.track_total)
        self.album = audio.album
        for pic in glob.glob(f"{directory_now}/*jpg"):
            self.cover = pic