
#this is a file taken from new.py which has canny display in open window 
# this is a file we need to make it in .

import os
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk
import math
import glob


root =Tk()
root.title("ROSA - i")
root.resizable(0,0)

root.geometry("790x400+10+10")
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
    global circle1
    global one1
    global two1
    global three1
    global four1
    global donesym1

    window=Toplevel()


    window.geometry("790x400+10+10")
    window.configure(bg="white")   




    circle1=PhotoImage(file="newbackbutton.png")
    one1=PhotoImage(file="captureforteach.png")
 

    label1=Label(window,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold")).pack()
   


    f1=LabelFrame(window,bg="white",border=0)
    f1.place(relx=0.2,rely=0.2,relwidth=0.76,relheight=0.73)

    l1=Label(f1,bg="pink",border=5)
    l1.pack()



    def close():
        cam.release()
        window.destroy()

    bt1=Button(window,image=circle1,border=0,bg="white",command=close)
    bt1.place(relx=0.04,rely=0.80,relwidth=0.13,relheight=0.09)



    

    def firstphoto():
        i=1
        while i<21:
            image=Image.fromarray(edges)       
            file="/home/pi/test-repo/train/img_black"+str(i)+".jpg" #file name 
            cv2.imwrite(file,edges) 
            i = i+1
            
        file_list = glob.glob("/home/pi/test-repo/train/*.*")
        print(file_list)
        
        non_black_pixels_values = []
        my_list_values = []
        
        path=("/home/pi/test-repo/train/*.*")
        i=2
        for a in glob.glob(path):
            photo2=cv2.imread("/home/pi/test-repo/train/img_black"+str(i)+".jpg")
            photo1= cv2.imread("/home/pi/test-repo/train/img_black1.jpg")
            
            if photo1.shape==photo2.shape:
                diff = cv2.subtract(photo1,photo2)
                print("difference image",diff)
                Non_black_diff_values = np.sum(diff!=0)
                non_black_pixels_values.append(Non_black_diff_values)
                i=i+1
            i=i
        print(non_black_pixels_values)
        
        Mean = sum(non_black_pixels_values)/len(non_black_pixels_values)
        Var = sum(pow(i_v - Mean) for i_v in non_black_pixels_values)/len(non_black_pixels_values)
        Std_dev = math.sqrt(Var)
        
        print(Std_dev)
        
        Uthreshold = (Mean +Std_dev)
        Lthrehold = (Mean-Std_dev)
        
        
        
  
 

    bt1=Button(window,image=one1,border=0,bg="white", command=firstphoto)
    bt1.place(relx=0.01,rely=0.25,relwidth=0.19,relheight=0.36)



    cam = cv2.VideoCapture(0)
    while True:
        _ , frame =cam.read()
    
        img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        lower_red = np.array([30,150,50])
        upper_red = np.array([255,255,180])

        mask = cv2.inRange(img1,lower_red,upper_red)


        res = cv2.bitwise_and(frame,frame,mask=mask)
        edges =cv2.Canny(img1,100,200)
        edgesvid = ImageTk.PhotoImage(Image.fromarray(edges))
        l1["image"] = edgesvid

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

    window2.geometry("790x400+10+10")
    window2.configure(background="white")


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

        image=Image.fromarray(edges1)
        file="/home/pi/test-repo/test/img00"+".jpg"   #file name 
        cv2.imwrite(file,edges1)



        imggrayed= cv2.imread("test-repo/train/img_black1.jpg",0)#i took trained image here ...........
        template = cv2.imread("test-repo/test/img00.jpg",0)
        if imggrayed.shape == template.shape:
            difference = cv2.subtract(imggrayed,template)


            #no_of_white_pix = np.sum(difference==255)
            open_test = np.sum(difference!=0)
            
            if open_test >Uthreshold:
                circlee= PhotoImage(file="reject1.png")
                circleebtn=Button(window2,image = circlee,border=0,bg="white")
                circleebtn.image = circlee
                circleebtn.place(relx=0.4,rely=0.5,relwidth=0.27,relheight=0.12)
            else:
                print("hello")
                circle2=PhotoImage(file="accept1.png")
                circle2btn=Button(window2,image = circle2,border =0,bg="white")
                circle2btn.image = circle2
                circle2btn.place(relx=0.4,rely=0.5,relwidth=0.30,relheight=0.12)
                
                
            #print(difference.shape)

          


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

        hellovid= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #print(hellovid)
        #thresh = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)[1]
        #img=ImageTk.PhotoImage(Image.fromarray(img1))

        #img=ImageTk.PhotoImage(Image.fromarray(imgg))
        lower_red = np.array([30,150,50])
        upper_red = np.array([255,255,180])

        mask = cv2.inRange(hellovid,lower_red,upper_red)
        res = cv2.bitwise_and(frame,frame,mask=mask)
        edges1 =cv2.Canny(hellovid,100,200)
        edgesvid1 = ImageTk.PhotoImage(Image.fromarray(edges1))
        bt1["image"]=edgesvid1
        key = cv2.waitKey(1) & 0xFF
        if key==32:
            break


        window2.update()


    cv2.destroyAllWindows()
    cam.release()



####################################################################################################################################################
def whenhelp():
    window3=Toplevel()

    window3.geometry("790x400+10+10") 
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

