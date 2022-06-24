from datetime import datetime
from fileinput import filename
import imp
import webbrowser
import cv2 
from PIL import Image
from playsound import playsound
import statistics
import mouse
import random
import time
from pygame import mixer
import pywhatkit as pk
from cv2 import mean
import keyboard as kb
import webbrowser as wb
import pyautogui as pg
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
check,pframe=webcam.read()
pcount=0
count=0
greet= ["kese.mp3","sharma.mp3","swagat.mp3","gareebkhana.mp3","chai.mp3"]
c=0
time.sleep(5)
while True:
    
    try:
        cv2.imwrite(filename='imageu.jpg',img=pframe)
        
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        cv2.imwrite(filename='imagef.jpg',img=frame)
        
        img1=Image.open('imageu.jpg')
        img2=Image.open('imagef.jpg')
        pix1=list(img1.getdata())
        pix2=list(img2.getdata())
        if(c>10):
            
            for i in range(0,len(pix1)):
                ru=pix1[i][0]
                gu=pix1[i][1]
                bu=pix1[i][2]
                rf=pix2[i][0]
                gf=pix2[i][1]
                bf=pix2[i][2]
                if(abs(ru-rf)>50 and abs(gu-gf)>50 and abs(bu-bf)>50):
            
                    count=count+1
        print(count)
        if(count>3000):

            print(count,"ACTIEE")
            m = datetime.now().minute
            h = datetime.now().hour
            pg.keyDown('alt')
            pg.press('tab')
            pg.press('tab')
            pg.keyUp('alt')
            time.sleep(2)
            kb.write("SOMEONE's IN THE HOUSE!")
            kb.press_and_release('enter')
            pg.keyDown('alt')
            pg.press('tab')
            pg.press('tab')
            pg.keyUp('alt')
           

            time.sleep(5)
            count=0        
        c+=1
        pcount=count        
        
        
         
    
        pframe=frame
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
