from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry("500x500")
root.title("StopWatch")


img = Image.open("clock.png")
img = ImageTk.PhotoImage(img)

img_label = Label(image=img)
img_label.pack()


root.mainloop()

