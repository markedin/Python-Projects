

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta
import time

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #creates button to select files from source directory
        self.sourceDir_btn = Button(text = "Select Source", width=20, command=self.sourceDir)
        #positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10),pady=(30,0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))
        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text = "Select Destination", width=20, command=self.destDir)
        #positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row =1, column=0, padx=(20,10), pady=(15,10))

        #creates entry for destination directory selection
        self.destination_dir=Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creats button to transfer files
        self.transfer_btn = Button(text = "Transfer Files", width=20, command = self.transferFiles)
        #positions transfer files btn
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #create exit btn
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #position exit btn
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #creates a function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #creats function to select destination dircetory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir entry widget
        self.destination_dir.insert(0, selectDestDir)


    #create function to check if file is less than 24 hours old, return a boolean
    def checkFileAge(self, file_path):
        #get time when path was last changed since epoch (UNIX)
        mod_time = os.path.getmtime(file_path)
        #get difference from curret time in seconds since epoch
        diff_time = time.time() - mod_time
        #convert to hours
        dt_hours = diff_time / 360
        #return conditions
        if dt_hours <= 24:
            return True
        else:
            return False
    
    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #get source dir
        source = self.source_dir.get()
        #get dest dir
        destination = self.destination_dir.get()
        #get list of files in the source dir
        source_files = os.listdir(source)
        #runs thru each file in source dir
        for i in source_files:
            #moves each files from source dir to dest dir if they are less than 24 hours old
            if self.checkFileAge(source + '/' + i):
                shutil.move(source + '/' + i, destination)
                print(i + ' was transferred successfully.')
            else:
                print(i + ' was not transferred because it is older than 24 hours.')

    #create function to exit program
    def exit_program(self):
        #root is main GUI window, use destroy()
        root.destroy()










        






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
