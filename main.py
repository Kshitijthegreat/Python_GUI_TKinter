import tkinter as tk
from tkinter import filedialog
import os

apps = []


# Define a function to save app list in a text file
def save():
    global apps
    file = open('save.txt', 'w')
    for app in apps:
        file.write(app + '\n')


def clrsv():
    file = open('save.txt', 'w')
    file.write('')
    for widget in frame.winfo_children():
        widget.destroy()
    for app in apps:
        local_label = tk.Label(frame, text=app, bg='gray')
        local_label.pack()
    createbuttons()
    return 0


# Define a function to retreive all saved apps
def retr():
    global apps
    file = open('save.txt', 'r')
    apps_ = []
    for line in file:
        apps_.append(line.replace('\n', ''))
        print(line)
    apps = apps_
    for widget in frame.winfo_children():
        widget.destroy()
    for app in apps:
        local_label = tk.Label(frame, text=app, bg='gray')
        local_label.pack()
    createbuttons()
    return 0


# Define function exitap to exit the app. Called by a Button
def exitap():
    quit(0)
    return 0


# Define function to run the selected apps. Called by a Button
def run():
    global apps
    for app in apps:
        os.startfile(app)
    return 0


# Define function to Add apps. Called by a Button.
def addap():
    # clear the screen
    for widget in frame.winfo_children():
        widget.destroy()
    # open file dialogue
    file = filedialog.askopenfilename(initialdir='C:/Users/User/Desktop', title='select file',
                                      filetypes=(('executable', '*.exe'), ('all files',     '*.*')))
    global apps
    # Add selected apps to list 'apps'
    apps.append(file)
    # Display selected apps
    for app in apps:
        local_label = tk.Label(frame, text=app, bg='gray')
        local_label.pack()
    createbuttons()
    return None


# Define function to clear app list. Called by a button
def clearap():
    global apps
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()
    createbuttons()
    return 0


# Define root
root = tk.Tk()

# Make a canvas
canvas = tk.Canvas(root, height=500, width=500, bg='#0000ff')
canvas.pack()

# Make a frame
frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# Make a help label
label = tk.Label(frame, text='To add apps, click button \'Add App\'. \n To Run apps, click button \'Run Apps\'.')
label.pack()


# Define function to create buttons
def createbuttons():
    addapp = tk.Button(frame, text="Add app", padx=10, pady=10, fg='white', bg='#00ff00', command=addap)
    addapp.pack()

    # Define button to run apps
    runapp = tk.Button(frame, text='Run app', padx=10, pady=10, fg='white', bg='#00ff00', command=run)
    runapp.pack()

    # Define button to clear app list
    clearlist = tk.Button(frame, text='Clear app list', padx=10, pady=10, fg='white', bg='#00ff00', command=clearap)
    clearlist.pack()

    # Define a button to retreive saved apps
    retrap = tk.Button(frame, text='Retreive saved app list', padx=10, pady=10, fg='white', bg='#00ff00', command=retr)
    retrap.pack()

    # Define a button to save app list
    save_apps = tk.Button(frame, text='Save app list', padx=10, pady=10, fg='white', bg='#00ff00', command=save)
    save_apps.pack()

    # Define button to clear saved apps
    clrsvap = tk.Button(frame, text='Clear saved app list', padx=10, pady=10, fg='white', bg='#00ff00', command=clrsv)
    clrsvap.pack()
    
    # Define button to exit app
    exitbutton = tk.Button(frame, text='Exit', padx=10, pady=10, fg='white', bg='#00ff00', command=exit)
    exitbutton.pack()


# call createbuttons
createbuttons()
# call mainloop
tk.mainloop()
