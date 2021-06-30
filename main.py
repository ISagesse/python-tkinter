import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

#button
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click ME", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()