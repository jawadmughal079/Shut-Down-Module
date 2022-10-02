# first import the module to get interaction with the system so we used the 
# os module to get the command of interactin with system 


import os




def logOutFun():
    os.system(" shutdown -l")


# this functin for restart 

def restartFun():
    os.system("shutdown /r /t 1")
    
# this functin for restart By Time

def restartFunByTime():
    os.system("shutdown /r /t 20")
    
# this functin for ShutDown  

def shutDowN():
    os.system("shutdown /s /t 0")



# this module is used to get the graphic of system 

from tkinter import * # * this us used to get all the properties of thinker 

# first make the vaiabel to assign all the properties of tkinder

sd=Tk() # T must be Capital 

# now Give the Graphic to show into termainal and screen 

# first Give the name 
sd.title("Shut Down Application")

# now give some background 
sd.config(bg="red")

# now set the widht and height of screen or terminal 
sd.geometry("500x500")

# let create the log out button 

logOutButton=Button(text="logOut Button ",command=logOutFun)
logOutButton.place(height=50 , width=100,x=150,y=50)

# let create the restart the button 

restartButton=Button(text="restartButton",command=restartFun)
restartButton.place(height=50 , width=100,x=150,y=120)


# let create the restartByTime the button 

restartByTime=Button(text="restartByTime",command=restartFunByTime)
restartByTime.place(height=50 , width=100,x=150,y=180)

# let create the ShutDown the button 

ShutDown=Button(text="ShutDown",command=shutDowN)
ShutDown.place(height=50 , width=100,x=150,y=240)


# this function is used to get the unlimited run through appplication 
sd.mainloop()

