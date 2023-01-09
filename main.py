import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from tinytag import TinyTag as td
from PIL import Image, ImageTk
import os
import glob
from os.path import exists
import pygame
import time
import csv
import random
import pandas as pd

# Initialize sound module
class Triad:
    def __init__(self, is_playing=False):
        """Launch mixer in background to allow for sound to play.
        Load last played playlist on start."""

        # Initialize Pygame Mixer Module to Enable Playback
        pygame.mixer.init()

        # Default Attributes
        self.is_playing = is_playing
        self.pause_label = "PAUSE"
        self.loop_label = "LOOP ALL"
        self.current_song_index = 0
        self.current_path_dir = ""
        self.next = ""
        self.now_playing_song = "3...TRIAD...3"
        self.now_playing_list_name = "Playlist: Now Playing"
        self.start = 0
        self.stop = 0
        self.fileyouwant = ""
        self.field_names = [
            "PL_Name",
            "Path",
            "File_Name",
            "Title",
            "Artist",
            "Album",
            "Track_Length",
            "Album_Cover",
        ]
        self.closing_list = []
        self.new_playlist = []
        self.now_playing_list = []
        self.editing_list = []
        self.current_path_dir_list = []

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

        # Root GUI Window
        root = Tk()
        root.title("TRIAD Audio Player")
        root.geometry("800x290")
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=1)

        # Create Menu Bar Widget
        menubar = Menu(root)
        root.config(menu=menubar)

        # File Menu Drop Down
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Files", command=self.open_it)
        file_menu.add_command(label="Open Playlist", command=self.open_playlist)
        file_menu.add_command(
            label="Create/Edit Playlists", command=self.launch_pl_editor
        )
        file_menu.add_command(label="Exit", command=root.destroy)

        # Help Menu Drop Down
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="About", menu=help_menu)
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

        # Playlist Variables to Update Labels/Images/Button Widgets
        self.list_var = tk.Variable(value=self.now_playing_list)
        self.song_var = tk.Variable(value=self.now_playing_song)
        self.pl_title_var = tk.Variable(value=self.now_playing_list_name)
        self.pause_l = tk.Variable(value=self.pause_label)
        self.looper_l = tk.Variable(value=self.loop_label)

        # Window Frame & Config
        window_frame = ttk.Frame(root, padding=5)
        window_frame.columnconfigure(0, weight=1)
        window_frame.grid(column=0, row=0, sticky=W)

        # Put File List Window Widget in Frame
        self.file_window = tk.Listbox(
            window_frame,
            listvariable=self.list_var,
            height=11,
            width=72,
            bg="#9F73AB",
            selectmode=tk.BROWSE,
        )
        self.file_window.grid(column=0, row=0)
        self.file_window.bind("<<ListboxSelect>>", self.play_selected_item)

        # Button Frame
        button_frame = ttk.Frame(root, padding=5)
        button_frame.columnconfigure(0, weight=1)
        button_frame.grid(column=0, row=1, sticky=W)

        # Add Buttons to Frame
        self.play_button = ttk.Button(
            button_frame, text="PLAY", command=self.play_it
        ).grid(column=0, row=1)

        self.rwd_button = ttk.Button(
            button_frame, text="REWIND", command=self.rwd_it
        ).grid(column=1, row=1)

        self.fwd_button = ttk.Button(
            button_frame, text="FORWARD", command=self.fwd_it
        ).grid(column=2, row=1)

        self.pause_button = ttk.Button(
            button_frame, textvariable=self.pause_l, command=self.pause_it
        ).grid(column=0, row=2)

        self.shuffle_button = ttk.Button(
            button_frame, text="SHUFFLE", command=self.shuffle
        ).grid(column=1, row=2)

        self.loop_button = ttk.Button(
            button_frame, textvariable=self.looper_l, command=self.loop
        ).grid(column=2, row=2)

        # Default Image == Logo/ Replaced by Album Art
        photo = ImageTk.PhotoImage(Image.open("./assets/t_dog_logo.png"))

        # Album Frame to Display Image
        imageframe = ttk.Frame(root, height=200, width=200, padding=5)
        imageframe.columnconfigure(0, weight=2)
        imageframe.grid(column=2, row=0)

        # Album Cover Image
        self.imageframe = Label(imageframe, image=photo)
        self.imageframe.grid(column=0, row=0)

        # Playlist Name Label Widget Frame
        pl_labelframe = ttk.Frame(root, height=100, width=200, padding=5)
        pl_labelframe.columnconfigure(0, weight=2)
        pl_labelframe.grid(column=2, row=1)

        # Attach Playlist Name Label Widget to Frame
        self.now_playing_list_title = ttk.Label(
            pl_labelframe, textvariable=self.pl_title_var, relief=SUNKEN, width=25
        ).grid(column=0, row=1)

        # Make a Frame for Now Playing Ticker Label Widget
        label_frame = ttk.Frame(root, padding=5)
        label_frame.columnconfigure(0, weight=1)
        label_frame.grid(column=2, row=1, sticky=W)

        # Now Playing Ticker Label Widget
        self.now_playing = ttk.Label(button_frame, text="Now Playing: ", width=29).grid(
            column=3, row=1, padx=5, pady=0, sticky=W
        )
        self.now_playing = ttk.Label(
            button_frame,
            textvariable=self.song_var,
            relief=SUNKEN,
            foreground="green",
            width=40,
        ).grid(column=3, row=2, sticky=W, padx=5, pady=0)

        # Fetch Last Played Playlist & Load on Startup
        self.fetch_closing_list()

        # Sets Default Loop Value to Loop All
        self.loop_one = False

        # Run Main Loop
        root.mainloop()

    def load_it(self, file):
        """Load File for Playback."""
        if not isinstance(file, str):
            raise ValueError("File loaded must be string")
        if ".mp3" in file:
            pygame.mixer.music.load(file)
        else:
            raise Exception("File Type not supported")

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

    def queue_next(self):
        """Queues Next Track for Playback. Default Behavior is to Loop All."""
        if self.loop_one == True:
            pygame.mixer.music.queue(
                self.current_path_dir_list[(self.current_song_index - 1)]
                + "/"
                + self.now_playing_list[(self.current_song_index - 1)]
            )
        else:
            if (self.current_song_index + 1) < len(self.now_playing_list):
                pygame.mixer.music.queue(
                    self.current_path_dir_list[(self.current_song_index + 1)]
                    + "/"
                    + self.now_playing_list[(self.current_song_index + 1)]
                )
            else:
                pygame.mixer.music.queue(
                    self.current_path_dir_list[0] + "/" + self.now_playing_list[0]
                )

    def play_it(self):
        """Play File Loaded for Playback."""
        pygame.mixer.music.play()
        self.get_meta(
            self.current_path_dir_list[self.current_song_index],
            self.now_playing_list[self.current_song_index],
        )
        self.is_playing = True
        self.update_album_cover(self.cover)
        self.queue_next()

    def pause_it(self):
        """Pause File Currently Playing. Press Again to Resume."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.pause_l.set("Resume")
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.pause_l.set("Pause")

    def fwd_it(self):
        """FWD Loads Next Track in Que and Plays It."""
        if self.loop_one == True:
            self.current_song_index = self.current_song_index
            self.load_it(
                self.current_path_dir_list[self.current_song_index]
                + "/"
                + self.now_playing_list[self.current_song_index]
            )
            self.play_it()
            self.now_playing_song = self.now_playing_list[self.current_song_index]
            self.change_song_label(self.now_playing_song)
            self.update_album_cover(self.cover)

        elif (self.current_song_index + 1) < len(self.now_playing_list):
            self.current_song_index = self.current_song_index + 1
            self.load_it(
                self.current_path_dir_list[self.current_song_index]
                + "/"
                + self.now_playing_list[self.current_song_index]
            )
            self.play_it()
            self.now_playing_song = self.now_playing_list[self.current_song_index]
            self.change_song_label(self.now_playing_song)
            self.update_album_cover(self.cover)

        else:
            self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
            self.current_song_index = 0
            self.play_it()
            self.now_playing_song = self.now_playing_list[self.current_song_index]
            self.change_song_label(self.now_playing_song)
            self.update_album_cover(self.cover)

    def rwd_it(self):
        """Return to the Beginning of Currently Loaded Song.
        If RWD Button Pressed < 4 Seconds After Start of Track,
        Skips Back to Previous Track in Que."""
        self.stop = time.time()
        count = self.stop - self.start
        if self.loop_one == True:
            pygame.mixer.music.rewind()
            self.start = time.time()
        elif count < 4.0:
            if (self.current_song_index - 1) > 0:
                self.current_song_index = self.current_song_index - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song_index]
                    + "/"
                    + self.now_playing_list[self.current_song_index]
                )
                self.play_it()
                self.now_playing_song = self.now_playing_list[self.current_song_index]
                self.change_song_label(self.now_playing_song)
                self.update_album_cover(self.cover)
            elif (self.current_song_index - 1) == 0:
                self.current_song_index = self.current_song_index - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song_index]
                    + "/"
                    + self.now_playing_list[self.current_song_index]
                )
                self.play_it()
                self.now_playing_song = self.now_playing_list[self.current_song_index]
                self.change_song_label(self.now_playing_song)
                self.update_album_cover(self.cover)
            elif (self.current_song_index) == 1:
                self.current_song_index = self.current_song_index - 1
                self.load_it(
                    self.current_path_dir_list[self.current_song_index]
                    + "/"
                    + self.now_playing_list[self.current_song_index]
                )
                self.play_it()
                self.now_playing_song = self.now_playing_list[self.current_song_index]
                self.change_song_label(self.now_playing_song)
                self.update_album_cover(self.cover)
            else:
                pygame.mixer.music.rewind()
                self.change_song_label(self.now_playing_song)
                self.update_album_cover(self.cover)
        else:
            pygame.mixer.music.rewind()
            self.start = time.time()

    def open_it(self):
        """Launches Dialog Box to Choose Music Files for Play."""
        self.playlist_name = "Now Playing"
        self.now_playing_list.clear()
        self.current_path_dir_list.clear()
        file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        if file_list == []:
            showinfo(
                title="No Files",
                message=f"No files Chosen!",
            )
            return None
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
            self.current_path_dir_list[self.current_song_index]
            + "/"
            + self.now_playing_list[self.current_song_index]
        )
        self.get_meta(
            self.current_path_dir_list[self.current_song_index],
            self.now_playing_list[self.current_song_index],
        )
        self.save_closing_list()
        self.play_it()
        self.now_playing_song = self.now_playing_list[self.current_song_index]
        self.change_song_label(self.now_playing_song)
        self.update_album_cover(self.cover)

    def update_now_playing(self, songs):
        """Updates the File Window Widget."""
        if not isinstance(songs, list):
            raise ValueError("Songs loaded must be list type.")
        self.file_window.delete(0, END)
        for file in songs:
            self.file_window.insert(END, file)

    def play_selected_item(self, event):
        """Plays File from File Window Widget Selected With the Cursor by User."""
        index = self.file_window.curselection()
        if index == ():
            showinfo(
                title="Error",
                message="Must click on a track to play it.",
            )  
        elif index[0] < 0:
            raise Exception("Negative index not valid.")
        else:
            self.current_song_index = int(index[0])
            self.load_it(
                self.current_path_dir_list[self.current_song_index]
                + "/"
                + self.now_playing_list[self.current_song_index]
            )
            self.get_meta(
                self.current_path_dir_list[self.current_song_index],
                self.now_playing_list[self.current_song_index],
            )
            self.play_it()
            self.now_playing_song = self.now_playing_list[self.current_song_index]
            self.change_song_label(self.now_playing_song)
            self.update_album_cover(self.cover)

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

    def save_closing_list(self):
        """Saves the Now Playing List Displayed in File Window When Program Closes. If First Time Launching,
        closing_list.csv is Created to Be Recalled and Loaded Next Time Program is Loaded."""
        for i in range(len(self.now_playing_list)):
            self.closing_list.append(
                dict(
                    PL_Name="Closing_List",
                    Path=self.current_path_dir_list[i] + "/",
                    File_Name=self.now_playing_list[i],
                    Title=self.title,
                    Artist=self.artist,
                    Album=self.album,
                    Track_Length=self.duration,
                    Album_Cover=self.cover,
                )
            )
        if not os.path.isdir("./Playlist"):
            os.makedirs("Playlist")
            with open("./Playlist/closing_list.csv", "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
                writer.writeheader()
                writer.writerows(self.closing_list)
        else:
            with open("./Playlist/closing_list.csv", "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
                writer.writeheader()
                writer.writerows(self.closing_list)
            self.closing_list.clear()

    def fetch_closing_list(self):
        """Fetch closing_list.csv to Populate Now Playing File Window on program launch. If First Time Opening Program,
        Function is Skipped."""
        if exists("./Playlist/closing_list.csv"):
            with open("./Playlist/closing_list.csv", "r") as openfile:
                csv_file = csv.DictReader(openfile)
                for lines in csv_file:
                    self.current_path_dir_list.append(lines["Path"])
                    self.now_playing_list.append(lines["File_Name"])
                self.update_now_playing(self.now_playing_list)
                self.load_it(
                    self.current_path_dir_list[0] + "/" + self.now_playing_list[0]
                )
                self.get_meta(self.current_path_dir_list[0], self.now_playing_list[0])
                self.update_album_cover(self.cover)
        else:
            pass

    def open_playlist(self, *args):
        """Open and Load an Existing Playlist."""
        if exists("./Playlist"):
            showinfo(
                title="Pick A Playlist",
                message="Pick a Playlist!",
            )
            file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
            if file_2 == None:
                raise Exception("No file was chosen.")
            csv_file = csv.DictReader(file_2)
            self.now_playing_list.clear()
            self.current_path_dir_list.clear()
            for lines in csv_file:
                self.current_path_dir_list.append(lines["Path"])
                self.now_playing_list.append(lines["File_Name"])
            self.update_now_playing(self.now_playing_list)
            self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
            self.get_meta(self.current_path_dir_list[0], self.now_playing_list[0])
            self.now_playing_song = self.now_playing_list[0]
            self.change_song_label(self.now_playing_song)
            self.update_album_cover(self.cover)
            self.change_pl_label(lines["PL_Name"])
            self.save_closing_list()
        else:
            showinfo(
                title="Error",
                message="No Playlists Available!",
            )

    def create_playlist(self):
        """Create a New Playlist."""
        self.new_playlist.clear()
        user_input = simpledialog.askstring(
            title="Playlist Name", prompt="Name this playlist: "
        )
        if user_input == "":
            showinfo(title="Title Error", message="Please Choose a Name for this list")
            self.create_playlist()
        showinfo(
                title="Add Songs",
                message="Pick Songs to Add.",
            )
        file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        if file_list == []:
            showinfo(
                title="No Files",
                message="No files Chosen!",
            )
            #return None
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        pl_name = user_input
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        for (directory_1, name_1) in heads_tails:
            for pic in glob.glob(f"{directory_1}/*jpg"):
                self.cover = pic
                self.get_meta(directory_1, name_1)
                self.new_playlist.append(
                    dict(
                        PL_Name=pl_name,
                        Path=directory_1,
                        File_Name=name_1,
                        Title=self.title,
                        Artist=self.artist,
                        Album=self.album,
                        Track_Length=self.duration,
                        Album_Cover=self.cover,
                    )
                )
        data_new = pd.DataFrame(self.new_playlist)
        if not os.path.isdir("./Playlist"):
            os.makedirs("Playlist")
        data_new.to_csv(f"./Playlist/{pl_name}.csv", index=False)
    
        self.new_playlist = data_new["File_Name"].tolist()
        self.update_pl_editor(self.new_playlist)
        showinfo(
            title="Create Playlist Complete",
            message=f"You Created: {pl_name}!",
        )

    def add_to_playlist(self):
        """Add Songs to an Existing Playlist."""
        self.new_playlist.clear()
        self.editing_list.clear()
        showinfo(
                title="Choose Playlist",
                message="Choose a Playlist You Want to Edit!",
            )
        file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
        data = pd.read_csv(file_2)
        self.editing_list = data["File_Name"].tolist()
        self.update_pl_editor(self.editing_list)
        pl_name = data["PL_Name"].loc[data.index[1]]
        showinfo(
                title="Songs",
                message="Pick Songs to Add.",
            )
        file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        for (directory_1, name_1) in heads_tails:
            self.editing_list.append(name_1)
            for pic in glob.glob(f"{directory_1}/*jpg"):
                self.cover = pic
                self.get_meta(directory_1, name_1)
                self.new_playlist.append(
                    dict(
                        PL_Name=pl_name,
                        Path=directory_1,
                        File_Name=name_1,
                        Title=self.title,
                        Artist=self.artist,
                        Album=self.album,
                        Track_Length=self.duration,
                        Album_Cover=self.cover,
                    )
                )
        data_new = pd.DataFrame(self.new_playlist)
        new_df = pd.concat([data, data_new], ignore_index=True)
        new_df.reset_index()
        new_df.to_csv(f"./Playlist/{pl_name}.csv", index=False)
        fresh_data = pd.read_csv(f"./Playlist/{pl_name}.csv")
        self.new_playlist = fresh_data["File_Name"].tolist()
        self.update_pl_editor(self.new_playlist)
        showinfo(
            title="Add To Playlist Complete",
            message=f"You added some sweet tracks to: {pl_name}!",
        )

    def delete_from_playlist(self):
        """Remove Song(s) From an Existing Playlist."""
        self.new_playlist.clear()
        self.editing_list.clear()
        showinfo(
                title="Remove",
                message="Choose a Playlist to Edit.",
            )
        file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
        data = pd.read_csv(file_2)
        self.editing_list = data["File_Name"].tolist()
        self.update_pl_editor(self.editing_list)
        showinfo(
                title="Songs",
                message="Choose Songs to Remove.",
            )
        file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        heads_tails = []
        for items in file_list:
            heads_tails.append(os.path.split(items))
        for (directory_1, name_1) in heads_tails:
            self.new_playlist.append(name_1)
        for song in self.new_playlist:
            data = data[data["File_Name"] != song]
        pl_name = data["PL_Name"].loc[data.index[1]]
        data.to_csv(f"./Playlist/{pl_name}.csv", index=False)
        fresh_data = pd.read_csv(f"./Playlist/{pl_name}.csv")
        new_list = fresh_data["File_Name"].tolist()
        self.update_pl_editor(new_list)
        showinfo(
            title="Removal Complete",
            message=f"You removed tracks from: {pl_name}!",
        )

    def launch_pl_editor(self):
        """Launches the Playlist Editor Window."""
        root_2 = Tk()
        root_2.title("Playlist Editor")
        root_2.geometry("600x800")
        root_2.columnconfigure(0, weight=4)
        root_2.columnconfigure(1, weight=1)
        # Add List Box to root
        self.pl_window = tk.Listbox(
            root_2,
            listvariable=self.list_var,
            height=40,
            width=65,
            bg="#9F73AB",
            selectmode=tk.BROWSE,
            justify=CENTER,
        )
        self.pl_window.grid(column=0, row=0, padx=10, pady=10)
        # Button frame
        self.button_frame = ttk.Frame(root_2, padding=5)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.grid(columnspan=2, row=1)
        # Add buttons to frame
        self.add_button = ttk.Button(
            self.button_frame, text="Create New Playlist", command=self.create_playlist
        ).grid(column=0, row=1)
        self.add_button = ttk.Button(
            self.button_frame,
            text="Remove from Playlist",
            command=self.delete_from_playlist,
        ).grid(column=1, row=1)
        self.add_button = ttk.Button(
            self.button_frame, text="Add To Playlist", command=self.add_to_playlist
        ).grid(column=2, row=1)

    def update_pl_editor(self, songs):
        """Updates the Playlist Editor Window Widget."""
        if not isinstance(songs, list):
            raise ValueError("Songs loaded must be list type.")
        self.pl_window.delete(0, END)
        for file in songs:
            self.pl_window.insert(END, file)

    def shuffle(self):
        """Shuffles Order of Now Playing List."""
        random.shuffle(self.now_playing_list)
        self.update_now_playing(self.now_playing_list)

    def loop(self):
        """Toggle Loop Single On/Off."""
        if self.loop_one == True:
            self.looper_l.set("LOOP ALL")
            self.loop_one = False
        else:
            self.looper_l.set("LOOP ONE")
            self.loop_one = True


# Launch Program
T = Triad()
