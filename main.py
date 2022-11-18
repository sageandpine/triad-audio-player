import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

# from mutagen.easyid3 import EasyID3
# from tkinter.messagebox import showinfo
import os
import pygame

# from pydub import AudioSegment
# from pydub.playback import play

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

        # Tk Window for application
        root = Tk()
        root.title("Triad")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Tk Frame that fits inside window
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # self.pl_var = tk.Variable(value=self.play_label)

        # Buttons for Basic Functions
        self.play_button = ttk.Button(
            mainframe, text="Play", command=self.play_it
        ).grid(column=1, row=3, sticky=E)
        self.pause_button = ttk.Button(
            mainframe, text="Pause", command=self.pause_it
        ).grid(column=2, row=3, sticky=W)
        self.unpause_button = ttk.Button(
            mainframe, text="Resume", command=self.unpause_it
        ).grid(column=3, row=3, sticky=W)
        self.rewind_button = ttk.Button(
            mainframe, text="RWD", command=self.rwd_it
        ).grid(column=4, row=3, sticky=E)
        self.forward_button = ttk.Button(
            mainframe, text="FWD", command=self.fwd_it
        ).grid(column=5, row=3, sticky=W)
        self.open_button = ttk.Button(
            mainframe, text="Open", command=self.open_it
        ).grid(column=5, row=3, sticky=W)

        # New Frame for listing files when directory chosen
        self.now_playing_list = ["a song", "another one"]
        self.var = tk.Variable(value=self.now_playing_list)

        # Frame that lists contents of chosen directory
        fileframe = ttk.Frame(root, padding="3 3 12 12")
        fileframe.grid(columnspan=4, row=1, sticky=W)
        self.file_window = tk.Listbox(fileframe, listvariable=self.var, height=10)
        self.file_window.grid(column=1, row=0)

        # Main Loop Launches the GUI and keeps it running until the program terminates
        root.mainloop()

    def load_it(self, file):
        """Load file for playback"""
        # print(f"load it took on this file: {file}")
        pygame.mixer.music.load(file)

    def change_label(self):
        """*NOT WORKING ATM -Change label on play button to pause when playing"""
        pass
        # Might need to REfresh window to see change

    # if self.is_playing:
    #     self.play_label = "Pause"
    # else:
    #    self.play_label = "Play"

    def play_it(self):
        """Play file loaded for playback"""
        pygame.mixer.music.play()
        self.is_playing = True

    def pause_it(self):
        """Pause File currently playing"""
        pygame.mixer.music.pause()
        self.is_playing = False

    def unpause_it(self):
        """UnPause File That is paused. Combine with Pause via With loop"""
        pygame.mixer.music.unpause()
        self.is_playing = True

    def fwd_it(self):
        """FWD should load a new track and play it"""
        pass

    def rwd_it(self):
        """Go back to the begining of currently loaded song"""
        pygame.mixer.music.rewind()

    def open_it(self):
        """Launch dialog box to choose a file or folder to pick from. Opens file/directory chosen and plays"""
        self.now_playing_list.clear()
        path = str(fd.askdirectory())
        file_list = os.listdir(path)
        for file in file_list:
            # print(file)
            if ".mp3" in file:
                self.now_playing_list.append(file)
        self.now_playing_list.sort()
        songs = self.now_playing_list
        self.update_now_playing(songs)
        self.load_it(path + "/" + self.now_playing_list[0])
        self.play_it()

    def update_now_playing(self, songs):
        """Updates the file_window widget."""
        self.file_window.delete(0, END)
        for file in songs:
            self.file_window.insert(0, file)


T = Triad()
