from tkinter import *
from datetime import datetime

# class handleError:
class handleError():
    def __init__(self, e, time):
        self.newWindow(e, time)

    def newWindow(self, error_message, time):
        root = Tk()
        root.geometry("400x200")
        root.geometry("400x200")
        root.resizable(True, True)
        root.title("Error")

        p1 = PhotoImage(file='error_logo.png')
        root.iconphoto(False, p1)
        label1 = Label(text='A Error Occurred')
        label1.config(font=("", 15))
        label1.pack()
        label2 = Label(text='The following error occurred')
        label2.config(font=("", 12))
        label2.pack()
        label3 = Label(text=f'{error_message}')
        label3.config(font=("", 12))
        label3.pack()
        label3 = Label(text=f'Error at {time}')
        label3.config(font=("", 12))
        label3.pack()
        canvas1 = Canvas(root)
        canvas1.pack()
        root.mainloop()

MyKeywordApp()