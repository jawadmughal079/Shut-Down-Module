#this funtion is used for get the information about the system 
import os

# funtion for create the shut down property 
def restartFun():
    os.system(("shutdown /r /t 0"))
    
# this function is used for shout down the system 
def shutDown():
    os.system(" shutdown /s /t 1 ") 
    
# this function is used for shut down the system 
def logOut():
    os.system(" shutdown -l") 

# this function is used for restart  the system  by time
def restartByTime():
    os.system(" shutdown /r /t 20") 




# tkinter is used for Get the graphic 
from tkinter import *

# st is simple variable   
st=Tk()

# HOW TO chagne the title of app 
# use the tiitle function pervoided by thinter 
st.title("shut down applicatin by jawad mughal ")

# how to change the background color of the app 
# config function is use for this variable.config()
st.config(bg='red')

# how to change the size of the application 
# geometry function is use for this variable.geometry()
st.geometry("500x500")

# Now this time we will discussed about the button class
# Button() this is used for create button 
# First create the restart Button
# Command functin is used for get the properties to get the function and also call pass the function 

restartButton=Button(st,text="Restart Button",command=restartFun)
restartButton.place(height="50",width="100",x='200',y='120')


# Now this time we will discussed about the button class
# Button() this is used for create button 
# First create the Shut down  Button
# Command functin is used for get the properties to get the function and also call pass the function 

shutDownButton=Button(st,text="Shut Down ",command=shutDown)
shutDownButton.place(height="50",width="100",x='200',y='50')


# Now this time we will discussed about the button class
# Button() this is used for create button 
# First create the LogOutButton
# Command functin is used for get the properties to get the function and also call pass the function 

LogOutButton=Button(st,text="LogOut ",command=logOut)
LogOutButton.place(height="50",width="100",x='200',y='190')


# Now this time we will discussed about the button class
# Button() this is used for create button 
# First create the RestartByTime
# Command functin is used for get the properties to get the function and also call pass the function 

RestartByTime=Button(st,text="Restart by Time ",command=restartByTime)
RestartByTime.place(height="50",width="100",x='200',y='260')


# main loop is for run the application for unlimited number oftimes
st.mainloop()