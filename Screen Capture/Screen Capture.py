import pyautogui
from tkinter import *
import tkinter as tk
from PIL import ImageTk ,Image
from tkinter import filedialog

bg_color='black'

#root = Tk()
root= tk.Tk()
root.geometry('250x200')

root.configure(background=bg_color)
root.title('Screen Capture')


photo = tk.PhotoImage(file='image\\sss.png')
                                                                 

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

#myButton = tk.Button(root,  image=photo, command = takeScreenshot, font= 10)

myButton = tk.Button(root, image = photo, bg = bg_color, compound = "center", command = takeScreenshot)
myButton.grid(row=0,column=0,padx=50, pady=50)

myButton.pack() 

root.mainloop()