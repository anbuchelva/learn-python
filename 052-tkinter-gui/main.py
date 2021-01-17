from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Label
label = Label(text="This is some text")
label.grid(column=0, row=0)

# Button
button = Button(text="This is a button")
button.grid(column=1, row=1)

# New Button
new_button= Button(text="A new Button")
new_button.grid(column=2, row=0)

# Entry
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="sample text")
entry.grid(column=3, row=3)

window.mainloop()

