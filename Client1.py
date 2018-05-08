#client

from Tkinter import *

def windows():

    bgcolor = "#4d2177"

    #Window Part
    global window
    window = Tk()
    window.title("Nasir")
    window.minsize(width=500, height=600)
    window.maxsize(width=500, height=600)

    #Frame Part
    global frame
    frame = Frame(window, width=500, height=600, bg=bgcolor)
    frame.pack()

    #Intro Part
    global profile_name
    profile_name = Label(frame, bg=bgcolor, fg="white", text="[ Nasir Khan ]", font=("Helvetica 15 bold"))
    profile_name.place(x=170, y=10)

    Online1_name = Label(frame, bg=bgcolor, fg="white", text="Tanvir Rahman", font=("Helvetica 12 bold"))
    Online1_name.place(x=18, y=50)
    Online2_name = Label(frame, bg=bgcolor, fg="white", text="Anis Likhon", font=("Helvetica 12 bold"))
    Online2_name.place(x=18, y=80)

    #button1_green = Button(frame, bg="green", font=("Helvetica 12 bold"))
    #button1_green.place(x=180, y=58, height=10, width=10)
    global button1
    global button2
    button1 = Button(frame, bg="red", font=("Helvetica 12 bold"))
    button1.place(x=200, y=58, height=10, width=10)

    #button2_green = Button(frame, bg="green", font=("Helvetica 12 bold"))
    #button2_green.place(x=180, y=88, height=10, width=10)
    button2 = Button(frame, bg="red", font=("Helvetica 12 bold"))
    button2.place(x=200, y=88, height=10, width=10)

    #Text Area Part
    global textarea
    textarea_label = Label(frame, bg=bgcolor, fg="white", text="Friends Message :", font=("Helvetica 15 bold"))
    textarea_label.place(x=18, y=120)

    textarea = Text(frame, font=("Helvetica", 13))
    textarea.place(x=20, y=150, height=250, width=455)
    scrollbar = Scrollbar(window, command=textarea.yview)
    textarea['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=462, y=150, height=250)

    #Text Box Part
    global textbox
    textbox_label = Label(frame, bg=bgcolor, fg="white", text="Enter Your Message :", font=("Helvetica 12 bold"))
    textbox_label.place(x=18, y=420)

    textbox = Entry(frame, font=("Helvetica", 12))
    textbox.place(x=20, y=450, height=50, width=460)

    #Button Part
    global button
    button = Button(frame, bg="#34af23", fg="white", text="SEND", font=("Helvetica 12 bold"), command=lambda: ClickAction())
    button.place(x=380, y=530, height=35, width=100)

    #LogOut Button
    global logout_button
    logout_button = Button(frame, bg="#e50914", fg="white", text="LOGOUT", font=("Helvetica 12 bold"), command=lambda: LogOut())
    logout_button.place(x=20, y=530, height=35, width=100)


def LogOut():
    textarea.configure(state='normal')
    textarea.insert(END, "\n" + "Nasir: " + "Disconnected")
    textarea.configure(state='disabled')
    disconnected = "Nasir Disconnected"
    sock.sendall(disconnected)
    window.destroy()
    sock.close()
    t1.stop()
    t2.stop()
    

    
def ClickAction():

    message = textbox.get()
    if message !="":
        print ("Nasir: " + message)
        send()
        textarea.configure(state='normal')
        textarea.insert(END, "\n" + "Nasir: " + message)
        textarea.configure(state='disabled')
        textbox.delete(0, END)


######### Socket Part ##############

from threading import Thread
import time
from socket import *
from Tkinter import *
from tkFileDialog import askopenfilename

sock = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 5001

####################################

########## Input Part ##############
try:
    sock.connect((host, port))
    print "Client Connection Established..."
    textarea.insert(END, "\n" + "Client Connection Established..." + "\n")
except:
    print ""

def send():
    message = textbox.get()
    sock.sendall(message)
    time.sleep(0.5)

def comapareString(s1,s2):
    set1 = set(s1.split(' '))
    set2 = set(s2.split(' '))

    if (set1 == set2) == True:
        return 1
    else:
        return 0


def recv():
    while True:
        data = sock.recv(4096)
        print "-->" + data + "\n"

        if data == "Tanvir is Online":
            button1 = Button(frame, bg="green", font=("Helvetica 12 bold"))
            button1.place(x=200, y=58, height=10, width=10)
            
        if data == "Anis is Online":
            button2 = Button(frame, bg="green", font=("Helvetica 12 bold"))
            button2.place(x=200, y=88, height=10, width=10)

        if data == "Tanvir Disconnected":
            button1 = Button(frame, bg="red", font=("Helvetica 12 bold"))
            button1.place(x=200, y=58, height=10, width=10)
            
        if data == "Anis Disconnected":
            button2 = Button(frame, bg="red", font=("Helvetica 12 bold"))
            button2.place(x=200, y=88, height=10, width=10)


        textarea.configure(state='normal')
        textarea.insert(END, "\n" + data)
        textarea.configure(state='disabled')
        time.sleep(0.5)


windows()
t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()
window.mainloop()
