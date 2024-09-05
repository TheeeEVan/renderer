from colors import *
from config import *
from object import Object
import os
import pygame
import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
# this hides main tk window
root.withdraw()

# ask user for file (this will be the object that is opened)
path = filedialog.askopenfilename(initialdir=os.getcwd() + "/objects", title="Select Object to Open", filetypes=[("python object", "*.pyobj")])

# if no file selected quit
if not path:
    messagebox.showerror("Error", "No File Selected")
    quit()

root.destroy()

# open pygame window
display = pygame.display.set_mode(SCREEN_SIZE)

# main class
class Renderer():
    def __init__(self):
        # set object to be the file that was selected
        self.object = Object(path)

    def update(self):
        self.object.update()
        
    def draw(self):
        display.fill(BLACK)
        self.object.draw(display)

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

renderer = Renderer()
clock = pygame.time.Clock()

while True:
    renderer.eventHandler()
    renderer.update()
    renderer.draw()
    pygame.display.update()
    clock.tick(30)
