#this is a file taken from new.py which has canny display in open window 
# this is a file we need to make it in .


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

root.geometry("730x360+28+28")
root.configure(background="white")



#canvas=Canvas(root,height=HEIGHT,width=WIDTH)
#canvas.pack()

#the upper canvas should be placed before any otjher customization..

f1=Frame(root,bg="white")
f1.place(relwidth=1,relheight=1)



label=Label(f1,text="R O S A - i",font=("comicsansms"," 68", "bold"),fg="#db04a6",background="white")
label.place(relx=-0.25,relwidth=1.5,relheight=0.2)

pic1=PhotoImage(file="TEACH1.png")
openpicc=PhotoImage(file="OPEN1.png")
helppicc=PhotoImage(file="HELP1.png")
toolspicc=PhotoImage(file="TOOLS1.png")



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
    window.geometry("730x360+28+28")
    window.configure(bg="white")   #so here,background will be red as bg=red...
    #l11=Label(root,text="R O S A -i",font=("times new roman","39","bold"),bg="white",fg="pink")
    #the above code writes a text creating label and for the texts ,the dimensions are given...


    view1=PhotoImage(file="viewpic.png")
    live1=PhotoImage(file="livepic.png")
    circle1=PhotoImage(file="newbackbutton.png")
    one1=PhotoImage(file="11.png")
    two1=PhotoImage(file="22.png")
    three1=PhotoImage(file="33.png")
    four1=PhotoImage(file="44.png")
    donesym1=PhotoImage(file="doonesymbol.png")

    label1=Label(window,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold")).pack()
    #label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)


    f1=LabelFrame(window,bg="white",border=0)#.pack(padx=50,pady=8,fill=X)
    f1.place(relx=0.2,rely=0.2,relwidth=0.76,relheight=0.73)

    l1=Label(f1,bg="pink",border=5) #here the line in the border is pink in color
    l1.pack()



    def close():
        cam.release()
        window.destroy()

    bt1=Button(window,image=circle1,border=0,bg="white",command=close)
    bt1.place(relx=0.04,rely=0.80,relwidth=0.13,relheight=0.09)



    def onedone():
        donesym1=PhotoImage(file="doonesymbol.png")
        btt1=Button(window,image=donesym1)
        btt1.image=donesym1
        btt1.place(relx=0.061,rely=0.25,relwidth=0.06,relheight=0.08)


    def twodone():
        bt2=Button(window,image=donesym1)
        bt2.place(relx=0.061,rely=0.39,relwidth=0.06,relheight=0.08)

    

    def threedone():
        bt3=Button(window,image=donesym1)
        bt3.place(relx=0.061,rely=0.53,relwidth=0.06,relheight=0.08)

    def fourdone():
        bt4=Button(window,image=donesym1)
        bt4.place(relx=0.061,rely=0.67,relwidth=0.06,relheight=0.08)

    def firstphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/template/train/img_black_01"+".jpg"   #file name 
        cv2.imwrite(file,img1) 
        #time=str(datetime.datetime.now().today()).replace(":"," ") +".jpg"
        #image.save(time)  


    def secondphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/template/train/img_black_02"+".jpg"
        cv2.imwrite(file,img1)

    def thirdphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/template/train/img_black_03"+".jpg"
        cv2.imwrite(file,img1)

    def fourthphoto():
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/template/train/img_black_04"+".jpg"
        cv2.imwrite(file,img1)



    bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
    bt1.place(relx=0.061,rely=0.25,relwidth=0.06,relheight=0.08)

    bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
    bt2.place(relx=0.061,rely=0.39,relwidth=0.06,relheight=0.08)

    bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
    bt3.place(relx=0.061,rely=0.53,relwidth=0.06,relheight=0.08)

    bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
    bt4.place(relx=0.061,rely=0.67,relwidth=0.06,relheight=0.08)

    cam = cv2.VideoCapture(0)
    while True:
        _ , img =cam.read()
        #WE CAPTURED AN IMAGE as img
        #print(img)


        img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #we updated an image and made into store in img1...
        print(img1)
        print(img)

        thresh = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)[1]

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




####################################################################################################################

def whenopen():

    global list1
    global circle1
    global one1
    global two1
    global three1
    global four1
    global test1
    global live1

    window2=Toplevel()

    window2.geometry("730x360+28+28")
    window2.configure(background="white")




    """list1=PhotoImage(file="listpic.png")
    circle1=PhotoImage(file="newbackbutton.png")
    one1=PhotoImage(file="11.png")
    two1=PhotoImage(file="22.png")
    three1=PhotoImage(file="33.png")
    four1=PhotoImage(file="44.png")"""




    label1=Label(window2,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 38", "bold"))
    label1.place(relx=0.0,rely=-0.35,relwidth=1,relheight=0.9)

    ft2=Frame(window2,bg="white",padx=25)
    ft2.place(relx=0.16,rely=0.2,relwidth=0.75,relheight=0.78)


    bt1= Label(ft2,border=0,bg="pink")
    bt1.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)

    def close():
        window2.destroy()
        cam.release()
        
    circle1=PhotoImage(file="newbackbutton.png")
    circle1btn=Button(window2,image=circle1,border=0,bg="white",command=close)
    circle1btn.image=circle1
    circle1btn.place(relx=0.04,rely=0.80,relwidth=0.13,relheight=0.09)

    def testing():
        #cam.release()
        
        image=Image.fromarray(img1)
        file="C:/Users/acer/Desktop/template/test/img00"+".jpg"   #file name 
        cv2.imwrite(file,img1)

        imggrayed = cv2.imread("",0)
        img_b_and_white = cv2.threshold(imggrayed,60,255,cv2.THRESH_BINARY)[1]

        template = cv2.imread("",0)
        imagee = cv2.threshold(template ,60,255,cv2.THRESH_BINARY)[1]

        w ,h = template.shape[::-1]

        res = cv2.matchTemplate(img_b_and_white,imagee,cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img1,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

            if pt !=None:
                circle12=PhotoImage(file="accept1.png")
                circle12btn=Button(window2,image=circle1,border=0,bg="white",command=close)
                circle12btn.image=circle1
                circle12btn.place(relx=0.09,rely=0.80,relwidth=0.13,relheight=0.09)

            else:
                circle12=PhotoImage(file="reject1.png")
                circle12btn=Button(window2,image=circle1,border=0,bg="white",command=close)
                circle12btn.image=circle1
                circle12btn.place(relx=0.09,rely=0.60,relwidth=0.13,relheight=0.09)

        try:
            os.remove("test/img00.jpg")
        except:
            pass









#######################################################################################################
    test1=PhotoImage(file="test1.png")
    b1=Button(window2,image=test1,border=0,bg="white",command=testing)
    b1.image=test1
    b1.place(relx=0.04,rely=0.41,relwidth=0.10,relheight=0.17)

        
    cam=cv2.VideoCapture(0)
    while True:
        _,frame =cam.read()

        img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        thresh = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)[1]
        img=ImageTk.PhotoImage(Image.fromarray(img1))

        #img=ImageTk.PhotoImage(Image.fromarray(imgg))


        bt1["image"]=img
        key = cv2.waitKey(1) & 0xFF
        if key==32:
            break
            

        window2.update()

        
    cv2.destroyAllWindows()
    




    def displaypic1():
        cam.release()
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

    


####################################################################################################################################################
def whenhelp():
    window3=Toplevel()

    window3.geometry("730x360+28+28")
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
    wifi1btn.place(relx=0.4,rely=0.31,relwidth=0.396,relheight=0.12)



    pass1=PhotoImage(file="passpic.png")
    pass1btn=Button(window3,image=pass1,border=0,bg="white")
    pass1btn.image=pass1
    pass1btn.place(relx=0.4,rely=0.45,relwidth=0.38,relheight=0.12)



    conn1=PhotoImage(file="connpic.png")
    conn1btn=Button(window3,image=conn1,border=0,bg="white")
    conn1btn.image=conn1
    conn1btn.place(relx=0.4,rely=0.6,relwidth=0.39,relheight=0.12)


    circle1=PhotoImage(file="newbackbutton.png")
    circle1btn=Button(window3,image=circle1,border=0,bg="white",command=window3.destroy)
    circle1btn.image= circle1
    circle1btn.place(relx=0.1,rely=0.75,relwidth=0.14,relheight=0.09)


###################################################################################33
b1=Button(f1,image=pic1,border=0,bg="white",command=when_teach,cursor="hand2")
b1.place(relx=0.05,rely=0.25,relwidth=0.44,relheight=0.30)

b2=Button(f1,image=openpicc,border=0,bg="white",command=whenopen,cursor="dot")
b2.place(relx=0.52,rely=0.25,relwidth=0.43,relheight=0.30)



b3=Button(f1,image=helppicc,border=0,bg="white",command=whenhelp,cursor="man")
b3.place(relx=0.05,rely=0.6,relwidth=0.43,relheight=0.30)



b4=Button(f1,image=toolspicc,border=0,bg="white",cursor="diamond_cross")
b4.place(relx=0.52,rely=0.6,relwidth=0.44,relheight=0.30)

root.mainloop()

