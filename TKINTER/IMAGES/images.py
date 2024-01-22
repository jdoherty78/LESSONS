import tkinter as tk
from PIL import ImageTk, Image
import webbrowser, os


# main window

root = tk.Tk()
root.title("Image GUI app")
root.geometry("600x750")
root.config(bg="grey")
root.iconbitmap("python_icon.ico")

# image URLS + website urls
image_list = ["pigeon1.jpg", "pigeon2.jpg", "pigeon3.jpg"]
website_urls = ["https://www.python.org",
               "https://www.openai.com",
               "https://www.google.com"]
image_labels = ["Maddox - The Angry Bird",
               "Jennifer - The Friendly",
               "Izzy - Keeping Busy"]
folder = "my_images"


# open websites function
def open_website_func(url):
    print(url)
    webbrowser.open(url)

# create imagetk objects for each image

images = []
for url in image_list:
    full_url = folder + os.sep + url
    image = Image.open(full_url)
    img = image.resize((200,200))  # resizing images
    image_tk = ImageTk.PhotoImage(img)
    images.append(image_tk)

# create labels for each image

labels = []
for i, image_tk in enumerate(images):
    label = tk.Label(root, image = image_tk)
    label.pack()
    labels.append(label)

    # add event to each label
    website_url = website_urls[i]
    label.bind("<Button-1>", lambda a, url=website_url:
open_website_func(url))
    
    # add labels
    text_label = tk.Label(root, text = image_labels[i])
    text_label.pack()

# create a styled title label

title_label = tk.Label(root, text="Pigeons are Shit Hawks",
                       font=("Arial", 16, "bold"), pady=10)
title_label.place(y = 680, x = 180)

# function to handle image click event

root.mainloop()
