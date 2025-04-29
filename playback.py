import pygame

class Playback(object):
    """Controls playback options."""
    def __init__(self):
        # Initialize Pygame Mixer Module to Enable Playback
        pygame.mixer.init()
        self.is_playing = is_playing
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
    
    def open_it(self):
        """Launches Dialog Box to Choose Music Files for Play."""
        print("OpenIT!")
        # self.playlist_name = "Now Playing"
        # self.now_playing_list.clear()
        # self.current_path_dir_list.clear()
        # file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        # if file_list == []:
        #     showinfo(
        #         title="No Files",
        #         message=f"No files Chosen!",
        #     )
        #     return None
        # heads_tails = []
        # for items in file_list:
        #     heads_tails.append(os.path.split(items))
        # for (directory_1, name_1) in heads_tails:
        #     self.current_path_dir_list.append(directory_1)
        #     self.now_playing_list.append(name_1)
        # self.now_playing_list.sort()
        # songs = self.now_playing_list
        # self.update_now_playing(songs)
        # self.load_it(
        #     self.current_path_dir_list[self.current_song_index]
        #     + "/"
        #     + self.now_playing_list[self.current_song_index]
        # )
        # self.get_meta(
        #     self.current_path_dir_list[self.current_song_index],
        #     self.now_playing_list[self.current_song_index],
        # )
        # self.save_closing_list()
        # self.play_it()
        # self.now_playing_song = self.now_playing_list[self.current_song_index]
        # self.change_song_label(self.now_playing_song)
        # self.update_album_cover(self.cover)

    def load_it(self, file):
        """Load File for Playback."""
        print("Load It!")
        # if not isinstance(file, str):
        #     raise ValueError("File loaded must be string")
        # if ".mp3" in file:
        #     pygame.mixer.music.load(file)
        # else:
        #     raise Exception("File Type not supported")   
    def queue_next(self):
        """Queues Next Track for Playback. Default Behavior is to Loop All."""
        print("queue_next")
        # if self.loop_one == True:
        #     pygame.mixer.music.queue(
        #         self.current_path_dir_list[(self.current_song_index - 1)]
        #         + "/"
        #         + self.now_playing_list[(self.current_song_index - 1)]
        #     )
        # else:
        #     if (self.current_song_index + 1) < len(self.now_playing_list):
        #         pygame.mixer.music.queue(
        #             self.current_path_dir_list[(self.current_song_index + 1)]
        #             + "/"
        #             + self.now_playing_list[(self.current_song_index + 1)]
        #         )
        #     else:
        #         pygame.mixer.music.queue(
        #             self.current_path_dir_list[0] + "/" + self.now_playing_list[0]
        #         ) 
    def play_it(self):
        """Play File Loaded for Playback."""
        print("PLay it!")
        # pygame.mixer.music.play()
        # self.get_meta(
        #     self.current_path_dir_list[self.current_song_index],
        #     self.now_playing_list[self.current_song_index],
        # )
        # self.is_playing = True
        # self.update_album_cover(self.cover)
        # self.queue_next()
    def play_selected_item(self, event):
        """Plays File from File Window Widget Selected With the Cursor by User."""
        print("play selected")
        # index = self.file_window.curselection()
        # if index == ():
        #     showinfo(
        #         title="Error",
        #         message="Must click on a track to play it.",
        #     )  
        # elif index[0] < 0:
        #     raise Exception("Negative index not valid.")
        # else:
        #     self.current_song_index = int(index[0])
        #     self.load_it(
        #         self.current_path_dir_list[self.current_song_index]
        #         + "/"
        #         + self.now_playing_list[self.current_song_index]
        #     )
        #     self.get_meta(
        #         self.current_path_dir_list[self.current_song_index],
        #         self.now_playing_list[self.current_song_index],
        #     )
        #     self.play_it()
        #     self.now_playing_song = self.now_playing_list[self.current_song_index]
        #     self.change_song_label(self.now_playing_song)
        #     self.update_album_cover(self.cover)

    def pause_it(self):
        """Pause File Currently Playing. Press Again to Resume."""
        print("Pause it!")
        # if self.is_playing:
        #     pygame.mixer.music.pause()
        #     self.is_playing = False
        #     self.pause_l.set("Resume")
        # else:
        #     pygame.mixer.music.unpause()
        #     self.is_playing = True
        #     self.pause_l.set("Pause")

    def fwd_it(self):
        """FWD Loads Next Track in Que and Plays It."""
        print("fwd it!")
        # if self.loop_one == True:
        #     self.current_song_index = self.current_song_index
        #     self.load_it(
        #         self.current_path_dir_list[self.current_song_index]
        #         + "/"
        #         + self.now_playing_list[self.current_song_index]
        #     )
        #     self.play_it()
        #     self.now_playing_song = self.now_playing_list[self.current_song_index]
        #     self.change_song_label(self.now_playing_song)
        #     self.update_album_cover(self.cover)

        # elif (self.current_song_index + 1) < len(self.now_playing_list):
        #     self.current_song_index = self.current_song_index + 1
        #     self.load_it(
        #         self.current_path_dir_list[self.current_song_index]
        #         + "/"
        #         + self.now_playing_list[self.current_song_index]
        #     )
        #     self.play_it()
        #     self.now_playing_song = self.now_playing_list[self.current_song_index]
        #     self.change_song_label(self.now_playing_song)
        #     self.update_album_cover(self.cover)

        # else:
        #     self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
        #     self.current_song_index = 0
        #     self.play_it()
        #     self.now_playing_song = self.now_playing_list[self.current_song_index]
        #     self.change_song_label(self.now_playing_song)
        #     self.update_album_cover(self.cover)

    def rwd_it(self):
        """Return to the Beginning of Currently Loaded Song.
        If RWD Button Pressed < 4 Seconds After Start of Track,
        Skips Back to Previous Track in Que."""
        print("rwd it!")
        # self.stop = time.time()
        # count = self.stop - self.start
        # if self.loop_one == True:
        #     pygame.mixer.music.rewind()
        #     self.start = time.time()
        # elif count < 4.0:
        #     if (self.current_song_index - 1) > 0:
        #         self.current_song_index = self.current_song_index - 1
        #         self.load_it(
        #             self.current_path_dir_list[self.current_song_index]
        #             + "/"
        #             + self.now_playing_list[self.current_song_index]
        #         )
        #         self.play_it()
        #         self.now_playing_song = self.now_playing_list[self.current_song_index]
        #         self.change_song_label(self.now_playing_song)
        #         self.update_album_cover(self.cover)
        #     elif (self.current_song_index - 1) == 0:
        #         self.current_song_index = self.current_song_index - 1
        #         self.load_it(
        #             self.current_path_dir_list[self.current_song_index]
        #             + "/"
        #             + self.now_playing_list[self.current_song_index]
        #         )
        #         self.play_it()
        #         self.now_playing_song = self.now_playing_list[self.current_song_index]
        #         self.change_song_label(self.now_playing_song)
        #         self.update_album_cover(self.cover)
        #     elif (self.current_song_index) == 1:
        #         self.current_song_index = self.current_song_index - 1
        #         self.load_it(
        #             self.current_path_dir_list[self.current_song_index]
        #             + "/"
        #             + self.now_playing_list[self.current_song_index]
        #         )
        #         self.play_it()
        #         self.now_playing_song = self.now_playing_list[self.current_song_index]
        #         self.change_song_label(self.now_playing_song)
        #         self.update_album_cover(self.cover)
        #     else:
        #         pygame.mixer.music.rewind()
        #         self.change_song_label(self.now_playing_song)
        #         self.update_album_cover(self.cover)
        # else:
        #     pygame.mixer.music.rewind()
        #     self.start = time.time()
    
    def shuffle(self):
        """Shuffles Order of Now Playing List."""
        print("shuffle it")
        # random.shuffle(self.now_playing_list)
        # self.update_now_playing(self.now_playing_list)

    def loop(self):
        """Toggle Loop Single On/Off."""
        pint("loop it")
        # if self.loop_one == True:
        #     self.looper_l.set("LOOP ALL")
        #     self.loop_one = False
        # else:
        #     self.looper_l.set("LOOP ONE")
        #     self.loop_one = True