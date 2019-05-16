from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led1=LED(14)
led2=LED(15)
led3=LED(3)


### GUI DEFINITIONS ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
num=IntVar()

### Event Functions ###
def ledToggle():
    led1.off()
    led2.off()
    led3.off()
    if num.get()==1:
        led1.on()
    if num.get()==2:
        led2.on()
    if num.get()==3:
        led3.on()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()



### WIDGETS ###

# Button, triggers the connected command when it is pressed
ledButton1 = Radiobutton(win, text='LED1', font=myFont, command=ledToggle, bg='bisque2', variable=num, value=1)
ledButton1.grid(row=0,column=1)
ledButton2 = Radiobutton(win, text='LED2', font=myFont, command=ledToggle, bg='bisque2', variable=num, value=2)
ledButton2.grid(row=1,column=1)
ledButton3 = Radiobutton(win, text='LED3', font=myFont, command=ledToggle, bg='bisque2', variable=num, value=3)
ledButton3.grid(row=2,column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever