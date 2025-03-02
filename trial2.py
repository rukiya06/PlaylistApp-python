import tkinter as tk
from tkinter import messagebox
import pygame
import pywhatkit
import os
import random

class PlaylistApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Playlist App")

        self.playlist = []

        self.track_entry = tk.Entry(master)
        self.track_entry.pack()

        self.add_button = tk.Button(master, text="Add Track", command=self.add_track)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Remove Track", command=self.remove_track)
        self.remove_button.pack()

        self.play_button = tk.Button(master, text="Play Track", command=self.play_track)
        self.play_button.pack()

        self.playlist_label = tk.Label(master, text="Playlist:")
        self.playlist_label.pack()

        self.playlist_text = tk.Text(master, height=10, width=60)
        self.playlist_text.pack()

        self.playlist_text.tag_configure("sel",background="yellow")
        self.playlist_text.tag_add("sel","1.0","end")

        self.shuffle_button=tk.Button(master,text="Shuffle Playlist",command=self.shuffle_playlist)
        self.shuffle_button.pack()

    def add_track(self):
        track = self.track_entry.get()
        if track:
            self.playlist.append(track)
            self.update_playlist_display()

    def remove_track(self):
        track = self.track_entry.get()
        if track in self.playlist:
            self.playlist.remove(track)
            self.update_playlist_display()

    def update_playlist_display(self):
        self.playlist_text.delete("1.0", tk.END)
        for index, track in enumerate(self.playlist, start=1):
            self.playlist_text.insert(tk.END, f"{index}. {track}\n")

    def play_track(self):
        current_index = self.playlist_text.get(tk.SEL_FIRST,tk.SEL_LAST)
        if not current_index.strip():
            messagebox.showerror("Error","Please select a track from the playlist")
            return
        pywhatkit.playonyt(current_index)
        self.playlist_text.tag_configure("sel",background="yellow")

    def update_playlist_display(self):
        self.playlist_text.delete("1.0",tk.END)
        for index, track in enumerate(self.playlist,start=1):
            self.playlist_text.insert(tk.END,f"{index}.{track}\n","sel")

    def shuffle_playlist(self):
        random.shuffle(self.playlist)
        self.update_playlist_display()
def main():
    root = tk.Tk()
    try:
        app = PlaylistApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred:{e}")

if __name__ == "__main__":
    main()
