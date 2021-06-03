from tkinter import *
import os,sys
def back():
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
def add():
	ret=verifier()
	if ret==0:
		la=eid.get()+' | '+psw.get()+"\n"
		f=open("admin.txt","a")
		f.write(la)
		f.close()
		os.system('python index.py')

if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.configure(bg="gray25")
    root.title("COVIDET V2.0")
     
    eid=StringVar()
    psw=StringVar()
    label=Label(root,text="ADD EMBLOYEE",font="bold",fg="Red")
    label.place(x=410,y=50)
    label1=Label(root,text="Embloyee id        :")
    label1.place(x=360,y=120)

    label2=Label(root,text="Create Password :")
    label2.place(x=360,y=150)


    e1=Entry(root,textvariable=eid)
    e1.place(x=460,y=120)

    e2=Entry(root,textvariable=psw)
    e2.place(x=460,y=150)
   
    b4=Button(root,text="Submit",command=add,bg="#ff0000",activebackground="Green",width=30)
    b4.place(x=363,y=200)

    b3=Button(root,text="Back",command=back,bg="Blue",activebackground="Green",width=20)
    b3.place(x=800,y=420)
    root.mainloop()