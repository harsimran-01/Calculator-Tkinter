from tkinter import *

window = Tk()
window.title("Tkinter-Calculator")
window.geometry("350x610")

def on_click_text(event):
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif button_text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, button_text)            



frame_1 = Frame(window, width=400, height=200, bg="#0d0c0c", borderwidth=2, relief=RAISED)
frame_1.place(x=0, y=0)

frame_2 = Frame(window, width=400, height=410, bg="#0d0c0c")
frame_2.place(x=0, y=200)

entry = Entry(frame_1, font=("Helvetica", 30), bg="#0d0c0c", fg="#00FF00", bd=0)
entry.place(x=16, y=60, width=390, height=120)

button_data = [
    ("C", 10, 10),
    ("(", 95, 10),
    (")", 180, 10),
    ("/", 265, 10),
    ("7", 10, 90),
    ("8", 95, 90),
    ("9", 180, 90),
    ("*", 265, 90),
    ("4", 10, 170),
    ("5", 95, 170),
    ("6", 180, 170),
    ("-", 265, 170),
    ("1", 10, 250),
    ("2", 95, 250),
    ("3", 180, 250),
    ("+", 265, 250),
    ("0", 10, 330),
    (".", 95, 330),
    ("=", 180, 330)
]

for text, x, y in button_data:
    button = Button(frame_2, text=text, bg="#4a4843", fg="#00FF00", font=("Helvetica", 26, "bold"), bd=0 )
    button.place(x=x, y=y, width=70, height=70)
    button.bind("<Button-1>", on_click_text)

window.mainloop()



