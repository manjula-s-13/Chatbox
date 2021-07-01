
def connecting():

    def newscrn():

        def voice():

            def combine():
                reply=str(txtmsgs.get())
                csock.send(bytes(reply, "utf-8"))
                w=len(reply)
                w=(w*13)+10
                txtmsgs.delete(0, END)
                global j
                global s
                if (j<600):
                    screen.update()
                    lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                    lab.place(x=355,y=j,height=45,width=w)
                    s.append(lab)
                    screen.update()
                    j=j+70
                    return s
                    return j
                else:
                    for k in range(0, 7 ):
                        foo=s.pop()
                        foo.destroy()   
                    j=110
                    lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                    lab.place(x=355,y=j,height=45,width=w)
                    s.append(lab)
                    screen.update()
                    j=j+70


            
            r=sr.Recognizer()
            global response
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                audio=r.listen(source)
                response=StringVar()
                response=r.recognize_google(audio)

            txtmsgs=Entry(screen,font=("times new roman",20) , bd=2 , relief=RAISED)
            txtmsgs.insert(0,response)
            txtmsgs.place(x=58,y=615, height=50 , width=547)

            sendbtns2=Button(screen, image=sendbtn ,relief=RIDGE , bd=5, command=combine)
            sendbtns2.place(x=605 , y=610)


        def going():
            opinion=messagebox.askokcancel('Notification','Are you sure to EXIT..?', parent=screen)
            if opinion==True:
                screen.destroy()
                csock.send(bytes('Your friend has disconnected...', "utf-8"))
                csock.close()
                
            else:
                return 0
                
        def onclick(event):
            txtmsg.configure(state=NORMAL)
            txtmsg.delete(0, END)

        def combined():
            reply=str(txtmsg.get())
            csock.send(bytes(reply, "utf-8"))
            w=len(reply)
            w=(w*13)+10
            txtmsg.delete(0, END)
            global j
            global s
            if (j<600):
                screen.update()
                lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                lab.place(x=355,y=j,height=45,width=w)
                s.append(lab)
                screen.update()
                j=j+70
                return s
                return j
            else:
                for k in range(0, 7 ):
                    foo=s.pop()
                    foo.destroy()   
                j=110
                lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                lab.place(x=355,y=j,height=45,width=w)
                s.append(lab)
                screen.update()
                j=j+70
#*************************************************************************CONNECTING CLASS*********************************************************************************

        class ThreadingExample:

            def __init__(self,screen,i,labels):
                self.screen=screen
                self.i=i
                self.labels=labels
                thread = threading.Thread(target=self.run, args=[i,labels])
                thread.daemon = True                           
                thread.start()                         

            def run(self,i,labels):
                self.msg=csock.recv(buf)
                self.data=(self.msg).decode('utf-8')
                w=len(self.data)
                w=(w*13)+10
                if (i<600):
                    screen.update()
                    self.lab=Label(screen,text=self.data,font=('times new roman',20),relief=RIDGE,bg="honeydew" , fg="black",bd=3)
                    self.lab.place(x=25,y=i,height=45,width=w)
                    self.labels.append(self.lab)
                    screen.update()
                    i=i+70
                    screen.after(10000,self.run(i,labels))
                else:
                    for k in range(0, 7):
                        foo=self.labels.pop()
                        foo.destroy()   
                    i=110
                    self.lab=Label(screen,text=self.data,font=('times new roman',20),relief=RIDGE,bg="honeydew" , fg="black",bd=3)
                    self.lab.place(x=25,y=i,height=45,width=w)
                    self.labels.append(self.lab)
                    screen.update()
                    i=i+70
                    screen.after(10000,self.run(i,labels))
#************************************************************************NEWSCREEN*******************************************************************************************************root.destroy()
        root.destroy()
        screen=tkinter.Tk()
        screen.geometry("661x670+650+10")
        screen.resizable(0,0)
        screen.title("CHAT APP")
        bckgrnd=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\Untitled1.png'))
        lab1=Label(screen,image=bckgrnd)
        lab1.place(x=0,y=0)

        frnd=data.capitalize()
        frndname=Label(screen,text=frnd,font=("times new roman",30,'bold','italic'),relief=RIDGE,bg='whitesmoke',fg='navy',borderwidth=3)
        frndname.place(x=0,y=0,width=661,height=60)

        dp=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\dp.png'))
        lab2=Label(screen,image=dp)
        lab2.place(x=2,y=3)

        exitbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\exit.png'))
        exitbtn2=Button(screen, image=exitbtn, command=going )
        exitbtn2.place(x=600,y=0)
        
        txtmsg=Entry(screen,font=("times new roman",20) , bd=2 , relief=RAISED)
        txtmsg.insert(0,"Type a message")
        txtmsg.configure(state=DISABLED)
        txtmsg.bind("<Button>",onclick)
        txtmsg.place(x=58,y=615, height=50 , width=547)

        sendbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\snd.png'))
        sendbtn2=Button(screen, image=sendbtn ,relief=RIDGE , bd=5, command=combined)
        sendbtn2.place(x=605 , y=610)

        recbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\rec.png'))
        recbtn2=Button(screen, image=recbtn ,relief=RIDGE , bd=5, command=voice)
        recbtn2.place(x=0 , y=613)

        example=ThreadingExample(screen,110,[])

        screen.mainloop()

#***********************************************************************CONNECTING********************************************************************************************
    
    host=ipentry.get()
    port=13000
    addr=(host,port)
    buf=1024
    csock=socket(AF_INET,SOCK_STREAM)
    try:
        csock.connect((host,port))
        messagebox.showinfo('Notification',"Let's begin...!! " , parent=root)
        frnd1=str(friend.get())
        csock.send(bytes( frnd1 , "utf-8"))
        time.sleep(3)
        msg=csock.recv(buf)
        data = msg.decode('utf-8')
        frnd1=str(friend.get())
        newscrn()
    except:
        messagebox.showerror('Error','Failed to connect')
        ipentry.delete(0, END)
    
        
        
    
###*****************************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************    

def standby():

    def newscrn():

        def voice():

            def combine():
                reply=str(txtmsgs.get())
                csock.send(bytes(reply, "utf-8"))
                w=len(reply)
                w=(w*13)+10
                txtmsgs.delete(0, END)
                global j
                global s
                if (j<600):
                    screen.update()
                    lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                    lab.place(x=355,y=j,height=45,width=w)
                    s.append(lab)
                    screen.update()
                    j=j+70
                    return s
                    return j
                else:
                    for k in range(0, 7 ):
                        foo=s.pop()
                        foo.destroy()   
                    j=110
                    lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                    lab.place(x=355,y=j,height=45,width=w)
                    s.append(lab)
                    screen.update()
                    j=j+70


            
            r=sr.Recognizer()
            global response
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                audio=r.listen(source)
                response=StringVar()
                response=r.recognize_google(audio)

            txtmsgs=Entry(screen,font=("times new roman",20) , bd=2 , relief=RAISED)
            txtmsgs.insert(0,response)
            txtmsgs.place(x=58,y=615, height=50 , width=547)
            sendbtns2=Button(screen, image=sendbtn ,relief=RIDGE , bd=5, command=combine)
            sendbtns2.place(x=605 , y=610)
        

        def going():
            opinion=messagebox.askokcancel('Notification','Are you sure to EXIT ', parent=screen)
            if opinion==True:
                screen.destroy()
                csock.send(bytes('Your friend has disconnected...', "utf-8"))
                csock.close()
                
            else:
                return 0
                

        def onclick(event):
            txtmsg.configure(state=NORMAL)
            txtmsg.delete(0, END)

        def combined():
            reply=str(txtmsg.get())
            csock.send(bytes(reply , "utf-8"))
            w=len(reply)
            w=(w*13)+10
            txtmsg.delete(0, END)
            global j
            global s
            if (j<600):
                screen.update()
                lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                lab.place(x=355,y=j,height=45,width=w)
                s.append(lab)
                screen.update()
                j=j+70
                return s
                return j
            else:
                for k in range(0, 7 ):
                    foo=s.pop()
                    foo.destroy()   
                j=110
                lab=Label(screen,text=reply,font=('times new roman',20),relief=RIDGE,bg="lightyellow" , fg="black",bd=3)
                lab.place(x=355,y=j,height=45,width=w)
                s.append(lab)
                screen.update()
                j=j+70
#************************************************************************************STANDBY CLASS************************************************************************

        class ThreadingExample:

            def __init__(self,screen,i,labels):
                self.screen=screen
                self.i=i
                self.labels=labels
                thread = threading.Thread(target=self.run, args=[i,labels])
                thread.daemon = True                           
                thread.start()                         

            def run(self,i,labels):
                self.msg=csock.recv(buf)
                self.data=(self.msg).decode('utf-8')
                w=len(self.data)
                w=(w*13)+10
                if (i<600):
                    screen.update()
                    self.lab=Label(screen,text=self.data,font=('times new roman',20),relief=RIDGE,bg="honeydew" , fg="black",bd=3)
                    self.lab.place(x=25,y=i,height=45,width=w)
                    self.labels.append(self.lab)
                    screen.update()
                    i=i+70
                    screen.after(10000,self.run(i,labels))
                else:
                    for k in range(0, 7):
                        foo=self.labels.pop()
                        foo.destroy()   
                    i=110
                    self.lab=Label(screen,text=self.data,font=('times new roman',20),relief=RIDGE,bg="honeydew" , fg="black",bd=3)
                    self.lab.place(x=25,y=i,height=45,width=w)
                    self.labels.append(self.lab)
                    screen.update()
                    i=i+70
                    screen.after(10000,self.run(i,labels))

##*************************************************************************NEWSCREEN****************************************************************************************************************************        

        root.destroy()
        screen=tkinter.Tk()
        screen.geometry("661x670+650+10")
        screen.resizable(0,0)
        screen.title("CHAT APP")
        bckgrnd=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\Untitled1.png'))
        lab1=Label(screen,image=bckgrnd).place(x=0,y=0)
                           
        frnd2=data.capitalize()
        frndname=Label(screen,text=frnd2,font=("times new roman",30,'bold','italic'),relief=RIDGE,bg='whitesmoke',fg='navy',borderwidth=3)
        frndname.place(x=0,y=0,width=661,height=60)


        dp=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\dp.png'))
        lab2=Label(screen,image=dp)
        lab2.place(x=2,y=3)

        exitbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\exit.png'))
        exitbtn2=Button(screen, image=exitbtn , command=going )
        exitbtn2.place(x=600,y=0)

        txtmsg=Entry(screen,font=("times new roman",20), bd=2 , relief=RAISED)
        txtmsg.insert(0,"Type a message")
        txtmsg.configure(state=DISABLED)
        txtmsg.bind("<Button>",onclick)
        txtmsg.place(x=58,y=615, height=50 , width=547)

        sendbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\snd.png'))
        sendbtn2=Button(screen, image=sendbtn ,relief=RIDGE , bd=5, command=combined)
        sendbtn2.place(x=605 , y=610)

        recbtn=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\rec.png'))
        recbtn2=Button(screen, image=recbtn ,relief=RIDGE , bd=5, command=voice)
        recbtn2.place(x=0 , y=613)

        example=ThreadingExample(screen,110,[])

        screen.mainloop()

##*************************************************************************STANDBY***********************************************************************************************************************

    
    
    host=""
    port=13000
    addr=(host,port)
    buf=1024
    ssock=socket(AF_INET,SOCK_STREAM)
    ssock.bind(addr)
    ssock.listen(1)
    (csock,host)=ssock.accept()
    messagebox.showinfo('Notification','You are now connected...!!' , parent=root)
    msg=csock.recv(buf)
    data = msg.decode('utf-8')
    time.sleep(3)
    frnd1=str(friend.get())
    csock.send(bytes( frnd1 , "utf-8"))
    newscrn()
    
            
#*******************************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************************    

def on_click(event):
    ipentry.configure(state=NORMAL)
    ipentry.delete(0, END)
def on_clicks(event):
    nameentry.configure(state=NORMAL)
    nameentry.delete(0, END)

#########################################################################################################################################################################################
#*************************************************************MAINPROGRAM********************************************************************************************************

import os,socket
from socket import *
import tkinter
from tkinter import *
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import time
import threading
import speech_recognition as sr
from speech_recognition import *

j=110
s=[]
root = tkinter.Tk()
root.geometry("661x670+650+10")
root.title("CHAT APP")
root.resizable(0,0)
photo = ImageTk.PhotoImage(Image.open("C:\\Users\\padmakumari\\Pictures\\chatapp.png"))
root.iconphoto(True, photo)

image1= ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\Untitled.png'))
panel=Label(root,image=image1)
panel.place(x=0,y=0)

nameheading=Label(root,text=" USERNAME " , font=("Algerian",25),bg="grey", relief=RAISED, borderwidth=5)
nameheading.place(x=100 ,y=45 )

friend=StringVar()
nameentry=Entry(root,textvariable=friend, font=("Times New Roman",20) , bg="azure" , bd=5 , relief=RAISED)
nameentry.insert(0,"FRIEND")
nameentry.configure(state=DISABLED)
nameentry.bind("<Button>",on_clicks)
nameentry.place(x=260 ,y=115 , height=50 , width=350)

ipheading=Label(root,text="  ENTER IP ADDRESS  " , font=("Algerian",25), bg="grey" , relief=RAISED ,  borderwidth=5)
ipheading.place(x=100,y=215)
root.wm_attributes("-transparentcolor" , "grey")

ipentry=Entry(root, font=("Times New Roman",20) , bg="azure" , bd=5 , relief=RAISED)
ipentry.insert(0,"IP ADDRESS")
ipentry.configure(state=DISABLED)
ipentry.bind("<Button>",on_click)
ipentry.place(x=260,y=285 , height=50 , width=350)

connect=ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Pictures\\connect.png'))
connectbtn=Button(root, image=connect ,   command=connecting).place(x=180 , y=400 )

waiting=Button(root,text="WAITING FOR CONNECTION..." , font=("Times New Roman bold italic",20) , bg="white" ,  borderwidth=5 , relief=RAISED , command=standby)
waiting.place(x=40,y=550)


root.mainloop()
