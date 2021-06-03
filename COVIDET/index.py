from tkinter import *
import sys,os
from PIL import Image, ImageTk
import dele

def verifier():
    a=b=c=d=e=f=0
    if not name.get():
        t1.insert(END,"<>Name is required<>\n")
        a=1
    if not adhar.get():
        t1.insert(END,"<>Adhar no is required<>\n")
        b=1
    if not age.get():
        t1.insert(END,"<>Age is required<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not cstatus.get():
        t1.insert(END,"<>Covid test result name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0
def ver():
    a=0
    if not name.get():
        t1.insert(END,"<>Name is required<>\n")
        a=1
    return a
def ser():
    t=ver()
    if (t==0):
        f=open("positive.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(name.get())!=-1:
                t1.insert(END,"\n"+i+"\n")
        g=open("negative.txt")
        lines1 = g.readlines()
        g.close()
        for j in lines1:
            if j.find(name.get())!=-1:
                t1.insert(END,"\n"+j+"\n")    

def ad():
    ls=name.get()+'|'+adhar.get()+'|'+age.get()+'|'+phone.get()+'|'+cstatus.get()+'|'+address.get()+"\n"
    if cstatus.get()=="positive":
        p=open('positive.txt','a')
        p.write(ls)
        p.close()
    if cstatus.get()=="negative":
        n=open('negative.txt','a')
        n.write(ls)
        n.close()
                    


def add_patient():
            ret=verifier()
            if ret==0:
                ad()
                t1.insert(END,"\nADDED SUCCESSFULLY\n")
                
def view_patient():
    p=open('positive.txt')
    n=open('negative.txt')
    c1=p.read()
    c2=n.read()
    p.close()
    n.close()
    t1.insert(END,"\npositive"+"\n")
    t1.insert(END,c1)
    t1.insert(END,"\n"+"Negative"+"\n")
    t1.insert(END,c2)


def delete_patient():
    if not adhar.get():
        t1.insert(END,"<>Adhar is required<>\n")
    else:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        t1.insert(END,"\nDeleted successfully\n")

def update_patient():
    ret=verifier()
    if ret==0:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        ad()
        t1.insert(END,"\nUpdated successfully\n")
def clse():
    root.destroy()
    os.system('python script.py')
def add():
    root.destroy()
    os.system('python sinup.py')
def im():
    load = Image.open("img6.jpg")
    load = load.resize((285,120), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=205)


if __name__=="__main__":
    root=Tk()
    root.title("COVIDET V2.0")
    root.minsize(935, 455)
    root.maxsize(935, 455)

    name=StringVar()
    adhar=StringVar()
    age=StringVar()
    phone=StringVar()
    cstatus=StringVar()
    address=StringVar()
    
    label1=Label(root,text="Patient name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Adhar:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Age:")
    label3.place(x=0,y=60)

    label4=Label(root,text="Phone Number:")
    label4.place(x=0,y=90)

    label5=Label(root,text="Covid19 test result:")
    label5.place(x=0,y=120)

    label6=Label(root,text="Address:")
    label6.place(x=0,y=150)

    e1=Entry(root,textvariable=name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=adhar)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=age)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=phone)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=cstatus)
    e5.place(x=100,y=120)

    e6=Entry(root,textvariable=address)
    e6.place(x=100,y=150)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
 
    b0=Button(root,text="SEARCH",command=ser,width=40)
    b0.place(x=0,y=180)  

    im()

    b1=Button(root,text="ADD PATIENT",command=add_patient,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL PATIENTS",command=view_patient,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE PATIENT",command=delete_patient,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_patient,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="LOGOUT",command=clse,width=40)
    b5.grid(row=15,column=0)
    b6=Button(root,text="Add Embloyee",command=add,width=25)
    b6.place(x=770,y=430)

    root.mainloop()
