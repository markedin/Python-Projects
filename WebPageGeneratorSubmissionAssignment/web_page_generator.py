


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")


        #create label for entry
        self.lbl_customText = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        #place label in correct grid spot
        self.lbl_customText.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+E)
        #create entry for custom text
        self.entry_customText = Entry(width=120)
        #place entry for custom text in correct grid spot
        self.entry_customText.grid(row=2, column=0, columnspan=4, padx=(20,10), pady=(10,10))
        #create default HTML page button
        self.btn_defaultHTML = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #place default HTML page button in correct grid spot
        self.btn_defaultHTML.grid(row=3, column=2, padx=(10,10), pady=(10, 10))
        #create submit custom text button
        self.btn_submitCustom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        #place submit custom text button in correct grid spot
        self.btn_submitCustom.grid(row=3, column=3, padx=(10,10), pady=(10, 10))

    #create a default html function
    def defaultHTML(self):
        #create default text 
        htmlText = "Stay tuned for our amazing summer sale!"
        #'open' an html file to write our text to 
        htmlFile = open("index.html", "w")
        #write htmlText in an h1 element of the index.html page
        htmlContent = ("<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>")
        #write the actual html text
        htmlFile.write(htmlContent)
        #clocse the file connection
        htmlFile.close()
        #open the webpage
        webbrowser.open_new_tab("index.html")

    #create a custom html function
    def customHTML(self):
        #get the text written in the entry and store it in htmlText
        htmlText = self.entry_customText.get()
        #do the exact same thing as the defaultHTML function
        htmlFile = open("index.html", "w")
        htmlContent = ("<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>")
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
