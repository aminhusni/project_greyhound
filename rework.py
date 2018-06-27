import threading
import tkinter as tk
import tkinter.font
from PIL import ImageTk
import serial
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
e=tk.Tk()
e.title("PROJECT GREYHOUND")
e.attributes("-fullscreen",True)
s=tk.PhotoImage(file="/home/pi/Desktop/projectvideo/background.png")
L=tkinter.font.Font(family='Helvetica',size=12,weight="bold")
A=serial.Serial('/dev/ttyUSB0',9600)
h="null"
v=Path("/home/pi/Desktop/projectvideo/full.mp4")
k=0
p=OMXPlayer(v,args=["--orientation","90","--loop","--no-osd"],dbus_name='org.mpris.MediaPlayer2.omxplayer0')
def disable():
 F.config(state=tk.DISABLED)
def enable():
 F.config(state=tk.NORMAL)
def watchdog():
 while(True):
  print("watchdog ended")
  Y.wait()
  j.clear()
  print("watchdog started")
  Y.clear()
  b(15)
  if(not j.isSet()):
   print("timeout")
   A.write(b'r')
   o.set()
def tap():
 k.set()
def ultrabypass():
 A.write(b'8')
def looper(X,videoname,f):
 print("Looper active")
 print("Video name: "+videoname)
 print("Start pos: "+str(X))
 global h
 while(True):
  b(0.01)
  x=p.position()
  if(x>=f):
   print("Relooping back to:"+str(X))
   p.set_position(X)
  if(videoname!=h):
   print("Video changed!")
   break
def seeking():
 global h
 print("Seeking thread started")
 b(1)
 print(h)
 while(True):
  b(1)
  print("From seeking thread:")
  print(h)
  if(h=="idle"):
   print("video set to idle")
   X=0
   n=19
   p.set_position(X)
   f=X+n
   looper(X,"idle",f)
  if(h=="tappls"):
   print("video set to tappls")
   X=21
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"tappls",f)
  if(h=="instruct"):
   print("video set to instruct")
   X=36
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"instruct",f)
  if(h=="instruct2"):
   print("video set to instruct2")
   X=51
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"instruct2",f)
  if(h=="charge1"):
   print("video set to charge1")
   X=66
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"charge1",f)
  if(h=="charge2"):
   print("video set to charge2")
   X=81
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"charge2",f)
  if(h=="charge3"):
   print("video set to charge3")
   X=96
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"charge3",f)
  if(h=="charge4"):
   print("video set to charge4")
   X=111
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"charge4",f)
  if(h=="charge5"):
   print("video set to charge5")
   X=126
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"charge5",f)
  if(h=="chargesucc"):
   print("video set to chargesucc")
   X=141
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"chargesucc",f)
  if(h=="dispense"):
   print("video set to dispense")
   X=156
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"dispense",f)
  if(h=="dispense2"):
   print("video set to dispense2")
   X=171
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"dispense2",f)
  if(h=="fail"):
   print("video set to fail")
   X=186
   n=14
   p.set_position(X)
   f=X+n
   looper(X,"fail",f)
def idle():
 global h
 print("PROGRAM START")
 while(True):
  disable()
  h="idle"
  print("From idle thread:")
  print(h)
  J=A.readline()
  print(J)
  if(J==b"ultra\n"):
   print("Ultra detected")
   enable()
   Y.set()
   h="tappls"
   o.wait()
   o.clear()
def runseries():
 global h
 while(True):
  k.wait()
  k.clear()
  j.set()
  A.write(b'1')
  h="instruct"
  k.wait()
  k.clear()
  disable()
  h="instruct2"
  J=A.readline()
  if(J==b"yes\n"):
   print("Stage1 complete")
   h="charge1"
  J=A.readline()
  if(J==b"yes\n"):
   print("Stage2 complete")
   h="charge2"
  J=A.readline()
  if(J==b"yes\n"):
   print("Stage3 complete")
   h="charge3"
  J=A.readline()
  if(J==b"yes\n"):
   print("Stage4 complete")
   h="charge4"
  J=A.readline()
  if(J==b"yes\n"):
   print("Stage5 complete")
   h="charge5"
  elif(J==b"no\n"):
   pass
  A.readline()
  print("Stage6 complete")
  J=A.readline()
  b(3)
  if(J==b"succ\n"):
   print("SUCCESS DISPENSE")
   h="chargesucc"
   b(2)
   h="dispense"
   b(5)
   h="dispense2"
   b(5)
  elif(J==b"fail\n"):
   h="fail"
   b(6)
   print("FAIL NO DISPENSE")
   pass
  b(5)
  o.set()
D=threading.Thread(target=idle)
m=threading.Thread(target=runseries)
r=threading.Thread(target=watchdog)
E=threading.Thread(target=seeking)
k=threading.Event()
Y=threading.Event()
j=threading.Event()
y=threading.Event()
o=threading.Event()
H=threading.Event()
F=tk.Button(e,text='TAP',font=myFont,command=tap,height=90,width=190)
F.grid(row=1,column=1,sticky=tk.NSEW)
G=tk.Button(e,text='BYPASS',font=myFont,command=ultrabypass,height=90,width=20)
G.grid(row=1,column=0,sticky=tk.NSEW)
if __name__=='__main__':
 D.start()
 m.start()
 r.start()
 E.start()
 e.mainloop()
 print("EXIT EXIT")


