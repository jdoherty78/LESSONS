import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("350x600")
root.title("Event GUI app")
root.iconbitmap("python_icon.ico")
root.config(bg = "lightgreen")

def submit():
    print("Submit")
    text_var = text.get("1.0", tk.END).strip()
    print(text_var)
    if text_var != "" and len(text_var) > 5:
        print("saved info")
        messagebox.showinfo("Thank you", "Submitted Successfully!")

    else:
        messagebox.showerror("Error", "Text box cannot be empty!")

def clear_text():
    text.delete("1.0", tk.END)

def hover_enter(event):
    event.widget.config(cursor="hand2")
    btn.config(bg="dodgerblue")

def hover_leave(event):
    event.widget.config(cursor="")
    btn.config(bg="orange")

def toggle_bg(event):
    key = event.keysym
    bg = root.cget("bg")  # light green
    print(key)
    if key == "0" and bg != "pink":
        root.config(bg = "pink")
    else:
        root.config(bg="lightgreen")
        
        

#### TEXT AREA
text = tk.Text(root, width = 40, height = 20)
text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
text.config(bg="pink", borderwidth=5)

#### CLEAR BUTTON
btn = tk.Button(root, text="Clear", command=clear_text)
btn.config(bg="orange", fg="black", padx=10, pady=10, borderwidth=5)
btn.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#### SUBMIT BUTTON
submit_btn = tk.Button(root, text="SUBMIT", command=submit)
submit_btn.config(bg="blue", font=("Arial", 15), fg="white", height=5, width=20)
submit_btn.grid(row=5, column=0, columnspan=3, padx=20, pady=20)


btn.bind("<Enter>", hover_enter)
btn.bind("<Leave>", hover_leave)

root.bind("<Key>", toggle_bg)

# run ze application
root.mainloop()