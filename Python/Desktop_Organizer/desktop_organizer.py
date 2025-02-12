# IMPORT LIBRARIES
import tkinter as tk
from tkinter import messagebox, filedialog
from os import scandir, rename, path, getenv
from os.path import exists, join, splitext
from shutil import move
import logging

# INFO MESSAGE LOG CONFIGURATION
logging.basicConfig(level=logging.INFO)

# DEFINE INITIAL DIRECTORY VARIABLES (UPDATED via GUI)
source_dir = ""
dest_dir_documents = ""
dest_dir_images = ""
dest_dir_music = ""
dest_dir_sfx = ""
dest_dir_videos = ""

# SUPPORTED FILE TYPES and DESTINATION DIRECTORIES
file_types = {
    "audios": [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"],
    "documents": [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".rtf"],
    "images": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
              ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt",
              ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"],
    "videos": [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov",
              ".qt", ".flv", ".swf", ".avchd"]
}

# FUNCTION to GENERATE a UNIQUE FILE NAME if CONFLICT ARISES
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

# Function to move files to the appropriate directory
def move_file(dest, entry, name):
    if exists(join(dest, name)):
        name = make_unique(dest, name)
    move(entry.path, join(dest, name))

# FUNCTION to SCAN and PROCESS FILES in the SOURCE DIRECTORY
def on_organizer():
    with scandir(source_dir) as entries:
        for entry in entries:
            if entry.is_file():
                process_file(entry)

# FUNCTION to DETERMINE DESTINATION DIRECTORY BASED on FILE TYPE and SIZE
def process_file(entry):
    name = entry.name
    for category, extensions in file_types.items():
        for extension in extensions:
            if name.lower().endswith(extension):
                dest = determine_destination(category, entry)
                move_file(dest, entry, name)
                logging.info(f"Moved {category} file: {name}")
                return

# FUNCTION to DETERMINE APPROPRIATE DESTINATION DIRECTORY for a FILE
def determine_destination(category, entry):
    if category == "audios":
        if entry.stat().st_size < 10_000_000 or "SFX" in entry.name:
            return dest_dir_sfx
        else:
            return dest_dir_music
    return globals()[f"dest_dir_{category}"]

# FUNCTION to RUN the ORGANIZER and UPDATE DIRECTORY VARIABLES
def run_organizer():
    global source_dir, dest_dir_sfx, dest_dir_music, dest_dir_videos, dest_dir_images, dest_dir_documents
    source_dir = source_dir_entry.get()
    dest_dir_documents = documents_dir_entry.get()
    dest_dir_images = images_dir_entry.get()
    dest_dir_music = music_dir_entry.get()
    dest_dir_sfx = sfx_dir_entry.get()
    dest_dir_videos = videos_dir_entry.get()

    on_organizer()
    messagebox.showinfo("Done", "File organization complete!")

# FUNCTION to OPEN DIRECTORY SELECTION DIALOG and SET SELECTED DIRECTORY in the ENTRY WIDGET
def select_directory(entry_widget, initial_directory=None):
    directory = filedialog.askdirectory(initialdir=initial_directory)
    if directory:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, directory)

# CREATE GUI
window = tk.Tk()
window.title('Desktop Organizer')
window.geometry('530x375')

# CONFIGURE GRID to be RESPONSIVE
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)
window.grid_columnconfigure(1, weight=1)

# TITLE
title_label = tk.Label(
    master=window,
    text='Desktop Organizer',
    font=['Arial', 30, 'bold']
)
title_label.grid(row=0, columnspan=3, pady=20, sticky='n')

# FUNCTION to CREATE DIRECTORY w/ LABEL and BROWSE BUTTON
def create_directory_input(label_text, entry_widget, row, initial_directory=None):
    label = tk.Label(window, text=label_text)
    label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
    entry_widget.grid(row=row, column=1, padx=10, pady=5, sticky='ew')
    browse_button = tk.Button(window, text="Browse", command=lambda: select_directory(entry_widget, initial_directory))
    browse_button.grid(row=row, column=2, padx=5, pady=5, sticky='w')

# GET PATH TO DESKTOP DIRECTORY
desktop_directory = path.join(getenv('HOME'), 'Desktop')

# CREATE ENTRY WIDGETS for DIRECTORIES
source_dir_entry = tk.Entry(window, width=30)
documents_dir_entry = tk.Entry(window, width=25)
images_dir_entry = tk.Entry(window, width=25)
music_dir_entry = tk.Entry(window, width=25)
sfx_dir_entry = tk.Entry(window, width=25)
videos_dir_entry = tk.Entry(window, width=25)

# CREATE DIRECTORY INPUTS w/ APPROPRIATE LABELS and INITIAL DIRECTORIES
create_directory_input("Source Directory:", source_dir_entry, 1, desktop_directory)
create_directory_input("Documents:", documents_dir_entry, 2)
create_directory_input("Images:", images_dir_entry, 3)
create_directory_input("Music:", music_dir_entry, 4)
create_directory_input("SFX:", sfx_dir_entry, 5)
create_directory_input("Videos:", videos_dir_entry, 6)

# ADD BUTTON to RUN "ORGANIZE" SCRIPT
organize_button = tk.Button(
    window,
    text="Organize",
    command=run_organizer
)
organize_button.grid(row=7, columnspan=3, pady=20, sticky='n')

# RUN APPLICATION
window.mainloop()
