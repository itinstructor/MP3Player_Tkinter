"""
    Name: mp3_player_pygame.py
    Author: William A Loring
    Created: 12/17/21
    Purpose: Browse for and play mp3 files
"""
# History
# ------------------------------------------------
# Author     Date           Comments
# Loring     12/17/2021       Initial creation


from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog  # Browsing for files
from pygame import mixer        # Play songs
import os                       # Working with file path
import time                     # Display length of song


class PlayMP3:
    def __init__(self):
        # Initialize the pygame mixer and volume
        mixer.init()
        mixer.music.set_volume(0.70000)

        # Define window
        self.root = Tk()
        self.root.title("Play Mp3")
        self.root.geometry('450x250')
        self.root.iconbitmap("note.ico")
        self.root.resizable(0, 0)
        self.create_widgets()
        # Start tkinter main program loop
        mainloop()

#------------------------------- PLAY SONG -----------------------------#
    def play_song(self, *args):
        """ Play song """
        # Load the song
        mixer.music.load(self.file_name)

        # Create Sound object containing the mp3 file
        sound = mixer.Sound(self.file_name)

        # Get the length of the song, convert it into time format
        length = time.strftime("%H:%M:%S", time.gmtime(
            mixer.Sound.get_length(sound)))

        # Set the initial volume
        volume = mixer.music.set_volume(0.70000)

        # Play the song asychronously
        mixer.music.play()
        self.lbl_length.configure(text=f"{length}")
        self.lbl_file_name.configure(text=f" Playing: {self.mp3_filename}")

#------------------------------- PAUSE SONG -----------------------------#
    def pause(self):
        # Pause sound
        mixer.music.pause()
        self.lbl_file_name.configure(text=f" Paused: {self.mp3_filename}")

#------------------------------- RESUME SONG -----------------------------#
    def resume(self):
        # Unpause sound
        mixer.music.unpause()
        self.lbl_file_name.configure(text=f" Playing: {self.mp3_filename}")

#------------------------ STOP SONG PLAYBACK -----------------------------#
    def stop(self):
        # Stop sound
        mixer.music.stop()
        self.lbl_file_name.configure(text=f" Stopped: {self.mp3_filename}")

#------------------------------- INCREASE VOLUME -----------------------------#
    def increase_volume(self):
        # TODO: Increase and decrease volume are too complicated
        volume = mixer.music.get_volume()
        mixer.music.set_volume(volume + .10000)
        volume = mixer.music.get_volume()
        volume = (round(volume * 10)) * 10
        self.lbl_volume.configure(text=f"Volume: {volume} %")

#------------------------------- DECREASE VOLUME -----------------------------#
    def decrease_volume(self):
        # TODO: Increase and decrease volume are too complicated
        volume = mixer.music.get_volume()
        mixer.music.set_volume(volume - .10000)
        volume = mixer.music.get_volume()
        volume = (round(volume * 10)) * 10
        self.lbl_volume.configure(text=f"Volume: {volume} %")

#------------------------------- BROWSE FILES -----------------------------#
    def browse_files(self):
        self.file_name = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a File",
            filetypes=(("Mp3 files",
                        "*.mp3*"),
                       ("all files",
                        "*.*")))

        # Split the filename from the absolute path
        self.mp3_filename = os.path.split(self.file_name)[1]

        # Display the name of the mp3 file
        self.lbl_file_name.configure(
            text=f" File Opened: {self.mp3_filename}")

#------------------------------- BROWSE FILES -----------------------------#
    def create_widgets(self):
        # Create input and output frames
        self.open_mp3_frame = LabelFrame(
            self.root,
            text="Open Mp3",
            borderwidth=2,
            relief=GROOVE)

        self.play_frame = LabelFrame(
            self.root,
            text="Play Mp3",
            borderwidth=2,
            relief=GROOVE)

        self.volume_frame = LabelFrame(
            self.root,
            text="Volume",
            borderwidth=2,
            relief=GROOVE)

        # Fill the frame to the width of the window
        self.open_mp3_frame.pack(fill=X)
        self.play_frame.pack(fill=X)
        self.volume_frame.pack(fill=X)
        # Keep the frame size regardless of the widget sizes
        self.open_mp3_frame.pack_propagate(False)
        self.play_frame.pack_propagate(False)
        self.volume_frame.pack_propagate(False)

        btn_open_mp3 = Button(
            self.open_mp3_frame, text="Open Mp3", command=self.browse_files)
        self.lbl_file_name = Label(
            self.open_mp3_frame, text=" No file open", relief=GROOVE, anchor=W, width=45)
        btn_play = Button(
            self.play_frame, text="Play", command=self.play_song)
        btn_pause = Button(
            self.play_frame, text="Pause", command=self.pause)
        btn_resume = Button(
            self.play_frame, text="Resume", command=self.resume)
        btn_stop = Button(
            self.play_frame, text="Stop", command=self.stop)
        btn_increase_volume = Button(
            self.volume_frame, text="Increase Volume", command=self.increase_volume)
        btn_decrease_volume = Button(
            self.volume_frame, text="Decrease Volume", command=self.decrease_volume)
        self.lbl_volume = Label(self.volume_frame, text="Volume: 70 %")
        self.lbl_length = Label(self.volume_frame)

        btn_open_mp3.grid(row=0, column=0)
        self.lbl_file_name.grid(row=0, column=1)
        btn_play.grid(row=0, column=0)
        btn_pause.grid(row=0, column=1)
        btn_resume.grid(row=0, column=2)
        btn_stop.grid(row=0, column=3)
        btn_increase_volume.grid(row=0, column=0)
        btn_decrease_volume.grid(row=0, column=1)
        self.lbl_volume.grid(row=0, column=2)
        self.lbl_length.grid(row=0, column=3)

        self.open_mp3_frame.pack_configure(padx=10, pady=(10, 0))
        self.play_frame.pack_configure(padx=10, pady=10)
        self.volume_frame.pack_configure(padx=10, pady=(0, 10))
        for child in self.open_mp3_frame.winfo_children():
            child.grid_configure(padx=7, pady=7, ipadx=3, ipady=3)
        for child in self.play_frame.winfo_children():
            child.grid_configure(padx=7, pady=7, ipadx=3, ipady=3)
        for child in self.volume_frame.winfo_children():
            child.grid_configure(padx=7, pady=7, ipadx=3, ipady=3)

        # The enter key will activate the play method
        self.root.bind('<Return>', self.play_song)


#------------------------- START MAIN PROGRAM -----------------------------#
# Create object, start main program
play_mp3 = PlayMP3()
