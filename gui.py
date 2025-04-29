from playback import Playback
from playlist import Playlist

import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from tinytag import TinyTag as td
from PIL import Image, ImageTk

class UserInterface(object):
    """GUI"""
    def __init__(self):    
        self.pause_label = "PAUSE"
        self.loop_label = "LOOP ALL"
    
    def main_gui(self):    
        # Root GUI Window
        self.root = Tk()
        self.root.title("TRIAD Audio Player")
        self.root.geometry("800x290")
        self.root.columnconfigure(0, weight=4)
        self.root.columnconfigure(1, weight=1)
        # Create Menu Bar Widget
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # File Menu Drop Down
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Open Files", command=Playback.open_it) # Call to command from diff class
        self.file_menu.add_command(label="Open Playlist", command=Playlist.open_playlist) # call to other class
        self.file_menu.add_command(
            label="Create/Edit Playlists", command=self.launch_pl_editor # other class call
        )
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        # Help Menu Drop Down
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="About", menu=self.help_menu)
        self.help_menu.add_command(
            label="TRIAD",
            command=lambda: showinfo(
                title="TRIAD",
                message="Triad is a wicked awesome audio player built by pc84! Enjoy!",
            ),
        )
        self.help_menu.add_command(
            label="Help",
            command=lambda: showinfo(
                title="Help",
                message="Visit this projects Github:\ngithub.com/sageandpine/triad-audio-player",
            ),
        )

        # Playlist Variables to Update Labels/Images/Button Widgets
        self.list_var = tk.Variable(value="List of stuff")
        self.song_var = tk.Variable(value="NOw playing")
        # self.list_var = tk.Variable(value=Playlist.now_playing_list)
        # self.song_var = tk.Variable(value=Playlist.now_playing_song)
        self.pl_title_var = tk.Variable(value="NowPLayingListName")
        # self.pl_title_var = tk.Variable(value=Playlist.now_playing_list_name)
        self.pause_l = tk.Variable(value=self.pause_label)
        self.looper_l = tk.Variable(value=self.loop_label)

        # Window Frame & Config
        self.window_frame = ttk.Frame(self.root, padding=5)
        self.window_frame.columnconfigure(0, weight=1)
        self.window_frame.grid(column=0, row=0, sticky=W)

        # Put File List Window Widget in Frame
        self.file_window = tk.Listbox(
            self.window_frame,
            listvariable=self.list_var,
            height=11,
            width=72,
            bg="#9F73AB",
            selectmode=tk.BROWSE,
        )
        self.file_window.grid(column=0, row=0)
        self.file_window.bind("<<ListboxSelect>>", Playback.play_selected_item)

        # Button Frame
        self.button_frame = ttk.Frame(self.root, padding=5)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.grid(column=0, row=1, sticky=W)

        # Add Buttons to Frame
        self.play_button = ttk.Button(
            self.button_frame, text="PLAY", command=Playback.play_it
        ).grid(column=0, row=1)    # other class command

        self.rwd_button = ttk.Button(
            self.button_frame, text="REWIND", command=Playback.rwd_it
        ).grid(column=1, row=1) # other class command

        self.fwd_button = ttk.Button(
            self.button_frame, text="FORWARD", command=Playback.fwd_it
        ).grid(column=2, row=1)     # other class command

        self.pause_button = ttk.Button(
            self.button_frame, textvariable=self.pause_l, command=Playback.pause_it
        ).grid(column=0, row=2)    # other class

        self.shuffle_button = ttk.Button(
            self.button_frame, text="SHUFFLE", command=Playback.shuffle
        ).grid(column=1, row=2)    # other class

        self.loop_button = ttk.Button(
            self.button_frame, textvariable=self.looper_l, command=Playback.loop
        ).grid(column=2, row=2)      # other class command

        # Default Image == Logo/ Replaced by Album Art
        self.photo = ImageTk.PhotoImage(Image.open("./assets/t_dog_logo.png"))

        # Album Frame to Display Image
        self.imageframe = ttk.Frame(self.root, height=200, width=200, padding=5)
        self.imageframe.columnconfigure(0, weight=2)
        self.imageframe.grid(column=2, row=0)

        # Album Cover Image
        self.imageframe = Label(self.imageframe, image=self.photo)
        self.imageframe.grid(column=0, row=0)

        # Playlist Name Label Widget Frame
        self.pl_labelframe = ttk.Frame(self.root, height=100, width=200, padding=5)
        self.pl_labelframe.columnconfigure(0, weight=2)
        self.pl_labelframe.grid(column=2, row=1)

        # Attach Playlist Name Label Widget to Frame
        self.now_playing_list_title = ttk.Label(
            self.pl_labelframe, textvariable=self.pl_title_var, relief=SUNKEN, width=25
        ).grid(column=0, row=1)

        # Make a Frame for Now Playing Ticker Label Widget
        self.label_frame = ttk.Frame(self.root, padding=5)
        self.label_frame.columnconfigure(0, weight=1)
        self.label_frame.grid(column=2, row=1, sticky=W)

        # Now Playing Ticker Label Widget
        self.now_playing = ttk.Label(self.button_frame, text="Now Playing: ", width=29).grid(
            column=3, row=1, padx=5, pady=0, sticky=W
        )
        self.now_playing = ttk.Label(
            self.button_frame,
            textvariable=self.song_var,
            relief=SUNKEN,
            foreground="green",
            width=40,
        ).grid(column=3, row=2, sticky=W, padx=5, pady=0)

        # # Fetch Last Played Playlist & Load on Startup
        # self.fetch_closing_list()

        # # Sets Default Loop Value to Loop All
        # self.loop_one = False

        # Run Main Loop
        self.root.mainloop()

    def launch_pl_editor(self):
        """Launches the Playlist Editor Window."""
        pass
        # root_2 = Tk()
        # root_2.title("Playlist Editor")
        # root_2.geometry("600x800")
        # root_2.columnconfigure(0, weight=4)
        # root_2.columnconfigure(1, weight=1)
        # # Add List Box to root
        # self.pl_window = tk.Listbox(
        #     root_2,
        #     listvariable=self.list_var,
        #     height=40,
        #     width=65,
        #     bg="#9F73AB",
        #     selectmode=tk.BROWSE,
        #     justify=CENTER,
        # )
        # self.pl_window.grid(column=0, row=0, padx=10, pady=10)
        # # Button frame
        # self.button_frame = ttk.Frame(root_2, padding=5)
        # self.button_frame.columnconfigure(0, weight=1)
        # self.button_frame.grid(columnspan=2, row=1)
        # # Add buttons to frame
        # self.add_button = ttk.Button(
        #     self.button_frame, text="Create New Playlist", command=self.create_playlist
        # ).grid(column=0, row=1)
        # self.add_button = ttk.Button(
        #     self.button_frame,
        #     text="Remove from Playlist",
        #     command=self.delete_from_playlist,
        # ).grid(column=1, row=1)
        # self.add_button = ttk.Button(
        #     self.button_frame, text="Add To Playlist", command=self.add_to_playlist
        # ).grid(column=2, row=1)

    def update_pl_editor(self, songs):
        """Updates the Playlist Editor Window Widget."""
        pass
        # if not isinstance(songs, list):
        #     raise ValueError("Songs loaded must be list type.")
        # self.pl_window.delete(0, END)
        # for file in songs:
        #     self.pl_window.insert(END, file)

T = UserInterface()
T.main_gui()
#T.root.mainloop()