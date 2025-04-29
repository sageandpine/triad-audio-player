class Playlist(object):
    """handles playlist operations"""
    def __init__(self):
        self.closing_list = []
        self.new_playlist = []
        self.now_playing_list = []
        self.editing_list = []
        self.current_path_dir_list = []
        self.now_playing_list_name = "Playlist: Now Playing"
        self.current_song_index = 0
        self.current_path_dir = ""
        self.next = ""
        self.now_playing_song = "3...TRIAD...3"
    
    def save_closing_list(self):
        """Saves the Now Playing List Displayed in File Window When Program Closes. If First Time Launching,
        closing_list.csv is Created to Be Recalled and Loaded Next Time Program is Loaded."""
        pass
        # for i in range(len(self.now_playing_list)):
        #     self.closing_list.append(
        #         dict(
        #             PL_Name="Closing_List",
        #             Path=self.current_path_dir_list[i] + "/",
        #             File_Name=self.now_playing_list[i],
        #             Title=self.title,
        #             Artist=self.artist,
        #             Album=self.album,
        #             Track_Length=self.duration,
        #             Album_Cover=self.cover,
        #         )
        #     )
        # if not os.path.isdir("./Playlist"):
        #     os.makedirs("Playlist")
        #     with open("./Playlist/closing_list.csv", "w") as csvfile:
        #         writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
        #         writer.writeheader()
        #         writer.writerows(self.closing_list)
        # else:
        #     with open("./Playlist/closing_list.csv", "w") as csvfile:
        #         writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
        #         writer.writeheader()
        #         writer.writerows(self.closing_list)
        #     self.closing_list.clear()

    def fetch_closing_list(self):
        """Fetch closing_list.csv to Populate Now Playing File Window on program launch. If First Time Opening Program,
        Function is Skipped."""
        pass
        # if exists("./Playlist/closing_list.csv"):
        #     with open("./Playlist/closing_list.csv", "r") as openfile:
        #         csv_file = csv.DictReader(openfile)
        #         for lines in csv_file:
        #             self.current_path_dir_list.append(lines["Path"])
        #             self.now_playing_list.append(lines["File_Name"])
        #         self.update_now_playing(self.now_playing_list)
        #         self.load_it(
        #             self.current_path_dir_list[0] + "/" + self.now_playing_list[0]
        #         )
        #         self.get_meta(self.current_path_dir_list[0], self.now_playing_list[0])
        #         self.update_album_cover(self.cover)
        # else:
        #     pass

    def open_playlist(self, *args):
        """Open and Load an Existing Playlist."""
        pass
        # if exists("./Playlist"):
        #     showinfo(
        #         title="Pick A Playlist",
        #         message="Pick a Playlist!",
        #     )
        #     file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
        #     if file_2 == None:
        #         raise Exception("No file was chosen.")
        #     csv_file = csv.DictReader(file_2)
        #     self.now_playing_list.clear()
        #     self.current_path_dir_list.clear()
        #     for lines in csv_file:
        #         self.current_path_dir_list.append(lines["Path"])
        #         self.now_playing_list.append(lines["File_Name"])
        #     self.update_now_playing(self.now_playing_list)
        #     self.load_it(self.current_path_dir_list[0] + "/" + self.now_playing_list[0])
        #     self.get_meta(self.current_path_dir_list[0], self.now_playing_list[0])
        #     self.now_playing_song = self.now_playing_list[0]
        #     self.change_song_label(self.now_playing_song)
        #     self.update_album_cover(self.cover)
        #     self.change_pl_label(lines["PL_Name"])
        #     self.save_closing_list()
        # else:
        #     showinfo(
        #         title="Error",
        # #         message="No Playlists Available!",
        #     )

    def create_playlist(self):
        pass
    #     """Create a New Playlist."""
    #     self.new_playlist.clear()
    #     user_input = simpledialog.askstring(
    #         title="Playlist Name", prompt="Name this playlist: "
    #     )
    #     if user_input == "":
    #         showinfo(title="Title Error", message="Please Choose a Name for this list")
    #         self.create_playlist()
    #     showinfo(
    #             title="Add Songs",
    #             message="Pick Songs to Add.",
    #         )
    #     file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
    #     if file_list == []:
    #         showinfo(
    #             title="No Files",
    #             message="No files Chosen!",
    #         )
    #         #return None
    #     heads_tails = []
    #     for items in file_list:
    #         heads_tails.append(os.path.split(items))
    #     pl_name = user_input
    #     heads_tails = []
    #     for items in file_list:
    #         heads_tails.append(os.path.split(items))
    #     for (directory_1, name_1) in heads_tails:
    #         for pic in glob.glob(f"{directory_1}/*jpg"):
    #             self.cover = pic
    #             self.get_meta(directory_1, name_1)
    #             self.new_playlist.append(
    #                 dict(
    #                     PL_Name=pl_name,
    #                     Path=directory_1,
    #                     File_Name=name_1,
    #                     Title=self.title,
    #                     Artist=self.artist,
    #                     Album=self.album,
    #                     Track_Length=self.duration,
    #                     Album_Cover=self.cover,
    #                 )
    #             )
    #     data_new = pd.DataFrame(self.new_playlist)
    #     if not os.path.isdir("./Playlist"):
    #         os.makedirs("Playlist")
    #     data_new.to_csv(f"./Playlist/{pl_name}.csv", index=False)
    
    #     self.new_playlist = data_new["File_Name"].tolist()
    #     self.update_pl_editor(self.new_playlist)
    #     showinfo(
    #         title="Create Playlist Complete",
    #         message=f"You Created: {pl_name}!",
    #     )

    def add_to_playlist(self):
        """Add Songs to an Existing Playlist."""
        pass
        # self.new_playlist.clear()
        # self.editing_list.clear()
        # showinfo(
        #         title="Choose Playlist",
        #         message="Choose a Playlist You Want to Edit!",
        #     )
        # file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
        # data = pd.read_csv(file_2)
        # self.editing_list = data["File_Name"].tolist()
        # self.update_pl_editor(self.editing_list)
        # pl_name = data["PL_Name"].loc[data.index[1]]
        # showinfo(
        #         title="Songs",
        #         message="Pick Songs to Add.",
        #     )
        # file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        # heads_tails = []
        # for items in file_list:
        #     heads_tails.append(os.path.split(items))
        # for (directory_1, name_1) in heads_tails:
        #     self.editing_list.append(name_1)
        #     for pic in glob.glob(f"{directory_1}/*jpg"):
        #         self.cover = pic
        #         self.get_meta(directory_1, name_1)
        #         self.new_playlist.append(
        #             dict(
        #                 PL_Name=pl_name,
        #                 Path=directory_1,
        #                 File_Name=name_1,
        #                 Title=self.title,
        #                 Artist=self.artist,
        #                 Album=self.album,
        #                 Track_Length=self.duration,
        #                 Album_Cover=self.cover,
        #             )
        #         )
        # data_new = pd.DataFrame(self.new_playlist)
        # new_df = pd.concat([data, data_new], ignore_index=True)
        # new_df.reset_index()
        # new_df.to_csv(f"./Playlist/{pl_name}.csv", index=False)
        # fresh_data = pd.read_csv(f"./Playlist/{pl_name}.csv")
        # self.new_playlist = fresh_data["File_Name"].tolist()
        # self.update_pl_editor(self.new_playlist)
        # showinfo(
        #     title="Add To Playlist Complete",
        #     message=f"You added some sweet tracks to: {pl_name}!",
        # )

    def delete_from_playlist(self):
        """Remove Song(s) From an Existing Playlist."""
        pass
        # self.new_playlist.clear()
        # self.editing_list.clear()
        # showinfo(
        #         title="Remove",
        #         message="Choose a Playlist to Edit.",
        #     )
        # file_2 = fd.askopenfile(mode="r", filetypes=[("CSV Files", "*.csv")])
        # data = pd.read_csv(file_2)
        # self.editing_list = data["File_Name"].tolist()
        # self.update_pl_editor(self.editing_list)
        # showinfo(
        #         title="Songs",
        #         message="Choose Songs to Remove.",
        #     )
        # file_list = list(fd.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")]))
        # heads_tails = []
        # for items in file_list:
        #     heads_tails.append(os.path.split(items))
        # for (directory_1, name_1) in heads_tails:
        #     self.new_playlist.append(name_1)
        # for song in self.new_playlist:
        #     data = data[data["File_Name"] != song]
        # pl_name = data["PL_Name"].loc[data.index[1]]
        # data.to_csv(f"./Playlist/{pl_name}.csv", index=False)
        # fresh_data = pd.read_csv(f"./Playlist/{pl_name}.csv")
        # new_list = fresh_data["File_Name"].tolist()
        # self.update_pl_editor(new_list)
        # showinfo(
        #     title="Removal Complete",
        #     message=f"You removed tracks from: {pl_name}!",
        # )