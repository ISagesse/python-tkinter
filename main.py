import tkinter

def button_clicked():
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)

#button
button = tkinter.Button(text="Click ME", command=button_clicked)
button.grid(column=1, row=1)

bt = tkinter.Button(text="New Button")
bt.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()