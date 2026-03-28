from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# label
my_label = Label(text="My label", font=("Arial", 24, "bold"))
my_label["text"] = "ahoj ty kare"
my_label.config(text="cau kare 2")

my_label.grid(column=0, row=0)

# button
def button_clicked():
    my_label.config(text=tk_input.get())

button_1 = Button(text="Click me", command=button_clicked)
button_1.grid(column=1, row=1)

button_2 = Button(text="Don't click me")
button_2.grid(column=2, row=0)

# entry
tk_input = Entry(width=10)
tk_input.get()
tk_input.grid(column=3, row=2)




window.mainloop()