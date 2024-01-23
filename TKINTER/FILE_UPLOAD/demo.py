import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import shutil

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB
IMAGE_FOLDER = "uploaded_images"

def upload_image():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            # Check if the file is an image
            if file_path.endswith((".jpg", ".jpeg", ".png", ".gif")):
                # Check file size
                if os.path.getsize(file_path) <= MAX_FILE_SIZE:
                    # Copy the file to the image folder
                    image_name = os.path.basename(file_path)
                    destination = os.path.join(IMAGE_FOLDER, image_name)
                    shutil.copyfile(file_path, destination)
                    # Add the file path to the listbox
                    listbox.insert(tk.END, image_name)
                    error_label.config(text = "", bg="grey")
                else:
                    error_label.config(bg="white", text="File size exceeds the limit.")
            else:
                
                error_label.config(bg="white", text="Invalid file format.")

def open_image():
    selection = listbox.curselection()
    if selection:
        image_name = listbox.get(selection[0])
        image_path = os.path.join(IMAGE_FOLDER, image_name)
        image = Image.open(image_path)
        image.show()

# Create the main window
window = tk.Tk()

# Set window title, geometry, background color, and icon
window.title("Image Uploader")
window.geometry("500x300")
window.config(bg="grey")
window.iconbitmap("python_icon.ico")

# Create and position the elements
upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

listbox_frame = tk.Frame(window)
listbox_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

error_label = tk.Label(window, fg="red", bg = "grey")
error_label.config(text = "")
error_label.pack()

# Create the image folder if it doesn't exist
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)
    
for file in os.listdir(IMAGE_FOLDER):
    
    image_name = os.path.basename(file)
    destination = os.path.join(IMAGE_FOLDER, image_name)
    listbox.insert(tk.END, image_name)




# Run the main loop
window.mainloop()
