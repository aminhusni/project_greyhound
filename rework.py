import threading
import tkinter as tk
import tkinter.font
from PIL import ImageTk
import serial
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
G=tk.Tk()
G.title("PROJECT GREYHOUND")
G.attributes("-fullscreen",True)
c=tk.PhotoImage(file="/home/pi/Desktop/projectvideo/background.png")
q=tkinter.font.Font(family='Helvetica',size=12,weight="bold")
H=serial.Serial('/dev/ttyUSB0',9600)
B="null"
L=Path("/home/pi/Desktop/projectvideo/full.mp4")
o=0
X=OMXPlayer(L,args=["--orientation","90","--loop","--no-osd"],dbus_name='org.mpris.MediaPlayer2.omxplayer0')
def disable():
 r.config(state=tk.DISABLED)
def enable():
 r.config(state=tk.NORMAL)
def watchdog():
 while(True):
  print("watchdog ended")
  f.wait()
  u.clear()
  print("watchdog started")
  f.clear()
  m(15)
  if(not u.isSet()):
   print("timeout")
   serial.write(b'r')
   K.set()
def tap():
 o.set()
def ultrabypass():
 serial.write(b'8')
def looper(v,videoname,T):
 print("Looper active")
 print("Video name: "+videoname)
 print("Start pos: "+str(v))
 global B
 while(True):
  m(0.01)
  y=X.position()
  if(y>=T):
   print("Relooping back to:"+str(v))
   X.set_position(v)
  if(videoname!=B):
   print("Video changed!")
   break
def seeking():
 global B
 print("Seeking thread started")
 m(1)
 print(B)
 while(True):
  m(1)
  print("From seeking thread:")
  print(B)
  if(B=="idle"):
   print("video set to idle")
   v=0
   i=19
   X.set_position(v)
   T=v+i
   looper(v,"idle",T)
  if(B=="tappls"):
   print("video set to tappls")
   v=21
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"tappls",T)
  if(B=="instruct"):
   print("video set to instruct")
   v=36
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"instruct",T)
  if(B=="instruct2"):
   print("video set to instruct2")
   v=51
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"instruct2",T)
  if(B=="charge1"):
   print("video set to charge1")
   v=66
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"charge1",T)
  if(B=="charge2"):
   print("video set to charge2")
   v=81
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"charge2",T)
  if(B=="charge3"):
   print("video set to charge3")
   v=96
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"charge3",T)
  if(B=="charge4"):
   print("video set to charge4")
   v=111
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"charge4",T)
  if(B=="charge5"):
   print("video set to charge5")
   v=126
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"charge5",T)
  if(B=="chargesucc"):
   print("video set to chargesucc")
   v=141
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"chargesucc",T)
  if(B=="dispense"):
   print("video set to dispense")
   v=156
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"dispense",T)
  if(B=="dispense2"):
   print("video set to dispense2")
   v=171
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"dispense2",T)
  if(B=="fail"):
   print("video set to fail")
   v=186
   i=14
   X.set_position(v)
   T=v+i
   looper(v,"fail",T)
def idle():
 global B
 print("PROGRAM START")
 while(True):
  disable()
  B="idle"
  print("From idle thread:")
  print(B)
  D=serial.readline()
  print(D)
  if(D==b"ultra\n"):
   print("Ultra detected")
   enable()
   f.set()
   B="tappls"
   K.wait()
   K.clear()
def runseries():
 global B
 while(True):
  o.wait()
  o.clear()
  u.set()
  serial.write(b'1')
  B="instruct"
  o.wait()
  o.clear()
  disable()
  B="instruct2"
  D=serial.readline()
  if(D==b"yes\n"):
   print("Stage1 complete")
   B="charge1"
  D=serial.readline()
  if(D==b"yes\n"):
   print("Stage2 complete")
   B="charge2"
  D=serial.readline()
  if(D==b"yes\n"):
   print("Stage3 complete")
   B="charge3"
  D=serial.readline()
  if(D==b"yes\n"):
   print("Stage4 complete")
   B="charge4"
  D=serial.readline()
  if(D==b"yes\n"):
   print("Stage5 complete")
   B="charge5"
  elif(D==b"no\n"):
   pass
  serial.readline()
  print("Stage6 complete")
  D=serial.readline()
  m(3)
  if(D==b"succ\n"):
   print("SUCCESS DISPENSE")
   B="chargesucc"
   m(2)
   B="dispense"
   m(5)
   B="dispense2"
   m(5)
  elif(D==b"fail\n"):
   B="fail"
   m(6)
   print("FAIL NO DISPENSE")
   pass
  m(5)
  K.set()
a=threading.Thread(target=idle)
h=threading.Thread(target=runseries)
j=threading.Thread(target=watchdog)
W=threading.Thread(target=seeking)
o=threading.Event()
f=threading.Event()
u=threading.Event()
E=threading.Event()
K=threading.Event()
F=threading.Event()
r=tk.Button(G,text='TAP',font=myFont,command=tap,height=90,width=190)
r.grid(row=1,column=0,sticky=tk.NSEW)
Q=tk.Button(G,text='BYPASS',font=myFont,command=ultrabypass,height=90,width=20)
Q.grid(row=1,column=1,sticky=tk.NSEW)
if __name__=='__main__':
 a.start()
 h.start()
 j.start()
 W.start()
 G.mainloop()
 print("EXIT EXIT")