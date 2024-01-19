import tkinter as tk

root = tk.Tk()
root.geometry("400x600")
root.title("First GUI app")
root.iconbitmap("python_icon.ico")
root.config(bg="lightblue")

label1 = tk.Label(root, text="Programming Languages")
label1.config(bg="pink", fg = "red", font = ("Arial", 20),
             relief = "groove", borderwidth = 10,
             pady = 20, padx = 5)

label1.pack()

# relief = (groove, raise, ridge, solid)

label2 = tk.Label(root, text="My favorite language is: ")
label2.config(bg="blue", fg="white", font=("Times-Roman", 15),
              relief = "ridge", borderwidth=2,
              pady = 10, padx = 10)

label2.place(y = 470)

label3 = tk.Label(root, text="Pick a language")
label3.config(bg="grey", fg="white", font=("Courier", 15),
              borderwidth=5, pady = 5, padx = 5, relief = "solid")
label3.place(y = 520)


languages = ["python", "javascript", "css", "html", "sql"]

def btn_lang(lang="no language"):
    print(lang)
    label3.config(text=lang)
    
for i in range(len(languages)):
    lang_text = languages[i]
    btn = tk.Button(root, text=lang_text.upper(), width = 100,
                   command = lambda lang = lang_text: btn_lang(lang))
    btn.config(bg="green", fg="white", font=("Courier", 15),
              relief="ridge", borderwidth=2,
              pady = 10, padx = 10)
    btn.pack(pady = 10)


root.mainloop()
