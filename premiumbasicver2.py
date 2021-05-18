#this is a file taken from new.py which has canny display in open window 
# this is a file we need to make it in .

import os
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk

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
    global folder1
    global folder2
    global folder3
    global folder4
    global capture_camera

    window=Toplevel()
    #when creating loop windows ,we must give >> toplevel<< instead creating simple window...

    #window.geometry("900x600")
    window.geometry("790x400+10+10")
    window.configure(bg="white")   #so here,background will be red as bg=red...
    #l11=Label(root,text="R O S A -i",font=("times new roman","39","bold"),bg="white",fg="pink")
    #the above code writes a text creating label and for the texts ,the dimensions are given...


    circle1=PhotoImage(file="newbackbutton.png")
    mainfolder=PhotoImage(file="mainfolderpic.png")
    capture_camera=PhotoImage(file="capturecamera.png")

    one1=PhotoImage(file="11.png")
    folder1=PhotoImage(file="1_folder.png")
    
    two1=PhotoImage(file="22.png")
    folder2=PhotoImage(file="2_folder.png")

    three1=PhotoImage(file="33.png")
    folder3=PhotoImage(file="3_folder.png")

    four1=PhotoImage(file="44.png")
    folder4=PhotoImage(file="4_folder.png")

    donesym1=PhotoImage(file="doonesymbol.png")

    label1=Label(window,image = folder4,fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold")).pack()
    #label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)


    f1=LabelFrame(window,bg="white",border=0)#.pack(padx=50,pady=8,fill=X)
    f1.place(relx=0.2,rely=0.2,relwidth=0.76,relheight=0.73)

    l1=Label(f1,bg="pink",border=5) #here the line in the border is pink in color
    l1.pack()



    def close():
        cam.release()
        window.destroy()

    bt1=Button(window,image=circle1,border=0,bg="white",command=close)
    bt1.place(relx=0.04,rely=0.85,relwidth=0.13,relheight=0.09)



    def onedone():
        donesym1=PhotoImage(file="doonesymbol.png")
        btt1=Button(window,image=donesym1)
        btt1.image=donesym1
        btt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)


    def twodone():
        bt2=Button(window,image=donesym1)
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.088)

    

    def threedone():
        bt3=Button(window,image=donesym1)
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

    def fourdone():
        bt4=Button(window,image=donesym1)
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    def firstphoto():
        image=Image.fromarray(edges)       
        file="/home/pi/test-repo/folderA/img_black_01"+".jpg"   #file name 
        cv2.imwrite(file,edges) 
        #time=str(datetime.datetime.now().today()).replace(":"," ") +".jpg"
        #image.save(time)  


    def firstphoto():
        image=Image.fromarray(edges)       
        file="/home/pi/test-repo/folderA/img_black_01"+".jpg"   #file name 
        cv2.imwrite(file,edges)


    def secondphoto():
        image=Image.fromarray(edges)
        file="/home/pi/test-repo/folderA/img_black_02"+".jpg"
        cv2.imwrite(file,edges)

    def thirdphoto():
        image=Image.fromarray(edges)
        file="/home/pi/test-repo/folderA/img_black_03"+".jpg"
        cv2.imwrite(file,edges)

    def fourthphoto():
        image=Image.fromarray(edges)
        file="/home/pi/test-repo/folderA/img_black_04"+".jpg"
        cv2.imwrite(file,edges)

    
    
    
    def folder1_path():

        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)
    
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)
    
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

        

        
    def folder2_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)
    
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)
    
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)
        
    def folder3_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)
    
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)
    
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)
        
    def folder4_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)
    
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)
    
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)
   




    bt_1=Button(window,image=mainfolder,border=0,bg="white")
    bt_1.place(relx=0.019,rely=0.21,relwidth=0.08,relheight=0.099)

    #bt_1=Button(window,image=capture_camera,border=0,bg="white")
   #bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

    #bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto(),onedone()])
    #bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)

    bt_1=Button(window,image=folder1,border=0,bg="white",command = folder1_path)
    bt_1.place(relx=0.03,rely=0.34,relwidth=0.06,relheight=0.08)

    #bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto(),twodone()])
   #bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)

    bt_2=Button(window,image=folder2,border=0,bg="white",command = folder2_path)
    bt_2.place(relx=0.03,rely=0.47,relwidth=0.06,relheight=0.08)

    #bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto(),threedone()])
    #bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

    bt_3=Button(window,image=folder3,border=0,bg="white",command = folder3_path)
    bt_3.place(relx=0.03,rely=0.58,relwidth=0.06,relheight=0.08)

    #bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto(),fourdone()])
    #bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    bt_4=Button(window,image=folder4,border=0,bg="white",command = folder4_path)
    bt_4.place(relx=0.03,rely=0.69,relwidth=0.06,relheight=0.08)

    cam = cv2.VideoCapture(0)
    while True:
        _ , frame =cam.read()
        print(frame)
        #WE CAPTURED AN IMAGE as img
        #print(img)


        #img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #we updated an image and made into store in img1...
        # print(img1)
        #print(img)
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
        files=[]
        #cam.release()
        #fla=filedialog.askdirectory(initialdir="C:/Users/acer/Desktop",title="select the image",filetypes=[(".csv Files", "*.csv"),("image files","*.jpg")])
        #
        fla=filedialog.askdirectory(initialdir="/home/pi/test-repo/train_images")
        
        print(fla)##files.append(fla)
        #print("files are",files)
        path_for_img_grayed = (fla+"/img_black_01.jpg")
        print(path_for_img_grayed)
        path_for_csvfile = (fla+"/4.csv")
        print(path_for_csvfile)
        print("pass")
        
    
        def testing():
        #cam.release()

            image=Image.fromarray(edges1)
            file="/home/pi/test-repo/test/img00"+".jpg"   #file name 
            cv2.imwrite(file,edges1)
            print("came inside testing function")

            imggrayed= cv2.imread(path_for_img_grayed,0)
            print(imggrayed)
            print("photo of first photo for comparing")
            #i took trained image here ...........
            template = cv2.imread("test/img00.jpg",0)
            print(template)
            print("Taken the test pic")

            #i need to load csv file here
            filee = path_for_csvfile
            print(filee)
            with open(filee,"r") as letscsv:
                csv_reader = csv.reader(letscsv)
                for line in csv_reader:
                    print(line,":")
                    print(len(line))
                    compute_value=line.pop(0)
                    print("compute_value",compute_value)
                    Uthreshold = int(float(compute_value))
                    print(type(Uthreshold))
                    break

             

            if imggrayed.shape == template.shape:
                difference = cv2.subtract(imggrayed,template)

                x= np.sum(difference!=0)
                #print(difference.shape)
                print("non_black_pixels",x)
                non_black_pixels = x.item(0)
                print(type(non_black_pixels))


                if non_black_pixels > Uthreshold:
                    print("non black pixel is greater than uthreshold")
                    circlee= PhotoImage(file="reject1.png")
                    circleebtn=Button(window2,image = circlee,border=0,bg="white")
                    circleebtn.image = circlee
                    circleebtn.place(relx=0.4,rely=0.5,relwidth=0.27,relheight=0.12)
                else:
                    print("this statement is for lthreshold")
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
def letsopentools():
    global capture_camera1
    login_wind =Toplevel()

    login_wind.title("ROSA - i")
    login_wind.resizable(0,0)

    login_wind.geometry("790x400+10+10")
    login_wind.configure(background="white")

    capture_camera1=PhotoImage(file="loginpng.png")

    f1=Frame(login_wind,bg="white")
    f1.place(relx= 0.0 ,rely= 0.0,relwidth=1,relheight=0.4)



    label1=Label(login_wind,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 60", "bold")).pack()

    label1=Label(login_wind,image = capture_camera1,fg="#db04a6",bg="white").pack()



    label2= Label(login_wind,text="ENTER PIN",font=("courier","25", "bold"),bg="grey")
    label2.place(relx=0.19,rely=0.42,relwidth=0.23,relheight=0.09)

    E1 = Entry(login_wind,bd=2,text= "MAKE A FOLDER")
    E1.place(relx=0.19,rely=0.52,relwidth=0.23,relheight=0.09)

    button_login= Button(login_wind,text="submit",font=("courier","15", "bold"),bg="green",border=0)
    button_login.place(relx=0.19,rely=0.62,relwidth=0.11,relheight=0.09)

    button_login= Button(login_wind,text="NEW",font=("courier","15", "bold"),bg="red",border=0)
    button_login.place(relx=0.32,rely=0.62,relwidth=0.099,relheight=0.09)





def toolslogin():
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


    wifi1=PhotoImage(file="toolspic.png")
    wifi1btn=Button(window3,image=wifi1,border=0,bg="white")
    wifi1btn.image=wifi1
    wifi1btn.place(relx=0.035,rely=0.31,relwidth=0.20,relheight=0.4)
    wifi1btn.configure(state='disable')

    more1=PhotoImage(file="moreopt.png")
    more1btn=Button(window3,image=more1,border=0,bg="white")
    more1btn.image=more1
    more1btn.place(relx=0.25,rely=0.45,relwidth=0.07,relheight=0.09)
    more1btn.configure(state='disable')



    pass1=PhotoImage(file="toolfolderpng.png")
    pass1btn=Button(window3,image=pass1,border=0,bg="white")
    pass1btn.image=pass1
    pass1btn.place(relx=0.4,rely=0.31,relwidth=0.16,relheight=0.35)



    conn1=PhotoImage(file="WIFIpng.png")
    conn1btn=Button(window3,image=conn1,border=0,bg="white")
    conn1btn.image=conn1
    conn1btn.place(relx=0.6,rely=0.31,relwidth=0.20,relheight=0.35)


    circle1=PhotoImage(file="newbackbutton.png")
    circle1btn=Button(window3,image=circle1,border=0,bg="white",command=window3.destroy)
    circle1btn.image= circle1
    circle1btn.place(relx=0.035,rely=0.75,relwidth=0.14,relheight=0.09)


###################################################################################33
b1=Button(f1,image=pic1,border=0,bg="white",command=when_teach,cursor="hand2")
b1.place(relx=0.05,rely=0.25,relwidth=0.44,relheight=0.30)

b2=Button(f1,image=openpicc,border=0,bg="white",command=whenopen,cursor="dot")
b2.place(relx=0.52,rely=0.25,relwidth=0.43,relheight=0.30)


                                                    
b3=Button(f1,image=toolspicc,border=0,bg="white",command=letsopentools,cursor="man")
b3.place(relx=0.05,rely=0.6,relwidth=0.43,relheight=0.30)



b4=Button(f1,image=helppicc,border=0,bg="white",cursor="diamond_cross")
b4.place(relx=0.52,rely=0.6,relwidth=0.44,relheight=0.30)

root.mainloop()





