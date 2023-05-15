# Python Ver: 3.10.11
#
# Author: Mark Edin
#
# Purpose: Phonebook applicatoin. Demonstrating OOP, TKinter GUI module,
#           using TKinter parent and child relationship
#
# Tested OS: Developed and tested in Windows 10



from tkinter import *
from tkinter import messagebox
import tkinter as tk


#Importing other modules to have access to them
import phonebook_gui
import phonebook_func

#Inheriting from TKinter frame class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500, 300)

        #Center window method will center app on user screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("TKinter PhoneBook")
        self.master.configure(bg="#F0F0F0")
        #This method catches if user clicks x in top right of window
        self.master.protocol("WM_DELETE_WINDOW", lambda:phonebook_func.ask_quit(self))
        arg = self.master

        #load in GUI widgets from seperate module
        phonebook_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
