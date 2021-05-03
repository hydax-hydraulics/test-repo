#this is a file taken from new.py which has canny display in open window 
# this is a file we need to make it in .

from os.path import join
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk
import glob
import time
import math
import os
import csv




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
    #when creating loop windows ,we must give >> toplevel<< instead creating simple window...

    #window.geometry("900x600")
    window.geometry("790x400+10+10")
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
    
    Le1 = Label(window, text="Make a folder",bg="white")
    Le1.place(relx=0.01,rely=0.10,relwidth=0.18,relheight=0.09)
    E1 = Entry(window,bd=5,text= "MAKE A FOLDER")
    E1.place(relx=0.01,rely=0.16,relwidth=0.18,relheight=0.09)
    


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
        
    def estimate_button():
        bt4=Button(window,text="ESTIMATE",border=0,bg="white",command=estimate_result)
        bt4.place(relx=0.061,rely=0.90,relwidth=0.09,relheight=0.08)
        

    def firstphoto():
        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[onedone(),secondphoto()])
        bt1.place(relx=0.061,rely=0.25,relwidth=0.06,relheight=0.08)

        image=Image.fromarray(edges)       
        file=("/home/pi/test-repo/train_images/{}/img_black_01"+".jpg").format(E1.get()) #file name 
        cv2.imwrite(file,edges) 
        #time=str(datetime.datetime.now().today()).replace(":"," ") +".jpg"
        #image.save(time)  


    def secondphoto():
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[twodone(),thirdphoto()])
        bt2.place(relx=0.061,rely=0.39,relwidth=0.06,relheight=0.08)

        image=Image.fromarray(edges)
        file=("/home/pi/test-repo/train_images/{}/img_black_02"+".jpg").format(E1.get())
        cv2.imwrite(file,edges)

    def thirdphoto():
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[threedone(),fourthphoto()])
        bt3.place(relx=0.061,rely=0.53,relwidth=0.06,relheight=0.08)


        image=Image.fromarray(edges)
        file=("/home/pi/test-repo/train_images/{}/img_black_03"+".jpg").format(E1.get())
        cv2.imwrite(file,edges)

    def fourthphoto():
        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourdone(),estimate_button()])
        bt4.place(relx=0.061,rely=0.67,relwidth=0.06,relheight=0.08)
        image=Image.fromarray(edges)
        file=("/home/pi/test-repo/train_images/{}/img_black_04"+".jpg").format(E1.get())
        cv2.imwrite(file,edges)

    def estimate_result():


        NonBP=[]
        calc=[]
        i=2
        print("pass")
        path = ("/home/pi/test-repo/train_images/{}/*.*").format(E1.get())
        print("path of file:",path)
        #path = ("/home/pi/test-repo/train/*.*")
        for a in glob.glob(path):
            ab = ("train_images/{}/img_black_01.jpg").format(E1.get())
            
#             print(ab)
            photo1 = cv2.imread(ab,0)
            print(photo1)
            bc=("train_images/{}/img_black_0"+str(int(i))+".jpg").format(E1.get())
            photo_all = cv2.imread(bc,0)           
            print("2nd path:", photo_all)
            if photo1.shape==photo_all.shape:
                print(i,"st pass")
                diff = cv2.subtract(photo1,photo_all)
                #print(diff)
                non_black_pix = np.sum(diff!=0)

                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)

                i=i+1
                print("i=",i)
                if i==5:
                    print("end of the loop")
                    print(NonBP)
                    break

        ef=("train_images/{}/img_black_02.jpg").format(E1.get())
        gh=("train_images/{}/img_black_03.jpg").format(E1.get())
        photo2 = cv2.imread(ef,0)
        photo3 = cv2.imread(gh,0)
        if photo2.shape==photo3.shape:
            diff1 = cv2.subtract(photo2,photo3)
            other_two_values = np.sum(diff1!=0)
            NonBP.append(other_two_values)
            print("other_two_values",other_two_values)
            print(NonBP)

        Mean = sum(NonBP)/len(NonBP)
        Var = sum(pow(i_v - Mean,2) for i_v in NonBP)/len(NonBP)
        Std_dev = math.sqrt(Var)
        print("Mean is ",Mean)
        calc.append(Mean)
        print("Std_dev",Std_dev)
        calc.append(Std_dev)
        Uthreshold = Mean+Std_dev
        Lthreshold = Mean-Std_dev
        print("Uthreshold",Uthreshold)
        calc.append(Uthreshold)
        print("Lthreshold",Lthreshold)
        calc.append(Lthreshold)
        
        print("calc=",calc)
        
        row_list=[["Mean","Std_dev","Uthreshold","Lthreshold"],[Mean,Std_dev,Uthreshold,Lthreshold]]
        ff=("train_images/{}/4.csv").format(E1.get())
        with open(ff,"w",newline="") as file:
              writer = csv.writer(file)
              writer.writerows(row_list)






        """bt1=Button(window,image=one1,border=0,bg="white", command=firstphoto)
        bt1.place(relx=0.061,rely=0.25,relwidth=0.06,relheight=0.08)"""
        



    def create_option():
        newpath = (r"/home/pi/test-repo/train_images/{}").format(E1.get())
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        firstphoto()
        

    def switch():
        pass

    

    create_button=Button(window,text= "create",border=5,bg="white",command=create_option)
    create_button.place(relx=0.12,rely=0.25,relwidth=0.06,relheight=0.08)


    def close():
        cam.release()
        window.destroy()

    bt1=Button(window,image=circle1,border=0,bg="white",command=close)
    bt1.place(relx=0.04,rely=0.80,relwidth=0.13,relheight=0.09)




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

        #thresh = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)[1]

        #img=ImageTk.PhotoImage(Image.fromarray(img1))
        #photo image ,we are converting into tkinter image


        #l1["image"]=img
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

    def choosethefolder():
        #cam.release()
        #fla=filedialog.askdirectory(initialdir="C:/Users/acer/Desktop",title="select the image",filetypes=[(".csv Files", "*.csv"),("image files","*.jpg")])
        fla=filedialog.askdirectory(initialdir="")
        print(fla)
        path_for_img_grayed = (fla+"/img_black_01.jpg")
        print(path_for_img_grayed)
        path_for_csvfile = (fla+"/4.csv")
        print(path_for_csvfile)
        
    
        def testing():
        #cam.release()

            image=Image.fromarray(edges1)
            file="/home/pi/test-repo/test/img00"+".jpg"   #file name 
            cv2.imwrite(file,edges1)

            imggrayed= cv2.imread(path_for_img_grayed,0)#i took trained image here ...........
            template = cv2.imread("test/img00.jpg",0)

            #i need to load csv file here 
            with open(path_for_csvfile,"r") as letscsv:
                csv_reader = csv.reader(letscsv)
                for line in csv_reader:
                    print(line)
                    break

            Uthreshold = line 

            if imggrayed.shape == template.shape:
                difference = cv2.subtract(imggrayed,template)

                test_hub_live = np.sum(difference!=0)
                #print(difference.shape)
                print(test_hub_live)


                if test_hub_live > Uthreshold:
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


            try:
                os.remove("test/img00.jpg")
            except:
                pass
#######################################################################################################
        test1=PhotoImage(file="test1.png")
        b1=Button(window2,image=test1,border=0,bg="white",command=testing)
        b1.image=test1
        b1.place(relx=0.04,rely=0.30,relwidth=0.10,relheight=0.17)    
        


    test1=PhotoImage(file="choose1.png")
    b1=Button(window2,image=test1,border=0,bg="white",command=choosethefolder)
    b1.image=test1
    b1.place(relx=0.04,rely=0.50,relwidth=0.10,relheight=0.17)


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

