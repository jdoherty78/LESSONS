import tkinter as tk   
from tkinter import filedialog   #accessing files in a folder
import os, shutil  # displaying files
from PIL import Image  # PytonImageLibrary handling upload 

root = tk.Tk()
root.iconbitmap("python_icon.ico")
root.title("File GUI app")
root.geometry("500x300")
root.config(bg="grey")

ext_tup = (".jpg", ".jpg", ".png", ".gif")  # image extensions only

IMAGE_FOLDER = "uploaded_images"
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

# FUNCTIONS

def upload_image():
    file_paths = filedialog.askopenfilenames()
    #print(file_paths)       prints to cli for testing
    for file_path in file_paths:
        # check if file is an image
        if file_path.endswith(ext_tup):
            # check file size
            if os.path.getsize(file_path) <= MAX_FILE_SIZE:
                # COPY IMAGE FILE
                image_name = os.path.basename(file_path)
                destination = os.path.join(IMAGE_FOLDER, image_name)
                shutil.copyfile(file_path, destination)
                # add the file path to the listbox
                listbox.insert(tk.END, image_name) 
                error_label.config(text = "", bg="grey")
            else:
                error_label.config(bg="white", text = "File size exceeds limit.")
        else:
            error_label.config(bg="white", text = "Invalid File Format.")


def open_image():
    selection = listbox.curselection()
    #print(selection, selection[0])       prints to cli for testing
    if selection:
        image_name = listbox.get(selection[0])
        image_path = os.path.join(IMAGE_FOLDER, image_name)
        image = Image.open(image_path)
        image.show()

# CREATE & POSITION ELEMENTS

# UPLOAD BUTTON

upload_btn = tk.Button(root, text="Upload Image", command= upload_image)
upload_btn.pack()



# LISTBOX_FRAME

listbox_frame = tk.Frame(root)
listbox_frame.pack(fill=tk.BOTH, expand = True)

# SCROLL BAR

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side = tk.RIGHT, fill=tk.Y)

# LISTBOX and SCROLLBAR

listbox = tk.Listbox(listbox_frame, yscrollcommand= scrollbar.set)
listbox.pack(side = tk.LEFT, fill=tk.BOTH, expand = True)
scrollbar.config(command=listbox.yview)

# OPEN BUTTON

open_btn = tk.Button(root, text="Open Image", command= open_image)
open_btn.pack()

# HANDLE ERRORS
error_label = tk.Label(root, fg="red", bg="grey")
error_label.config(text = "")
error_label.pack()

# CREATE IMAGE FOLDER IF IT DOES NOT EXIST

if not os.path.exists(IMAGE_FOLDER):
    os.mkdir(IMAGE_FOLDER)
    
# DISPLAY FILES IN DIR, IN THE LISTBOX

for file in os.listdir(IMAGE_FOLDER):
    image_name = os.path.basename(file)
    listbox.insert(tk.END, image_name)

root.mainloop()
