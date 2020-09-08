import pygame
from tkinter import *
root = Tk()
pygame.init()
def play():
    pygame.mixer.music.load("example.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
Button(root,text="Play",command=play).pack()
root.mainloop()