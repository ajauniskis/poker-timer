from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import pygame

root = Tk()
root.title('Poker timer')
root.iconbitmap('icon.ico')
root.geometry('400x200')

# configure resize
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)

# declare time variables
minute = StringVar()
second = StringVar()
# set default value to 0
minute.set('00')
second.set('00')

# configure blind change sound
pygame.init()
pygame.mixer.music.load('timer.mp3')

# declare blinds
blinds = [[25,50], [50,100], [100, 200], [150, 300], [200,400], [250,500], [300,600], [400,800], [500,1000], [600,1200], [700,1400], [800,1600], [900,1800], [1000,2000]]


def start():
    global blinds
    global start_min
    global start_sec
    global running
    start_min = minute.get()
    start_sec = second.get()
    try:
        temp = int(minute.get())*60 + int(second.get())
    except:
        # ignore entry errors
        return
    button_start['state']=DISABLED
    #button_pause['state']=NORMAL
    #button_stop['state']=NORMAL
    
    for b in blinds:
        temp = int(start_min)*60 + int(start_sec)
        label_blinds['text'] = 'Current blinds {} / {}'.format(b[0], b[1])

        while temp >= 0:
            mins,secs = divmod(temp,60)

            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the temp value every time
            root.update()
            time.sleep(1)
            
            # after every one sec the value of temp will be decremented by one
            temp -= 1
        pygame.mixer.music.play()

    # when temp value = 0; then a messagebox pop's up with a message:"Time's up"
    messagebox.showinfo("Poker Timer", "Time's up ")

def pause():
    return

def stop():
    return

# configure text label
textLabel = Label(root, text='Choose round length')
textLabel.grid(row=0, column=0, columnspan=12)

# configure logo
img = ImageTk.PhotoImage(Image.open('logo.png'))
logo = Label(image=img)
logo.grid(row=0, column=13, rowspan=4)

# configure entry
e_min = Entry(root, borderwidth=2, textvariable=minute)
e_min.grid(row=1, column=0, columnspan=3)

e_sec = Entry(root, width=6, borderwidth=2, textvariable=second)
e_sec.grid(row=1, column=6, columnspan=3)

# configure time labels
label_min = Label(root, text='minutes')
label_min.grid(row=1, column=3, columnspan=3)
label_sec = Label(root, text='seconds')
label_sec.grid(row=1, column=9, columnspan=3)

# configure blinds label
label_blinds = Label(root, text='')
label_blinds.grid(row=2, column = 0, columnspan=12)
label_blinds.config(font=(None, 12, 'bold'))

# configure time buttons
button_start = Button(root, text='Start', padx=15, pady=10, command=lambda: start() if int(minute.get())*60 + int(second.get()) > 0 else False)
button_start.grid(row=3, column=0, columnspan=4)

button_pause = Button(root, text='Pause', padx=15, pady=10, command=pause, state=DISABLED)
button_pause.grid(row=3, column=4, columnspan=4)

button_stop = Button(root, text='Stop', padx=15, pady=10, command=stop, state=DISABLED)
button_stop.grid(row=3, column=8, columnspan=4)

root.resizable(False, False)
root.mainloop()