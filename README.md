# rosa-i
#this is the initial code for rosa-i and implementation wll be done 
#this file is purely on customization of open file


import datetime
import os
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk

#HEIGHT=600
#WIDTH=800

root =Tk()
root.title("ROSA - i")

root.geometry("800x600+50+50")
root.configure(background="white")



#canvas=Canvas(root,height=HEIGHT,width=WIDTH)
#canvas.pack()

#the upper canvas should be placed before any otjher customization..

f1=Frame(root,bg="white")
f1.place(relwidth=1,relheight=1)



label=Label(f1,text="R O S A - i",font=("comicsansms"," 110", "bold"),fg="#db04a6",background="white")
label.place(relx=-0.25,relwidth=1.5,relheight=0.2)

pic1=PhotoImage(file="EDITED1.png")
openpicc=PhotoImage(file="openpic1.png")
helppicc=PhotoImage(file="HELPPIC.png")
toolspicc=PhotoImage(file="TOOLS.png")



#################################################################################################################
def when_teach():
    global view1
    global live1
    global circle1
    global one1
    global two1
    global three1
    global four1
    global donesym1

    window=Toplevel()
    #when creating loop windows ,we must give >> toplevel<< instead creating simple window...

    #window.geometry("900x600")
    window.geometry("800x600+50+50")
    window.configure(bg="white")   #so here,background will be red as bg=red...
    #l11=Label(root,text="R O S A -i",font=("times new roman","39","bold"),bg="white",fg="pink")
    #the above code writes a text creating label and for the texts ,the dimensions are given...


    view1=PhotoImage(file="viewpic.png")
    live1=PhotoImage(file="livepic.png")
    circle1=PhotoImage(file="circle-cropped.png")
    one1=PhotoImage(file="11.png")
    two1=PhotoImage(file="22.png")
    three1=PhotoImage(file="33.png")
    four1=PhotoImage(file="44.png")
    donesym1=PhotoImage(file="donesymbol1.png")

    label1=Label(window,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold")).pack()
    #label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)


    f1=LabelFrame(window,bg="white",border=0)#.pack(padx=50,pady=8,fill=X)
    f1.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.55)

    l1=Label(f1,bg="pink",border=5) #here the line in the border is pink in color
    l1.pack()

    #cap=cv2.VideoCapture(0)

    #bt1=Button(window,image=view1,border=0,bg="white")
    #bt1.place(relx=0.1,rely=0.78,relwidth=0.17,relheight=0.099)


    #bt1=Button(window,image=live1,border=0,bg="white")
    #bt1.place(relx=0.28,rely=0.78,relwidth=0.17,relheight=0.099)

    bt1=Button(window,image=circle1,border=0,bg="white",command=window.destroy)
    bt1.place(relx=0.1,rely=0.89,relwidth=0.13,relheight=0.09)



    def onedone():
        donesym1=PhotoImage(file="donesymbol1.png")
        btt1=Button(window,image=donesym1)
        btt1.image=donesym1
        btt1.place(relx=0.33,rely=0.89,relwidth=0.06,relheight=0.08)


    def twodone():
        bt2=Button(window,image=donesym1)
        bt2.place(relx=0.43,rely=0.89,relwidth=0.06,relheight=0.08)

    

    def threedone():
        bt3=Button(window,image=donesym1)
        bt3.place(relx=0.53,rely=0.89,relwidth=0.06,relheight=0.08)

    def fourdone():
        bt4=Button(window,image=donesym1)
        bt4.place(relx=0.63,rely=0.89,relwidth=0.06,relheight=0.08)

    def firstphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/rossa-i/machineimages/{}"+"img00"+".jpg" .format(e1.get())   #file name 
        cv2.imwrite(file,img1) 
        #time=str(datetime.datetime.now().today()).replace(":"," ") +".jpg"
        #image.save(time)  


    def secondphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/rossa-i/img01"+".jpg"
        cv2.imwrite(file,img1)

    def thirdphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/rossa-i/img02"+".jpg"
        cv2.imwrite(file,img1)

    def fourthphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/rossa-i/img03"+".jpg"
        cv2.imwrite(file,img1)



    bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
    bt1.place(relx=0.33,rely=0.89,relwidth=0.06,relheight=0.08)

    bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
    bt2.place(relx=0.43,rely=0.89,relwidth=0.06,relheight=0.08)

    bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
    bt3.place(relx=0.53,rely=0.89,relwidth=0.06,relheight=0.08)

    bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
    bt4.place(relx=0.63,rely=0.89,relwidth=0.06,relheight=0.08)


#################customization section #############################
    e1=Entry(window,bg="white",font=30)
    e1.place(relx=0.5,rely=0.78,relwidth=0.4,relheight=0.089)

    global picsave
    global picdone

    picsave=PhotoImage(file="save1.png")
    picdone=PhotoImage(file="donestamp1.png")

    entrybutton=Button(window,image=picsave,command=lambda :[create(),link(),new()] ,border=0,background="white")
    entrybutton.place(relx=0.68,rely=0.84,relwidth=0.40,relheight=0.15)

    def create():
        import os

        #file1=fdialog.askopenfile()
        #label1=Label(text=file1).pack()
        #folder=e1.get()
        newpath = r"C:\Users\acer\Desktop\rossa-i\machineimages\{}".format(e1.get())
        if not os.path.exists(newpath):
            os.makedirs(newpath)


    
    def link():
        b1=Button(window,image=picdone,border=0,background="white")
        b1.place(relx=0.68,rely=0.84,relwidth=0.40,relheight=0.15)

    cam=cv2.VideoCapture(0)
    
    while True:
        _,img=cam.read()
        #WE CAPTURED AN IMAGE as img


        img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #we updated an image and made into store in img1...

        img=ImageTk.PhotoImage(Image.fromarray(img1))
        #photo image ,we are converting into tkinter image
    

        l1["image"]=img
        #we have created l1 Label ,where our live video i.e , is stored in (img )is directly linked 


        #key=cv2.waitKey(1)
        #if key==27:
            #break


        window.update()





        if cv2.waitKey(1)& 0xFF==ord('q'):
            break
    cam.release() 
    cv2.destroyAllWindows()

    #bt1=Button(window,image=circle1,border=0,bg="white",command=window.destroy)
    #bt1.place(relx=0.1,rely=0.89,relwidth=0.13,relheight=0.09)
####################################################################################################################

def whenopen():
    window2=Toplevel()

    window2.geometry("800x600+50+50")
    window2.configure(background="white")
    global list1
    global circle1
    global one1
    global two1
    global three1
    global four1
    global view1
    global live1



    """list1=PhotoImage(file="listpic.png")
    circle1=PhotoImage(file="circle-cropped.png")
    one1=PhotoImage(file="11.png")
    two1=PhotoImage(file="22.png")
    three1=PhotoImage(file="33.png")
    four1=PhotoImage(file="44.png")"""




    label1=Label(window2,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold"))
    label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)

    ft2=Frame(window2,bg="white",padx=25)
    ft2.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.51)


    bt1=Label(ft2,border=0,bg="pink")
    bt1.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)
        

    list1=PhotoImage(file="listpic.png")
    list1btn=Button(window2,image=list1,border=0,bg="white")
    list1btn.image=list1
    list1btn.place(relx=0.11,rely=0.78,relwidth=0.49,relheight=0.099)

    circle1=PhotoImage(file="circle-cropped.png")
    circle1btn=Button(window2,image=circle1,border=0,bg="white",command=window2.destroy)
    circle1btn.image= circle1
    circle1btn.place(relx=0.1,rely=0.89,relwidth=0.13,relheight=0.09)

    view1=PhotoImage(file="viewpic.png")
    b1=Button(window2,image=view1,border=0,bg="white")
    b1.image=view1
    b1.place(relx=0.60,rely=0.78,relwidth=0.17,relheight=0.099)


    ####################
    def getting_live():
        cam=cv2.VideoCapture(0)
        while True:
            _,img=cam.read()
            img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=ImageTk.PhotoImage(Image.fromarray(img1))
            label1["image"]=img

            key = cv2.waitKey(1)
            if key==27:
                break
            

            window2.update()

        cam.release()
        cv2.destroyAllWindows()


        

                


        
    
    


    live1=PhotoImage(file="livepic.png")
    b2=Button(window2,image=live1,border=0,bg="white",command=getting_live)
    b2.place(relx=0.76,rely=0.78,relwidth=0.17,relheight=0.1)


    """view1=PhotoImage(file="viewpic.png")
    view1btn=Button(window2,image=view1,border=0,bg="white")
    view1btn.image=view1
    bt1.place(relx=0.78,rely=0.78,relwidth=0.17,relheight=0.099)


    live1=PhotoImage(file="livepic.png")
    live1btn=Button(window2,image=live1,border=0,bg="white")
    live1btn.image=live1
    bt1.place(relx=0.99,rely=0.78,relwidth=0.17,relheight=0.099) """

    
    def displaypic1():
        fla=filedialog.askopenfilename(initialdir=os.getcwd(),title="select the image")
        img=Image.open(fla)
        img.thumbnail((350,500))
        img1=ImageTk.PhotoImage(img)
        label1.configure(image=img1)
        label1.image=img1
        


    global one1
    global two1
    label1=Label(ft2,bg="white")
    label1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)

    
    def displaypic2():
        flb=filedialog.askopenfilename(initialdir=os.getcwd(),title="select the image")
        img=Image.open(flb)
        img.thumbnail((350,500))
        img1=ImageTk.PhotoImage(img)
        label1.configure(image=img1)
        label1.image=img1
       
    
    
    def displaypic3():
        flc=filedialog.askopenfilename(initialdir=os.getcwd(),title="select the image")
        img=Image.open(flc)
        img.thumbnail((350,500))
        img1=ImageTk.PhotoImage(img)
        label1.configure(image=img1)
        label1.image=img1


    def displaypic4():
        fld=filedialog.askopenfilename(initialdir=os.getcwd(),title="select the image")
        img=Image.open(fld)
        img.thumbnail((350,500))
        img1=ImageTk.PhotoImage(img)
        label1.configure(image=img1)
        label1.image=img1


    one1=PhotoImage(file="11.png")
    onne1btn=Button(window2,image=one1,border=0,bg="white",command=displaypic1)
    onne1btn.image=one1
    onne1btn.place(relx=0.33,rely=0.89,relwidth=0.06,relheight=0.08)

    two1=PhotoImage(file="22.png")
    two1btn=Button(window2,image=two1,border=0,bg="white",command=displaypic2)
    two1btn.image=two1
    two1btn.place(relx=0.43,rely=0.89,relwidth=0.06,relheight=0.08)

    three1=PhotoImage(file="33.png")
    three1btn=Button(window2,image=three1,border=0,bg="white",command=displaypic3)
    three1btn.image=three1
    three1btn.place(relx=0.53,rely=0.89,relwidth=0.06,relheight=0.08)

    four1=PhotoImage(file="44.png")
    four1btn=Button(window2,image=four1,border=0,bg="white",command=displaypic4)
    four1btn.image=four1
    four1btn.place(relx=0.63,rely=0.89,relwidth=0.06,relheight=0.08)


#####################################################################################################################################################
############################################################################################################
def whenhelp():
    window3=Toplevel()

    window3.geometry("800x600+50+50")
    window3.configure(background="white")

    global wifi1
    global pass1
    global conn1



    label1=Label(window3,text="R O S A -i",fg="#db04a6",bg="white",font=("comicsansms"," 60"))
    label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)

    ft3=Frame(window3,bg="white")
    ft3.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.45)


    wifi1=PhotoImage(file="wifipic.png")
    wifi1btn=Button(window3,image=wifi1,border=0,bg="white")
    wifi1btn.image=wifi1
    wifi1btn.place(relx=0.4,rely=0.31,relwidth=0.49,relheight=0.12)



    pass1=PhotoImage(file="passpic.png")
    pass1btn=Button(window3,image=pass1,border=0,bg="white")
    pass1btn.image=pass1
    pass1btn.place(relx=0.4,rely=0.45,relwidth=0.49,relheight=0.12)



    conn1=PhotoImage(file="connpic.png")
    conn1btn=Button(window3,image=conn1,border=0,bg="white")
    conn1btn.image=conn1
    conn1btn.place(relx=0.4,rely=0.6,relwidth=0.49,relheight=0.12)


    circle1=PhotoImage(file="circle-cropped.png")
    circle1btn=Button(window3,image=circle1,border=0,bg="white",command=window3.destroy)
    circle1btn.image= circle1
    circle1btn.place(relx=0.1,rely=0.75,relwidth=0.21,relheight=0.1)


###################################################################################33
b1=Button(f1,image=pic1,border=0,bg="white",command=when_teach,cursor="hand2")
b1.place(relx=0.05,rely=0.25,relwidth=0.43,relheight=0.29)

b2=Button(f1,image=openpicc,border=0,bg="white",command=whenopen,cursor="dot")
b2.place(relx=0.52,rely=0.25,relwidth=0.43,relheight=0.29)



b3=Button(f1,image=helppicc,border=0,bg="white",command=whenhelp,cursor="man")
b3.place(relx=0.05,rely=0.6,relwidth=0.43,relheight=0.29)



b4=Button(f1,image=toolspicc,border=0,bg="white",cursor="diamond_cross")
b4.place(relx=0.52,rely=0.6,relwidth=0.43,relheight=0.29)

root.mainloop()





















































































































































