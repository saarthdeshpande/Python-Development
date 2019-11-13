from tkinter import *

#window and widget are two main parts of tkinter GUI


#create a window
window = Tk()

def km_to_miles():
	t1.insert(END, int(e1_value.get()) *1.6)


#add a button
b1 = Button(window, text = "Execute", command=km_to_miles)
#specify where to keep the button
b1.grid(row=0, column=0)

#add an entry

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value) 
e1.grid(row=0, column=1)

#add text box
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


#to keep the window open
window.mainloop()


