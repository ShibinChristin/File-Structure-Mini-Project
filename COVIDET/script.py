from tkinter import *
import os,index
from PIL import Image, ImageTk

def clse():
    sys.exit() 
def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt")
        lines = h.readlines()
        h.close()
        for i in lines:
            if i.find(eid.get())!=-1 and i.find(psw.get())!=-1:
                root.destroy()
                os.system('python index.py')
def verifier():
    a=b=0
    if not eid.get():
        a=1
    if not psw.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0            
def im1():
    load = Image.open("img3.jpg")
    load = load.resize((350,470), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)

    load1 = Image.open("img4.jpg")
    load1 = load1.resize((350,470), Image.ANTIALIAS)
    render1 = ImageTk.PhotoImage(load1)
    img1 = Label(root, image=render1)
    img1.image = render1
    img1.place(x=590, y=0)



        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("COVIDET V2.0")
    im1()
    eid=StringVar()
    psw=StringVar()
    label=Label(root,text="LOGIN",font="bold",fg="Red")
    label.place(x=450,y=50)
    label1=Label(root,text="Embloyee id :")
    label1.place(x=360,y=120)

    label2=Label(root,text="Password      :")
    label2.place(x=360,y=150)


    e1=Entry(root,textvariable=eid)
    e1.place(x=460,y=120)

    e2=Entry(root,show='*',textvariable=psw)
    e2.place(x=460,y=150)
   
    b4=Button(root,text="Submit",command=pos,activebackground="Green",bg="#ff0000",width=30)
    b4.place(x=363,y=200)
    b3=Button(root,text="Close",command=clse,bg="Green",activebackground="Blue",width=20)
    b3.place(x=800,y=420)
    root.mainloop()

