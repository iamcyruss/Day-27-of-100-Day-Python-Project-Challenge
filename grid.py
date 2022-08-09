from tkinter import *


window = Tk()
window.title("Yo")
window.minsize(width=500, height=300)

my_label = Label(text="Hello world")
my_label.grid(column=2, row=5)

window.mainloop()
