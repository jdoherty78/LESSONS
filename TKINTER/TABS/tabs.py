
import tkinter as tk
from tkinter import ttk
import lorem

root = tk.Tk()
root.geometry("400x600")
root.iconbitmap("python_icon.ico")
root.title("Tabs GUI app")
root.config(bg="lightblue")

# text tab
# tab_control -> text_tab -> text_frame  ->  text_box
tab_control =  ttk.Notebook(root)
text_tab = ttk.Frame(tab_control)
tab_control.add(text_tab, text = "Text")

# text box
text_frame = tk.Frame(text_tab)
text_frame.pack(pady=30, padx=10)

text_box = tk.Text(text_frame, height=20, width =30)
text_box.pack()

# submit button
submit_btn = tk.Button(text_frame, text="Submit", height=2, width = 10)
submit_btn.config(bg="green", fg="white", font=("Arial", 10))
submit_btn.pack(pady=10)
                  
# second tab
second_tab = ttk.Frame(tab_control)
tab_control.add(second_tab, text="Second")

# labels with lorem (sentence, paragraph, text)
label = tk.Label(second_tab, text=lorem.text(), wraplength=300)
label.config(bg="pink", padx=10, pady=50)
label.pack(pady=5, padx=5)


# third tab
third_tab = ttk.Frame(tab_control)
tab_control.add(third_tab, text="Third")

tab_control.pack(fill = tk.BOTH, expand = True,
                pady = 50, padx = 10)




root.mainloop()

