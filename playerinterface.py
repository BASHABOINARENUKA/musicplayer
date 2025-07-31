
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from musicplayer import DoublyLinkedList
# import pygame
# from PIL import Image, ImageTk
# import os

# class MusicPlayerGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Music Player")
#         self.root.geometry("600x400")
#         self.root.configure(bg="black")

#         pygame.mixer.init()
#         pygame.mixer.music.set_endevent(pygame.USEREVENT)

#         self.playlist = DoublyLinkedList()

#         # Load background
#         bg_image = Image.open("music.jpg")
#         # bg_image = bg_image.resize((600, 400), Image.ANTIALIAS)
#         bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)

#         self.bg_photo = ImageTk.PhotoImage(bg_image)

#         self.bg_label = tk.Label(self.root, image=self.bg_photo)
#         self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Load icons
#         self.icons = {
#             "play": ImageTk.PhotoImage(Image.open("play.png").resize((40, 40))),
#             "pause": ImageTk.PhotoImage(Image.open("pause.png").resize((40, 40))),
#             "next": ImageTk.PhotoImage(Image.open("fast-forward.png").resize((40, 40))),
#             "prev": ImageTk.PhotoImage(Image.open("rewind-button.png").resize((40, 40))),
#             "add": ImageTk.PhotoImage(Image.open("add.png").resize((25, 25))),
#             "delete": ImageTk.PhotoImage(Image.open("bin.png").resize((25, 25))),
#             "display": ImageTk.PhotoImage(Image.open("display-frame.png").resize((25, 25))),
#         }

#         # Right-side buttons
#         tk.Button(self.root, image=self.icons["display"], command=self.display_playlist, bd=0, bg="white").place(x=550, y=10)
#         tk.Button(self.root, image=self.icons["add"], command=self.add_song, bd=0, bg="white").place(x=550, y=50)
#         tk.Button(self.root, image=self.icons["delete"], command=self.delete_song, bd=0, bg="white").place(x=550, y=90)

#         # Bottom control buttons
#         tk.Button(self.root, image=self.icons["prev"], command=self.prev_song, bd=0, bg="white").place(x=200, y=330)
#         self.play_button = tk.Button(self.root, image=self.icons["play"], command=self.toggle_play_pause, bd=0, bg="white")
#         self.play_button.place(x=270, y=330)
#         tk.Button(self.root, image=self.icons["next"], command=self.next_song, bd=0, bg="white").place(x=340, y=330)

#         self.is_playing = False

#     def add_song(self):
#         file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
#         if file_path:
#             self.playlist.append(file_path)
#             messagebox.showinfo("Added", f"{os.path.basename(file_path)} added to playlist.")

#     def delete_song(self):
#         if self.playlist.current:
#             deleted = os.path.basename(self.playlist.current.data)
#             self.playlist.delete(self.playlist.current.data)
#             pygame.mixer.music.stop()
#             messagebox.showinfo("Deleted", f"{deleted} removed from playlist.")
#         else:
#             messagebox.showwarning("Warning", "No song selected to delete.")

#     def toggle_play_pause(self):
#         if self.is_playing:
#             self.playlist.pause()
#             self.play_button.config(image=self.icons["play"])
#             self.is_playing = False
#         else:
#             self.playlist.play_current()
#             self.play_button.config(image=self.icons["pause"])
#             self.is_playing = True

#     def next_song(self):
#         self.playlist.next()
#         self.play_button.config(image=self.icons["pause"])
#         self.is_playing = True

#     def prev_song(self):
#         self.playlist.previous()
#         self.play_button.config(image=self.icons["pause"])
#         self.is_playing = True

#     def display_playlist(self):
#         current = self.playlist.head
#         songs = []
#         while current:
#             songs.append(os.path.basename(current.data))
#             current = current.next
#         messagebox.showinfo("Playlist", "\n".join(songs) if songs else "Playlist is empty.")

# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MusicPlayerGUI(root)
#     root.mainloop()

import tkinter as tk
from tkinter import filedialog
from musicplayer import DoublyLinkedList
import pygame
from PIL import Image, ImageTk
import os

class MusicPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("600x400")

        pygame.mixer.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        self.playlist = DoublyLinkedList()

        # Load and set background image
        bg_image = Image.open("music.jpg")
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load icons
        self.icons = {
            "add": ImageTk.PhotoImage(Image.open("add.png").resize((25, 25))),
            "delete": ImageTk.PhotoImage(Image.open("bin.png").resize((25, 25))),
            "display": ImageTk.PhotoImage(Image.open("display-frame.png").resize((25, 25))),
            "prev": ImageTk.PhotoImage(Image.open("rewind-button.png").resize((30, 30))),
            "play": ImageTk.PhotoImage(Image.open("play.png").resize((30, 30))),
            "next": ImageTk.PhotoImage(Image.open("fast-forward.png").resize((30, 30)))
        }

        # Buttons (Right side)
        tk.Button(self.root, image=self.icons["display"], bg="white", command=self.display_playlist).place(x=570, y=10)
        tk.Button(self.root, image=self.icons["add"], bg="white", command=self.add_song).place(x=570, y=60)
        tk.Button(self.root, image=self.icons["delete"], bg="white", command=self.delete_song).place(x=570, y=110)

        # Controls (Bottom)
        tk.Button(self.root, image=self.icons["prev"], bg="white", command=self.play_prev).place(x=200, y=350)
        tk.Button(self.root, image=self.icons["play"], bg="white", command=self.play_pause).place(x=270, y=350)
        tk.Button(self.root, image=self.icons["next"], bg="white", command=self.play_next).place(x=340, y=350)

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)

    def delete_song(self):
        if self.playlist.current:
            self.playlist.delete(self.playlist.current.data)

    def play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            self.playlist.play_current()

    def play_next(self):
        self.playlist.next()

    def play_prev(self):
        self.playlist.previous()

    def display_playlist(self):
        display_win = tk.Toplevel(self.root)
        display_win.title("Playlist")
        display_win.geometry("300x400")
        display_win.configure(bg="purple")

        tk.Label(display_win, text="Current Playlist", font=("Arial", 14, "bold"), bg="purple", fg="white").pack(pady=10)

        listbox = tk.Listbox(display_win, bg="white", fg="black", width=40, height=20)
        listbox.pack(pady=10)

        node = self.playlist.head
        while node:
            listbox.insert(tk.END, os.path.basename(node.data))
            node = node.next

if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayerGUI(root)
    root.mainloop()
