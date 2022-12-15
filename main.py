import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from tinytag import TinyTag as td
import os
from os.path import exists
import pygame
import time
import csv
from PIL import Image

# Initialize sound module
class Triad:
    def __init__(self, is_playing=False):
        """Launch mixer in background to allow for sound to play.
        Load last played playlist or last file folder location."""

        # Initialize pygame mixer module to enable sound
        pygame.mixer.init()

        # Default attributes
        self.is_playing = is_playing
        self.pause_label = "Pause"
        self.current_song = 0
        self.current_path_dir = ""
        self.next = ""
        self.now_song = ""
        self.start = 0
        self.stop = 0
        self.field_names = ["PL_Name", "Path", "File_Name", "Title", "Artist", "Album", "Track_Length"]
        self.closing_list = []
        self.new_playlist = []
        self.now_playing_list = []
        self.last_played = []
        self.track_index = len(self.now_playing_list)
        self.current_path_dir_list = []

        # Song metadata
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

        # Tk Window for application
        root = Tk()
        root.title("Triad")
        root.geometry("600x400")
        root.columnconfigure(0, weight=1)
        root.resizable(0, 0)
        
        # Create menu bar
        menuubar = Menu(root)
        root.config(menu=menuubar)

        # File Menu Drop Down
        file_menu = Menu(menuubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_it)
        file_menu.add_command(label="Open Playlist", command=self.open_playlist)
        file_menu.add_command(label="Create New Playlist", command=self.create_playlist)
        file_menu.add_command(label="Add to Existing Playlist", command=self.add_to_playlist)
        file_menu.add_command(label="Remove track(s) from an Existing Playlist", command=self.delete_from_playlist)
        file_menu.add_command(label="Exit", command=root.destroy)
        
        # Help Menu Drop Down
        help_menu = Menu(menuubar, tearoff=0)
        menuubar.add_cascade(label="File", menu=file_menu)
        menuubar.add_cascade(label="About", menu=help_menu)
        help_menu.add_command(
            label="TRIAD",
            command=lambda: showinfo(
                title="TRIAD",
                message="Triad is a wicked awesome audio player built by pc84! Enjoy!",
            ),
        )
        help_menu.add_command(
            label="Help",
            command=lambda: showinfo(
                title="Help",
                message="Visit this projects Github:\ngithub.com/sageandpine/triad-audio-player",
            ),
        )

        # Tk Frame that fits inside window
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=5, sticky=(N, W, E, S))

        # Buttons for Basic Functions
        self.pause_l = tk.Variable(value=self.pause_label)
        self.play_button = ttk.Button(
            mainframe, text="Play", command=self.play_it
        ).grid(column=0, row=1)
        self.pause_button = ttk.Button(
            mainframe, textvariable=self.pause_l, command=self.pause_it
        ).grid(column=0, row=2)
        self.rewind_button = ttk.Button(
            mainframe, text="RWD", command=self.rwd_it
        ).grid(column=0, row=3)
        self.forward_button = ttk.Button(
            mainframe, text="FWD", command=self.fwd_it
        ).grid(column=0, row=4)
        
        # Playlist Variables to update Label
        self.var = tk.Variable(value=self.now_playing_list)
        self.now_var = tk.Variable(value=self.now_song)

        # Now Playing Label
        self.now_playing = ttk.Label(mainframe, text="Now Playing: ").grid(
            column=1, row=6, sticky=W
        )
        self.now_playing = ttk.Label(
            mainframe,
            textvariable=self.now_var,
            relief=RIDGE,
            foreground="green",
        ).grid(column=2, row=6, sticky=EW)

        # Frame that shows logo or album art
        self.photo = tk.PhotoImage(file="./t_dog_logo.png")
        imageframe = ttk.Frame(root, padding="3 3 12 12")
        imageframe.grid(column=2, row=4, sticky=W)
        self.imageframe = ttk.Label(imageframe, image=self.photo, padding=2)
        self.imageframe.grid(column=0, row=2)

        # Frame that lists contents of chosen directory
        fileframe = ttk.Frame(root, padding="3 3 12 12")
        fileframe.grid(columnspan=1, row=4, sticky=W)
        self.file_window = tk.Listbox(
            fileframe,
            listvariable=self.var,
            height=10,
            width=45,
            bg="#9F73AB",
            selectmode=tk.BROWSE,
        )
        self.file_window.bind("<<ListboxSelect>>", self.selected_item)
        self.file_window.grid(column=2, row=0)

        # Retrieve last played playlist and load upon opening program
        self.fetch_closing_list()

        # Main Loop Launches the GUI and keeps it running until the program terminates
        root.mainloop()

    def load_it(self, file):
        """Load file for playback"""
        if not isinstance(file, str):
            raise ValueError("File loaded must be string")
        if ".mp3" in file:
            pygame.mixer.music.load(file)
        else:
            raise Exception("File Type not supported")

    def change_label(self, new):
        """Change text label to reflect song playing."""
        if not isinstance(new, str):
            raise ValueError("To change label, must use string data type.")
        self.now_var.set(new)

    def queue_next(self):
        """Queues next track for playback. If user is at end of playlist, loads 1st track to start over."""
        if (self.current_song + 1) < len(self.now_playing_list):
            pygame.mixer.music.queue(
                self.current_path_dir_list[(self.current_song + 1)]
                + "/"
                + self.now_playing_list[(self.current_song + 1)]
            )
        else:
            pygame.mixer.music.queue(
                self.current_path_dir_list[0] + "/" + self.now_playing_list[0]
            )

    def play_it(self):
        """Play file loaded for playback."""
        pygame.mixer.music.play()
        self.get_meta(
            self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song]
        )
        self.is_playing = True
        self.queue_next()

    def pause_it(self):
        """Pause File currently playing. Press again to resume."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.pause_l.set("Resume")
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.pause_l.set("Pause")

    def fwd_it(self):
        """FWD should load a new track and play it. When we come to the end of the playlist
        automatically re-starts at track 1."""
        if (self.current_song + 1) < len(self.now_playing_list):
            self.current_song = self.current_song + 1
            self.load_it(
                self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song]
            )
            self.play_it()
            self.now_song = self.now_playing_list[self.current_song]
            self.change_label(self.now_song)
            # self.change_label("#" + (str(self.current_song + 1)) + " Artist: " + self.artist + " Song: " + self.title + " ")

        else:
            self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
            self.current_song = 0
            self.play_it()
            self.now_song = self.now_playing_list[self.current_song]
            self.change_label(self.now_song)

    def rwd_it(self):
        """Go back to the begining of currently loaded song.
        If RWD button pressed less than 4 seconds after start of track,
        skips back to previous track."""
        self.stop = time.time()
        count = self.stop - self.start
        if count < 4.0:
            if (self.current_song - 1) > 0:
                self.current_song = self.current_song - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song]
                    + "/"
                    + self.now_playing_list[self.current_song]
                )
                self.play_it()
                self.now_song = self.now_playing_list[self.current_song]
                self.change_label(self.now_song)
            elif (self.current_song - 1) == 0:
                self.current_song = self.current_song - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song]
                    + "/"
                    + self.now_playing_list[self.current_song]
                )
                self.play_it()
                self.now_song = self.now_playing_list[self.current_song]
                self.change_label(self.now_song)
            elif (self.current_song) == 1:
                self.current_song = self.current_song - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song]
                    + "/"
                    + self.now_playing_list[self.current_song]
                )
                self.play_it()
                self.now_song = self.now_playing_list[self.current_song]
                self.change_label(self.now_song)
            else:
                pygame.mixer.music.rewind()
                self.change_label(self.now_song)
        else:
            pygame.mixer.music.rewind()
            self.start = time.time()

    def open_it(self):
        """Launch dialog box to choose files to pick music from. Opens files chosen and starts to play."""
        self.playlist_name = "Now Playing"
        self.now_playing_list.clear()
        self.current_path_dir_list.clear()
        file_list = list(fd.askopenfilenames())
        # heads_tails contains list of tuples where heads = dir & tails = file name
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        for (directory_1, name_1) in heads_tails:
            self.current_path_dir_list.append(directory_1)
            self.now_playing_list.append(name_1) 
        self.now_playing_list.sort()
        songs = self.now_playing_list
        self.update_now_playing(songs)
        self.load_it(
            self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song]
        )
        self.get_meta(
            self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song]
        )
        self.save_closing_list()
        self.play_it()
        self.now_song = self.now_playing_list[self.current_song]
        self.change_label(self.now_song)

    def update_now_playing(self, songs):
        """Updates the file_window widget."""
        if not isinstance(songs, list):
            raise ValueError("Songs loaded must be list type.")
        self.file_window.delete(0, END)
        for file in songs:
            self.file_window.insert(END, file)

    def selected_item(self, event):
        """Select/play file from file_window widget with cursor."""
        index = self.file_window.curselection()
        self.current_song = int(index[0])
        self.load_it(self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song])
        self.get_meta(
            self.current_path_dir_list[self.current_song] + "/" + self.now_playing_list[self.current_song]
        )
        self.play_it()
        self.now_song = self.now_playing_list[self.current_song]
        self.change_label(self.now_song)

    def get_meta(self, file):
        """Retrieve metadata from song playing."""
        audio = td.get(file)
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

    def save_closing_list(self):
        """Saves the now playing list when closing program. If first time playing,
        creates CLOSING FILE to be recalled and loaded next time program is loaded.
        Otherwise it recalls CLOSING FILE in memory"""
        for i in range(len(self.now_playing_list)):
            self.closing_list.append(dict(PL_Name = "Closing_List", Path = self.current_path_dir_list[i] + "/", File_Name = self.now_playing_list[i], Title = self.title, Artist = self.artist, Album = self.album, Track_Length = self.duration))
        with open('closing_list.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            writer.writeheader()
            writer.writerows(self.closing_list)
        self.closing_list.clear()

    def fetch_closing_list(self):
        """Fetch closing_list.csv file to populate now_playing_list on program launch. If first time opening program,
        function is skipped."""
        if exists("closing_list.csv"):
            with open("closing_list.csv", "r") as openfile:
                csv_file = csv.DictReader(openfile)
                for lines in csv_file:
                    self.current_path_dir_list.append(lines["Path"])
                    self.now_playing_list.append(lines["File_Name"])
                self.update_now_playing(self.now_playing_list)
                self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
                self.get_meta(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
        else:
            pass

    def open_playlist(self):
        """open playlist to populate now_playing_list."""
        file_2 = fd.askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
        csv_file = csv.DictReader(file_2)
        self.now_playing_list.clear()
        self.current_path_dir_list.clear()
        for lines in csv_file:
            self.current_path_dir_list.append(lines["Path"])
            self.now_playing_list.append(lines["File_Name"])
        self.update_now_playing(self.now_playing_list)
        self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
        self.get_meta(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
        self.now_song = self.now_playing_list[0]
        self.change_label(self.now_song)
        self.save_closing_list()

    def create_playlist(self):
        """Create a new playlist to recall later."""
        user_input = simpledialog.askstring(title="Playlist Name", prompt="Name this playlist: ")
        file_list = list(fd.askopenfilenames())
        heads_tails = [] 
        for items in file_list:
            heads_tails.append(os.path.split(items))
        if exists(f"{user_input}.csv"):
            self.open_playlist
        else:
            for (directory_1, name_1) in heads_tails:
                self.get_meta(directory_1 + "/" + name_1)
                self.new_playlist.append(dict(PL_Name = f"{user_input}", Path = directory_1, File_Name = name_1, Title = self.title, Artist = self.artist, Album = self.album, Track_Length = self.duration))
        with open(f"{user_input}.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            writer.writeheader()
            writer.writerows(self.new_playlist)
        self.new_playlist.clear()

    def delete_from_playlist(self):
        """Remove song(s) from existing playlist"""
        # Open PLaylist to Edit
        file_2 = fd.askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
        y = file_2.readlines()
        pl_name = y[1].split(",")[0]
        # Ask to edit
        simpledialog.askstring(title= pl_name, prompt="Edit this playlist?")
        file_list = list(fd.askopenfilenames())
        heads_tails = []
        # split files to be removed into tuples
        for items in file_list:
            heads_tails.append(os.path.split(items))
        # find heads/tails in csv and remove them    
        for (directory_1, name_1) in heads_tails:
            with open((pl_name + ".csv"), "a") as file:
                self.get_meta(directory_1 + "/" + name_1)
                self.new_playlist.remove(dict(PL_Name = pl_name, Path = directory_1, File_Name = name_1, Title = self.title, Artist = self.artist, Album = self.album, Track_Length = self.duration))
                # self.now_playing_list.append(name_1)
                writer = csv.DictWriter(file, fieldnames=self.field_names)
                writer.writerows(self.new_playlist)
            self.new_playlist.clear()


    def add_to_playlist(self):
        """Add songs to an existing saved playlist"""
        file_2 = fd.askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
        y = file_2.readlines()
        pl_name = y[1].split(",")[0]
        simpledialog.askstring(title= pl_name, prompt="Add to this list?")
        file_list = list(fd.askopenfilenames())
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        for (directory_1, name_1) in heads_tails:
            with open((pl_name + ".csv"), "a") as file:
                self.get_meta(directory_1 + "/" + name_1)
                self.new_playlist.append(dict(PL_Name = pl_name, Path = directory_1, File_Name = name_1, Title = self.title, Artist = self.artist, Album = self.album, Track_Length = self.duration))
                self.now_playing_list.append(name_1)
                writer = csv.DictWriter(file, fieldnames=self.field_names)
                writer.writerows(self.new_playlist)
            self.new_playlist.clear()




# Comment out for testing
T = Triad()

