from tkinter import *
from tkinter import ttk
import pygame
# from pydub import AudioSegment
# from pydub.playback import play

# Initialize sound module
pygame.mixer.init()

def load_it(file):
    """Load file for playback"""
    pygame.mixer.music.load(file)
    
def play_it():
    """Play file loaded for playback"""
    pygame.mixer.music.play()

def pause_it():
    """Pause File currently playing"""
    pygame.mixer.music.pause()

def unpause_it():
    """UnPause File That is paused. Combine with Pause via With loop"""
    pygame.mixer.music.unpause()

def fwd_it():
    """FWD should load a new track and play it"""
    pass
    
def rwd_it():
    """Go back to the begining of currently loaded song"""
    pygame.mixer.music.rewind()


root = Tk()

root.title("Triad")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Play", command=play_it).grid(column=1, row=3, sticky=E)
ttk.Button(mainframe, text="Pause", command=pause_it).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="RWD", command=rwd_it).grid(column=3, row=3, sticky=E)
ttk.Button(mainframe, text="FWD", command=fwd_it).grid(column=4, row=3, sticky=W)

load_it("Michał Lewicki - Ton - 05 Komeda.mp3")


root.mainloop()
