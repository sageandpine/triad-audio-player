## Libraries being imported:

* importing libraries:
* import tkinter as tk
* from tkinter import *
* from tkinter import filedialog as fd
* from tkinter import ttk
* from tkinter.messagebox import showinfo
* from tinytag import TinyTag as td
* import os
* from os.path import exists
* import pygame
* import time
* import json

# List of steps/Order of tasks:

## Tackled:

X * Create Basic Box GUI Tkinter
X * Allow user to pick the folder to read from
X * Add PLAY function
      X * Load and play mp3 files
X * Tie PLay button to function
X * Add Stop function
X * Add Stop Button
X * Add Pause function
X * Add Pause Button 
X * Show contents of File Folder selected in it's own window
X * Prettify Text So file extension is removed
X * Add FWD function
X * Add FWD button
X * Show currently playing song
X * Tie FWD button to function
X  * index playlist so last track plays
X  * if at end of playlist... start over
X * When continue to next track automatically update list.
X * Repeat with RWD function/button
X * RWD currently only goes to begining of track. Does not skip back to the previous track in the list
X * Logo window
X * Display playlist in window
X * Get button label to toggle: PAUSE/UNPAUSE
X * Make songs selectable and make them play
X * update now playing label
X * Pause/unpause toggles correctly.
X * Retrieve metadata from files
X * HELP window connect to drop down option
X * TRIAD window connect to drop down option
X * Fix RWD Bug
X* BUG: RWD/SKIP BACK "When I reach the second track skipping backwards this error is thrown" Recursion error hd to do with 2 functions bouncing off one another. **RWD_IT & Skip_Back**. This is where the recursion was happening. Combining the logic of these two functions into one rewind function should take care of this problem.
X * Must figure out how to save file when program closes. Open file when program loads
X * Save now_playing playlist when program closes
X * Fetch last_played playlist when program opens
X * Testing is just doing my head in. Not functioning as expected.
X * Check out Py Fundamentals 20.2 for CSV logic in playlists
X * Advanced 10.5 for exceptions
X * Create Unit Tests for some existing functions
X 
X * Create new playlist Function
X * If lists exist show them as possibilities
X * Create a New playlist using CSV
X * Add to Playlist function
X * Refactor load_it to work with files not dir
X* When opening playlists, directory needs to be changed per file/song to load correctly
X * When A user picks a song with the mouse, the indexing is thrown off. RWD skips back 2 while FWD advances by 3 
X * MkDir for PLaylists
X * Identify/Display Album Art in window Not working
X * Shuffle
X * Loop 1
X * Loop All
X * Create Playlists Launches THAT playlist automatically
X * Need a popup to easily view and edit playlists.'
    X - maybe there is a dropdown PLaylist button that launches the window
    X - window has options
    X - open/create/edit buttons
X * Add to PLaylist button
X * View Playlists function 
X * Add to Playlist doesn't update the current window if it is the playlist being edited.
X * Remove from PLaylist function
X * Remove from PLaylist button
X * Pandas Solved~~Removing files from a csv is tricky. CSV files, are not actual databases. I did not remember this.~~
X * CSV makes creation AND adding to easy, but removing it not so much
X * ~~Add to playlist has a crazy loop that shows the list in the window correctly, but the csv has a billion duplicates
    X- Instead of adding ONLY the new tracks it adds the original list AND the new file in CSV- 
    X- Solved * editing pl list never cleared
    X- Could be solved with Panda~~
X * Main Window GUI TITLE CHANGE    
X * PLaylist functions throwing traceback errors for the team. finding the ui difficult to navigate.
  X - Try making things editable from the list. Instead of a click 'playing'like the main window,
 X  a click on an item could remove/cancel item. All playlist functions might have a dialog that gives X more info "Pick the playlist" "Now pick a File". That kind of thing.
   
X * Sarahs Bug 2: Open playlist. If no playlist is selected I replicated the error by 
X not choosing a playlist. Maybe this could be handled with an exception?
   X - Fix 1 If newly opening there is no 'Playlist' folder so trying to pick a playlist now tells you
   X there are no playlists yet. 

X * Sarahs Bug 1: This error appears to be triggered by clicking the mouse in a
X window where no songs are present. I have updated the code to handle this exception.
X * Alex's Bug 1:
X * Ask user when adding to playlist if they want to load that list
X * Update all functions to use pandas exclusively to work with playlists

---

## Remaining Core Functions:

* Update Play function to play any music format

---

## BUGS/Problems:

* Tried to combine PLay/Pause/Unpause but the logic is giving me trouble. 
* When Using Shuffle, Selected items for playback runs into an error-index is thrown off, items in middle not registering as existing?

## Notes:



---


## Advanced functions:
* Accept FLAC & WAV
* Visualiser Window
* Opaque Visualiser over track list
* Catapillar track list
* Allow User to link Spotify to GUI
* Light/Dark Theme
* Various Skins/Themes
* Package and distribute




### Code for later


