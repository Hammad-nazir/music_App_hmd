from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

# Function to add songs to the playlist
def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="/home/hammad/Music", title="Choose a song", filetypes=(("MP3 Files", "*.mp3"),))
    for s in temp_song:
        # Get only the filename from the full path
        s = os.path.basename(s)
        # Check if the song is already in the list
        if s not in songs_list.get(0, END):
            songs_list.insert(END, s)
        else:
            messagebox.showinfo("Duplicate", f"{s} is already in the playlist.")

# Function to delete the selected song
def deletesong():
    curr_song = songs_list.curselection()
    if curr_song:
        songs_list.delete(curr_song[0])
    else:
        messagebox.showwarning("No Selection", "No song selected to delete")

# Function to play the selected song
def Play():
    song = songs_list.get(ACTIVE)
    if song:
        song_path = os.path.join("/home/hammad/Music", song)
        if os.path.isfile(song_path):
            mixer.music.load(song_path)
            mixer.music.play()
        else:
            messagebox.showerror("Error", "Song file not found")
    else:
        messagebox.showwarning("No Selection", "No song selected to play")

# Function to pause the song
def Pause():
    mixer.music.pause()

# Function to stop the song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

# Function to resume the song
def Resume():
    mixer.music.unpause()

# Function to navigate to the previous song
def Previous():
    try:
        current_index = songs_list.curselection()[0]
        previous_index = current_index - 1
        if previous_index < 0:
            messagebox.showwarning("No Previous Song", "No previous song available")
            return
        song = songs_list.get(previous_index)
        song_path = os.path.join("/home/hammad/Music", song)
        if os.path.isfile(song_path):
            mixer.music.load(song_path)
            mixer.music.play()
            songs_list.selection_clear(0, END)
            songs_list.activate(previous_index)
            songs_list.selection_set(previous_index)
        else:
            messagebox.showerror("Error", "Song file not found")
    except IndexError:
        messagebox.showwarning("No Previous Song", "No previous song available")

# Function to navigate to the next song
def Next():
    try:
        current_index = songs_list.curselection()[0]
        next_index = current_index + 1
        if next_index >= songs_list.size():
            messagebox.showwarning("No Next Song", "No next song available")
            return
        song = songs_list.get(next_index)
        song_path = os.path.join("/home/hammad/Music", song)
        if os.path.isfile(song_path):
            mixer.music.load(song_path)
            mixer.music.play()
            songs_list.selection_clear(0, END)
            songs_list.activate(next_index)
            songs_list.selection_set(next_index)
        else:
            messagebox.showerror("Error", "Song file not found")
    except IndexError:
        messagebox.showwarning("No Next Song", "No next song available")

# Creating the root window 
root = Tk()
root.title('HMD Music Player App')

# Initialize mixer 
mixer.init()

# Create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

# Create buttons
Button(root, text="Play", width=7, command=Play, font=defined_font).grid(row=1, column=0)
Button(root, text="Pause", width=7, command=Pause, font=defined_font).grid(row=1, column=1)
Button(root, text="Stop", width=7, command=Stop, font=defined_font).grid(row=1, column=2)
Button(root, text="Resume", width=7, command=Resume, font=defined_font).grid(row=1, column=3)
Button(root, text="Prev", width=7, command=Previous, font=defined_font).grid(row=1, column=4)
Button(root, text="Next", width=7, command=Next, font=defined_font).grid(row=1, column=5)

# Create menu 
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

root.mainloop()
