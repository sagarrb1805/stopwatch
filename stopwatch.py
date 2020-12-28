from tkinter import *
from PIL import Image, ImageTk
from datetime import date



root = Tk()
root.geometry("500x500")
root.title("StopWatch")
#root.protocol("WM_DELETE_WINDOW", root.iconify)

root.bind('<Escape>', lambda e: root.destroy())

img = Image.open("clock.png")
img = ImageTk.PhotoImage(img)
img_label = Label(root, image=img)
img_label.pack()

today_date = date.today()
date_label = Label(root, text=today_date, relief="solid", width=20, font=("arial", 20, "bold"), bg="grey")
date_label.place(x=76, y=220)




watch_time = "{} : {} : {}".format(00, 00, 00)
watch_label = Label(root, text=watch_time, relief="solid", width=20, bg="grey", font=("arial", 20, "bold"))
watch_label.place(x=76, y=280)

def start():
    print("start")
def stop():
    print("stop")
def restart():
    print("restart")

start_btn = Button(root, text="Start", width=12, bg="grey", fg="white", command=start)
start_btn.place(x=76, y=350)

stop_btn = Button(root, text="Stop", width=12, bg="grey", fg="white", command=stop)
stop_btn.place(x=328, y=350)

restart_btn = Button(root, text="Restart", width=12, bg="grey", fg="white", command=restart)
restart_btn.place(x=203, y=350)


root.mainloop()




