import tkinter

window = tkinter.Tk()
# above creates the window
# space below is for your code
window.title("Hello World")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# .pack() places object on the screen and centers it.
my_label.pack()
# below are two methods for changing the text of my_label
my_label["text"] = "New text"
my_label.config(text="new tecxt2")

# Entry
input = tkinter.Entry(width=30)
input.insert(index=1, string="Theres some stuff here.")
input.pack()


# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Text
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert()
# gets current value in textbox on line 1, character 0
print(text.get("1.0", END))

# Spinbox
def spinbox_used():
    #get value from spinbox and print it
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # print 1 is on button checked and 0 otherwise
    print(checked_state.get())


# variable to hold onto the checked state, 0 for off and 1 for on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# below makes the window appear and listens for user inputs
window.mainloop()
