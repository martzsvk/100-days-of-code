from tkinter import *

window = Tk()
window.title("Mile to kilometers converter")
window.minsize(width=400, height=200)
window.config(padx=25, pady=20)

# function for mile to km conversion
def mile_to_km():
    result = int(miles_input.get()) * 1.609344
    miles_label.config(text=f"Miles is equal to {round(result, 2)} Km")

# input
miles_input = Entry(width=10)
miles_input.get()
miles_input.place(x=25, y=10)

# label
miles_label = Label(text=f"Miles is equal to 0 Km ", font=("Arial", 15, "bold"))
miles_label.place(x=100, y=5)

# button
button = Button(text="Calculate", command=mile_to_km)
button.place(x=138, y=40)


window.mainloop()