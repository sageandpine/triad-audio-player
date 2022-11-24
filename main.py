import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import os
import pygame
import time

# from tkinter.messagebox import showinfo

# Initialize sound module
class Triad:
    def __init__(self, is_playing=False):
        """Launch mixer in background to allow for sound to play.
        Load last played playlist or last file folder location."""

        # Initialize pygame mixer module to enable sound
        pygame.mixer.init()

        # Default attributes
        self.is_playing = is_playing
        self.play_label = "Play"
        self.current_song = 0
        self.current_path_dir = ""
        self.next = ""
        self.now_song = ""
        self.start = 0
        self.stop = 0

        # Tk Window for application
        root = Tk()
        root.title("Triad")
        root.geometry("600x400")
        root.columnconfigure(0, weight=1)
        root.resizable(0, 0)

        menuubar = Menu(root)
        root.config(menu=menuubar)
        
        # Create menu bar

        # File Menu Drop Down
        file_menu = Menu(menuubar, tearoff=0)
        file_menu.add_command(
            label='Open',
            command=self.open_it
        )

        file_menu.add_command(
            label='Exit',
            command=root.destroy
        )
        
        
        # Help Menu Drop Down
        help_menu = Menu(menuubar, tearoff=0)
        menuubar.add_cascade(
            label="File",
            menu=file_menu
        )
        menuubar.add_cascade(
            label="About",
            menu=help_menu
        )
        help_menu.add_command(
            label='TRIAD',
            command=self.open_it
        )
        help_menu.add_command(
            label='Help',
            command=self.open_it
        )

        # Tk Frame that fits inside window
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=5, sticky=(N, W, E, S))

        # Buttons for Basic Functions
        self.play_button = ttk.Button(
            mainframe, text="Play", command=self.play_it
        ).grid(column=0, row=1)
        self.pause_button = ttk.Button(
            mainframe, text="Pause", command=self.pause_it
        ).grid(column=0, row=2)
        self.rewind_button = ttk.Button(
            mainframe, text="RWD", command=self.rwd_it
        ).grid(column=0, row=3)
        self.forward_button = ttk.Button(
            mainframe, text="FWD", command=self.fwd_it
        ).grid(column=0, row=4)
        
        self.now_playing_list = []
        self.track_index = len(self.now_playing_list)
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
        self.photo = tk.PhotoImage(file="./triad_dog.png")
        imageframe = ttk.Frame(root, padding="3 3 12 12")
        imageframe.grid(column=2, row=4, sticky=W)
        self.imageframe = ttk.Label(imageframe, image=self.photo, padding=2)
        self.imageframe.grid(column=0, row=2)

        # Frame that lists contents of chosen directory
        fileframe = ttk.Frame(root, padding="3 3 12 12")
        fileframe.grid(columnspan=1, row=4, sticky=W)
        self.file_window = tk.Listbox(
            fileframe, listvariable=self.var, height=10, width=45, bg="#9F73AB"
        )
        self.file_window.grid(column=2, row=0)

        # Main Loop Launches the GUI and keeps it running until the program terminates
        root.mainloop()

    def load_it(self, file):
        """Load file for playback"""
        pygame.mixer.music.load(file)

    def change_label(self, new):
        """Change text label to reflect song playing."""
        self.now_var.set(new)

    def queue_next(self):
        """Queues next track for playback. If user is at end of playlist, loads 1st track to start over."""
        if (self.current_song + 1) < len(self.now_playing_list):
            pygame.mixer.music.queue(
                self.current_path_dir
                + "/"
                + self.now_playing_list[(self.current_song + 1)]
            )
        else:
            pygame.mixer.music.queue(
                self.current_path_dir + "/" + self.now_playing_list[0]
            )

    def play_it(self):
        """Play file loaded for playback."""
        pygame.mixer.music.play()
        self.is_playing = True
        self.start = time.time()
        self.queue_next()

    def pause_it(self):
        """Pause File currently playing."""
        pygame.mixer.music.pause()
        self.is_playing = False

    def unpause_it(self):
        """UnPause File That is paused. Combine with Pause via With loop."""
        pygame.mixer.music.unpause()
        self.is_playing = True

    def fwd_it(self):
        """FWD should load a new track and play it. When we come to the end of the playlist, automatically re-starts at track 1."""
        if (self.current_song + 1) < len(self.now_playing_list):
            self.current_song = self.current_song + 1
            self.load_it(
                self.current_path_dir + "/" + self.now_playing_list[self.current_song]
            )
            self.play_it()
            self.now_song = self.now_playing_list[self.current_song]
            self.change_label(self.now_song)

        else:
            self.load_it(self.current_path_dir + "/" + self.now_playing_list[0])
            self.current_song = 0
            self.play_it()
            self.now_song = self.now_playing_list[self.current_song]
            self.change_label(self.now_song)

    def skip_back(self):
        """Skips back to previous track."""
        if (self.current_song - 1) > 0:
            self.current_song = self.current_song - 1
            self.load_it(
                self.current_path_dir + "/" + self.now_playing_list[self.current_song]
            )
            self.play_it()
            self.now_song = self.now_playing_list[self.current_song]
            self.change_label(self.now_song)
        else:
            self.rwd_it()
            self.change_label(self.now_song)

    def rwd_it(self):
        """Go back to the begining of currently loaded song, if button pressed less than 2 seconds after start, skip_back()"""
        # Buggy - When skipping back, track 1 throws a recursion error and will not load Track 1
        self.stop = time.time()
        count = self.stop - self.start
        if count < 4.0:
            self.skip_back()
        else:
            pygame.mixer.music.rewind()
            self.start = time.time()

    def open_it(self):
        """Launch dialog box to choose a file or folder to pick music from. Opens file/directory chosen and starts to play."""
        self.now_playing_list.clear()
        self.current_path_dir = str(fd.askdirectory())
        file_list = os.listdir(self.current_path_dir)
        for file in file_list:
            if ".mp3" in file:
                self.now_playing_list.append(file)
        self.now_playing_list.sort()
        songs = self.now_playing_list
        self.update_now_playing(songs)
        self.load_it(
            self.current_path_dir + "/" + self.now_playing_list[self.current_song]
        )
        self.play_it()
        self.now_song = self.now_playing_list[self.current_song]
        self.change_label(self.now_song)

    def update_now_playing(self, songs):
        """Updates the file_window widget."""
        self.file_window.delete(0, END)
        for file in songs:
            self.file_window.insert(END, file)


T = Triad()
