from time import strftime, localtime
from tkinter import Tk, StringVar
from tkinter.ttk import Label, Checkbutton
from playsound import playsound
import webbrowser

root = Tk()
root.title("Time Aid")

def open_url(url):
    webbrowser.open_new_tab(url)

credit_title = Label(root, font=("Arial",10,""), text="PyDing TimeAid", foreground="blue", cursor="hand2")
credit_author = Label(root, font=("Arial",10,""), text="Code by Rosier", foreground="blue", cursor="hand2")

current_time = StringVar()

DING_CONFIG = {
    0: "sounds/current/hour_00.mp3",
    15: "sounds/current/quarter_15.mp3",
    30: "sounds/current/half_30.mp3",
    45: "sounds/current/quarter_45.mp3"
}

START_TIME = 800
END_TIME = 2200
NIGHT_OWL = START_TIME > END_TIME

CHECK_RANGE = range(START_TIME, END_TIME, 5)

def ding(min):
     if min in DING_CONFIG.keys():
            playsound(DING_CONFIG[min])

def compare_time():
    current_hour = int(strftime("%H"))
    current_min = int(strftime("%M"))
    current_time = (current_hour * 100) + current_min
    if ((NIGHT_OWL and not (current_time in CHECK_RANGE)) or current_time in CHECK_RANGE) and (current_min in DING_CONFIG.keys()):
            ding(current_min)
            print(f"ding @ {current_time}")

def update_time():
    if int(strftime("%S")) == 0:
        compare_time()
    current_time.set(strftime("%I:%M:%S %p"))
    label_clock.config(textvariable=current_time)
    label_clock.after(1000, update_time)


label_clock = Label(root, font=("Monospace", 14, ""))
root.resizable(False, False)
update_time()

credit_title.grid(column=0,row=0)
label_clock.grid(column=1,row=1)
credit_author.grid(column=2,row=0)
credit_title.bind("<ButtonRelease-1>", lambda e: open_url("https://github.com/RoseAHill/pyding-timeaid"))
credit_author.bind("<ButtonRelease-1>", lambda e: open_url("https://github.com/RoseAHill"))
root.mainloop()