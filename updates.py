class Updates(object):
    def __init__():
        pass

    def update_now_playing(self, songs):
        """Updates the File Window Widget."""
        if not isinstance(songs, list):
            raise ValueError("Songs loaded must be list type.")
        self.file_window.delete(0, END)
        for file in songs:
            self.file_window.insert(END, file)
            
    def change_song_label(self, new):
        """Change Text Label to Reflect Song Currently Playing."""
        if not isinstance(new, str):
            raise ValueError("To change label, must use string data type.")
        self.song_var.set(new)

    def change_pl_label(self, new):
        """Change Text Label to Reflect Current Playlist Title."""
        if not isinstance(new, str):
            raise ValueError("To change label, must use string data type.")
        self.pl_title_var.set(new)

    def update_album_cover(self, cover):
        """Change Album Cover Image to Match Current Songs Album."""
        if not isinstance(cover, str):
            raise ValueError("To change label, must use string data type.")
        photo_raw = Image.open(cover)
        photo_resized = photo_raw.resize((200, 200))
        cover_new = ImageTk.PhotoImage(photo_resized)
        self.imageframe.configure(image=cover_new)
        self.imageframe.image = cover_new