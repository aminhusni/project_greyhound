import threading
import tkinter as tk
import tkinter.font
from PIL import ImageTk
import serial
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
win=tk.Tk()
win.title("PROJECT GREYHOUND")
win.attributes("-fullscreen",True)
photo=tk.PhotoImage(file="/home/pi/Desktop/projectvideo/background.png")
myFont=tkinter.font.Font(family='Helvetica',size=12,weight="bold")
serial=serial.Serial('/dev/ttyUSB0',9600)
videovar="null"
FULL=Path("/home/pi/Desktop/projectvideo/full.mp4")
tapflag=0
player1=OMXPlayer(FULL,args=["--orientation","90","--loop","--no-osd"],dbus_name='org.mpris.MediaPlayer2.omxplayer0')
def disable():
 choicebutton1.config(state=tk.DISABLED)
def enable():
 choicebutton1.config(state=tk.NORMAL)
def watchdog():
 while(True):
  print("watchdog ended")
  watchdogflag.wait() 
  timeoutflag.clear()
  print("watchdog started")
  watchdogflag.clear()
  sleep(15)
  if(not timeoutflag.isSet()):
   print("timeout")
   serial.write(b'r')
   idleblock.set()
def tap():
 tapflag.set()
def ultrabypass():
 serial.write(b'8')
def looper(starttime,videoname,endtime):
 print("Looper active")
 print("Video name: "+videoname)
 print("Start pos: "+str(starttime))
 global videovar
 while(True):
  sleep(0.01)
  currentvidtime=player1.position()
  if(currentvidtime>=endtime):
   print("Relooping back to:"+str(starttime))
   player1.set_position(starttime)
  if(videoname!=videovar):
   print("Video changed!")
   break
def seeking():
 global videovar
 print("Seeking thread started")
 sleep(1)
 print(videovar)
 while(True):
  sleep(1)
  print("From seeking thread:")
  print(videovar)
  if(videovar=="idle"):
   print("video set to idle")
   starttime=0
   duration=19
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"idle",endtime)
  if(videovar=="tappls"):
   print("video set to tappls")
   starttime=21
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"tappls",endtime)
  if(videovar=="instruct"):
   print("video set to instruct")
   starttime=36
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"instruct",endtime)
  if(videovar=="instruct2"):
   print("video set to instruct2")
   starttime=51
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"instruct2",endtime)
  if(videovar=="charge1"):
   print("video set to charge1")
   starttime=66
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"charge1",endtime)
  if(videovar=="charge2"):
   print("video set to charge2")
   starttime=81
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"charge2",endtime)
  if(videovar=="charge3"):
   print("video set to charge3")
   starttime=96
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"charge3",endtime)
  if(videovar=="charge4"):
   print("video set to charge4")
   starttime=111
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"charge4",endtime)
  if(videovar=="charge5"):
   print("video set to charge5")
   starttime=126
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"charge5",endtime)
  if(videovar=="chargesucc"):
   print("video set to chargesucc")
   starttime=141
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"chargesucc",endtime)
  if(videovar=="dispense"):
   print("video set to dispense")
   starttime=156
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"dispense",endtime)
  if(videovar=="dispense2"):
   print("video set to dispense2")
   starttime=171
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"dispense2",endtime)
  if(videovar=="fail"):
   print("video set to fail")
   starttime=186
   duration=14
   player1.set_position(starttime)
   endtime=starttime+duration
   looper(starttime,"fail",endtime)
def idle():
 global videovar
 print("PROGRAM START")
 while(True):
  disable()
  videovar="idle"
  print("From idle thread:")
  print(videovar)
  reading=serial.readline() 
  print(reading)
  if(reading==b"ultra\n"):
   print("Ultra detected")
   enable()
   watchdogflag.set()
   videovar="tappls"
   idleblock.wait() 
   idleblock.clear()
def runseries():
 global videovar
 while(True):
  tapflag.wait() 
  tapflag.clear()
  timeoutflag.set() 
  serial.write(b'1')
  videovar="instruct"
  tapflag.wait()
  tapflag.clear()
  disable()
  videovar="instruct2"
  reading=serial.readline() 
  if(reading==b"yes\n"):
   print("Stage1 complete")
   videovar="charge1"
  reading=serial.readline() 
  if(reading==b"yes\n"):
   print("Stage2 complete")
   videovar="charge2"
  reading=serial.readline() 
  if(reading==b"yes\n"):
   print("Stage3 complete")
   videovar="charge3"
  reading=serial.readline() 
  if(reading==b"yes\n"):
   print("Stage4 complete")
   videovar="charge4"
  reading=serial.readline() 
  if(reading==b"yes\n"): 
   print("Stage5 complete")
   videovar="charge5"
  elif(reading==b"no\n"):
   pass
  serial.readline() 
  print("Stage6 complete")
  reading=serial.readline() 
  sleep(3)
  if(reading==b"succ\n"):
   print("SUCCESS DISPENSE")
   videovar="chargesucc"
   sleep(2)
   videovar="dispense"
   sleep(5)
   videovar="dispense2"
   sleep(5)
  elif(reading==b"fail\n"):
   videovar="fail"
   sleep(6)
   print("FAIL NO DISPENSE")
   pass
  sleep(5)
  idleblock.set()
threadidle=threading.Thread(target=idle)
threadseries=threading.Thread(target=runseries)
threadwatchdog=threading.Thread(target=watchdog)
threadseeking=threading.Thread(target=seeking)
tapflag=threading.Event()
watchdogflag=threading.Event()
timeoutflag=threading.Event()
seriesblock=threading.Event()
idleblock=threading.Event()
blockbutton=threading.Event()
choicebutton1=tk.Button(win,text='TAP',font=myFont,command=tap,height=90,width=190)
choicebutton1.grid(row=1,column=2,sticky=tk.NSEW)
choicebutton=tk.Button(win,text='BYPASS',font=myFont,command=ultrabypass,height=90,width=20)
choicebutton.grid(row=1,column=1,sticky=tk.NSEW)
if __name__=='__main__':
 threadidle.start()
 threadseries.start()
 threadwatchdog.start()
 threadseeking.start()
 win.mainloop()
 print("EXIT EXIT")
