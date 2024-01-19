import tkinter as tk

def open_third_window():
    print("open third window!")  # end here for only cli output
    third_window = tk.Toplevel()
    third_window.title("Third window")
    third_window.geometry("300x300")
    third_window.iconbitmap("python_icon.ico")
    third_window.config(bg="pink")

    btn_third_window = tk.Button(third_window, text="Close Window",
                                 command = third_window.destroy)
    btn_third_window.pack()
    btn_third_close_all = tk.Button(third_window, text="Close ALL",
                                 command = third_window.quit)
    btn_third_close_all.pack()

def open_new_window():
    print("Open Window")
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry("200x200")
    new_window.iconbitmap("python_icon.ico")
    new_window.config(bg="grey")

    btn_window = tk.Button(new_window, text="Open 3rd Window",
                           command = open_third_window)
    btn_window.pack()
    btn_second_window = tk.Button(new_window, text="Close",
                                  command=new_window.destroy)     # new_window.quit  <-- closes all windows
    btn_second_window.pack()

# create main window
window = tk.Tk()
window.geometry("300x500")
window.title("Multiple Windows Example")
window.iconbitmap("python_icon.ico")


btn1 = tk.Button(window, text="Open New Window", command=open_new_window)
btn1.config(bg="grey", fg="red", font=("Helvetica", 20))

btn2 = tk.Button(window, text="Close Window", command=window.destroy)
btn2.config(bg="purple", fg="white", font=("Helvetica", 20))

btn1.pack(pady=10, padx=10)
btn2.pack(pady=10, padx=10)


# run the app

window.mainloop()

