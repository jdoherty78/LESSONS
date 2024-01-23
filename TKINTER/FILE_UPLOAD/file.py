import tkinter as tk   
from tkinter import filedialog   #accessing files in a folder
import os, shutil  # displaying files
from PIL import Image  # PIL handling upload 

root = tk.Tk()
root.iconbitmap("python_icon.ico")
root.title("File GUI app")
root.geometry("500x300")
root.config(bg="grey")

ext_tup = (".jpg", ".jpg", ".png", ".gif")

IMAGE_FOLDER = "uploaded_images"
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

# FUNCTIONS

# CREATE & POSITION ELEMENTS

# UPLOAD BUTTON

# LISTBOX_FRAME

# LISTBOX and SCROLLBAR

# OPEN BUTTON

# HANDLE ERRORS

# CREATE IMAGE FOLDER IF IT DOES NOT EXIST

root.mainloop()
