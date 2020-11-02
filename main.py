import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []


def exit():
    quit(0)
    return None


def Addapp():
    for widget in frame.winfo_children():
        widget.destroy()

    file = filedialog.askopenfilename(initialdir='C:/Users/User/Desktop', title='select file',
                                      filetypes=(('executable', '*.exe'), ('all files', '*.*')))
    global apps
    apps.append(file)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()
    return None


def Runapp():
    for app in apps:
        os.startfile(app)
    return None


root = tk.Tk()
root.state('normal')
canvas = tk.Canvas(root, height=500, width=500, bg='#263d42')
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

addapp = tk.Button(root, text="Add app", padx=10, pady=10, fg='white', bg='#00ff00', command=Addapp)
addapp.pack()
runapp = tk.Button(root, text='Run app', padx=10, pady=10, fg='white', bg='#00ff00', command=Runapp)
# os.startfile(apps[0])
runapp.pack()
exitbutton = tk.Button(root, text='Exit', padx=10, pady=10, fg='white', bg='#00ff00', command=exit)
exitbutton.pack()
root.mainloop()
