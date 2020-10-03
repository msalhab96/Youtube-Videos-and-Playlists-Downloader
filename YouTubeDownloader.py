#this file works well !
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import youtube_dl
import threading
import time 
background_color = "#398ca3"
text_color = "#fedf00"
button_color = "#e6e2d5"
folder_selected = ""

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def Exit():
    win.destroy()
def Min():
    win.state('iconic')
def Res():
    win.state('normal')
    #print("save result")

def how():
    win.state('normal')
    #print("how")

def about():
    win.state('normal')
    #print("about")

def contact():
    msg = messagebox.showinfo('Contacts','Done By: Mahmoud A. Salhab\n \nEmail: mahmoud@salhab.work \nFaceBook: facebook.com/msalhab96')

def clear():
    Link.set("")
    warning.set("")
    des.set("")

def select_dir():
    bt_download.configure(state = "normal")
    global folder_selected
    folder_selected = filedialog.askdirectory()
    des.set(folder_selected)

def dow():
    global t
    t = StoppableThread(target = downlaod)  
    t.start()

def progress():
    print(t.is_alive())

    while t.is_alive():

        delay = 1
        warning.set("Downloading")
        if not(t.is_alive()):
            warning.set("")
            break
        time.sleep(delay)
        warning.set(warning.get()+'.')
        if not(t.is_alive()):
            warning.set("")
            break
        time.sleep(delay)
        warning.set(warning.get()+'.')
        if not(t.is_alive()):
            warning.set("")
            break
        time.sleep(delay)
        warning.set(warning.get()+'.')
        if not(t.is_alive()):
            warning.set("")
            break
        time.sleep(delay)
        warning.set(warning.get()+'.')
        if not(t.is_alive()):
            warning.set("")
            break
        time.sleep(delay)
        
        print(t.is_alive())
        

        
def p():
    print("GGH")
def downlaod():

    if Link.get() == "":
        warning.set("Please Try again!")
    else:
        warning.set("")
        
        try:
            if variable.get() == youtube_type[0]:
                t3 = StoppableThread(target = progress)
                t3.start()
                ydl_opts = {'outtmpl': (folder_selected+"\\%(title)s.%(ext)s")}
                youtube_dl.YoutubeDL(ydl_opts).download([Link.get()])
                msg = messagebox.showinfo('Completed','Your Video has successfully Downloaded')
                warning.set("")

            if variable.get() == youtube_type[1]:
                downloading_condition = False
                t3 = StoppableThread(target = progress)
                t3.start()
                ydl_opts = {'outtmpl': (folder_selected+"\\%(title)s.%(ext)s")}
                youtube_dl.YoutubeDL(ydl_opts).download([Link.get()])
                msg = messagebox.showinfo('Completed','Your Video has successfully Downloaded')
                downloading_condition = True
                warning.set("")
        except:
            warning.set("Please Try again!")
            msg = messagebox.showerror('ERROR','ERROR,\nPlease Try Later!')
            downloading_condition = True
        


youtube_type = ['Video',
                'PlayList']

win = Tk()
win.configure(bg = background_color,)
win.maxsize(width = 540 , height = 260)
win.minsize(width = 540 , height = 260)
win.title('YouTube Downloader')
win.iconbitmap('icon.ico')

############ variables ##########
variable = StringVar()
des = StringVar()
Link = StringVar()
warning = StringVar()
variable.set(youtube_type[0])
############ menu ############
mu = Menu(win)
file_mu = Menu(mu)
mu.add_cascade(label='File' , menu = file_mu)
file_mu.add_command(label = 'Minimize' , command = Min)
file_mu.add_command(label = 'Exit', command = Exit)
help_mu = Menu(mu)
mu.add_cascade(label='Help' , menu = help_mu )
help_mu.add_command(label = 'How to use it', command = how)
help_mu.add_command(label = 'Contacts', command = contact)

############ picking the type ############
L_Type = Label(win , text= "Type:" , font=("Trebuchet MS" , 12 , 'bold'),bg = background_color,fg = text_color, )
L_Type.place(x = 35 , y = 35)

w = OptionMenu(win , variable , *youtube_type , )
w.config(width=8, font=('Trebuchet MS', 12) )

w.place(x = 90 , y = 32)

############ Link entery ############
pos = 90
L_Type = Label(win , text= "Link:" , font=("Trebuchet MS" , 12 , 'bold'), bg = background_color, fg = text_color,)
L_Type.place(x = 35 , y = pos)

e1 = Entry(win , width = 45 ,textvariable = Link, font = ("Arial" , 12))
e1.place(x = 90, y = pos + 3)  

bt_clear = Button(win , command = clear ,  text = " Clear Link Field " , font = ("Trebuchet MS" , 12), )
bt_clear.place(x = 205 , y = 145)

############ select directory ############

B_Dir = Button(win , text = "Select a Folder" , command = select_dir , font = ("Trebuchet MS" , 12 ) )
B_Dir.place(x = 35 , y = 145)

############ Download button ############
bt_download = Button(win , command = dow , state=DISABLED , text = " Download " , font = ("Trebuchet MS" , 12 , "bold"))
bt_download.place(x = 395 , y = 145)

############ warning Label and location ############
L_Warning = Label(win , text= "" , textvariable = warning, font=("Trebuchet MS" , 13), bg = background_color,fg = text_color, )
L_Warning.place(x = 210 , y = 200)

L_Dir= Label(win , text= "" , textvariable = des, font=("Trebuchet MS" , 11),bg = background_color, fg = text_color, )
L_Dir.place(x = 10 , y = 225)
############ Teh End Of the window ############
win.config(menu = mu)
win.mainloop()
