from tkinter import *
from tkinter import ttk

import pygame

# from pydub import AudioSegment
# from pydub.playback import play

# Initialize sound module
class Triad():

    def __init__(self, is_playing=False, file = "Michał Lewicki - Ton - 05 Komeda.mp3"):
        """Launch mixer in background to allow for sound to play. 
           Load last played playlist or last file folder location."""
        
        pygame.mixer.init()
        self.file = file
        self.load_it(file)
        self.is_playing = is_playing
        self.play_label = "Play"
        root = Tk()
        root.title("Triad")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.play_button = ttk.Button(mainframe, text=self.play_label, command=self.play_it).grid(column=1, row=3, sticky=E)
        self.pause_button = ttk.Button(mainframe, text="Pause", command=self.pause_it).grid(column=2, row=3, sticky=W)
        self.unpause_button = ttk.Button(mainframe, text="Resume", command=self.unpause_it).grid(column=3, row=3, sticky=W)
        self.rewind_button = ttk.Button(mainframe, text="RWD", command=self.rwd_it).grid(column=4, row=3, sticky=E)
        self.forward_button = ttk.Button(mainframe, text="FWD", command=self.fwd_it).grid(column=5, row=3, sticky=W)
        root.mainloop()

    def load_it(self, file):
        """Load file for playback"""
        pygame.mixer.music.load(file)
    
    def change_label(self):
        """Change label on play button to pause when playing"""
        if self.is_playing:
            self.play_label = "Pause"
        else:
            self.play_label = "Play"

    def play_it(self):
        """Play file loaded for playback"""
        pygame.mixer.music.play()
        self.is_playing = True
        self.change_label()
        
    def pause_it(self):
        """Pause File currently playing"""
        pygame.mixer.music.pause()
        self.is_playing = False
        self.change_label()

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

T = Triad()