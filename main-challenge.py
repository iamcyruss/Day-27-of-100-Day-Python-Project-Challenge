from tkinter import *

window = Tk()
window.title(string="Day 27 Challenge")
window.minsize(width=500, height=500)
window.config(padx=150, pady=150)

entry = Entry()
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label1 = Label()
label1.config(text="Miles")
label1.grid(column=2, row=0)

label2 = Label()
label2.config(text="is about")
label2.grid(column=0, row=1)

label3 = Label()
label3.config(text="0")
label3.grid(column=1, row=1)

label4 = Label()
label4.config(text="Km")
label4.grid(column=3, row=1)


def button_clicked():
    new_text = entry.get()
    miles_to_km = int(new_text) * 1.6
    label3.config(text=str(int(miles_to_km)))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
