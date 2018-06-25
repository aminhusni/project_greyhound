import threading
u=True
g=print
L=str
N=threading.Thread
d=threading.Event
import tkinter as tk
R=tk.Tk
M=tk.NORMAL
S=tk.DISABLED
K=tk.NSEW
w=tk.PhotoImage
c=tk.Button
import tkinter.font
from PIL import ImageTk
import serial
a=serial.readline
X=serial.Serial
A=serial.write
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
h=R()
h.title("PROJECT GREYHOUND")
h.attributes("-fullscreen",u)
H=w(file="/home/pi/Desktop/projectvideo/background.png")
n=tkinter.font.Font(family='Helvetica',size=12,weight="bold")
r=X('/dev/ttyUSB0',9600)
J="null"
l=Path("/home/pi/Desktop/projectvideo/full.mp4")
j=0
z=OMXPlayer(l,args=["--orientation","90","--loop","--no-osd"],dbus_name='org.mpris.MediaPlayer2.omxplayer0')
def W():
 k.config(state=S)
def e():
 k.config(state=M)
def Y():
 while(u):
  g("watchdog ended")
  O.wait() 
  f.clear()
  g("watchdog started")
  O.clear()
  q(15)
  if(not f.isSet()):
   g("timeout")
   A(b'r')
   o.set()
def G():
 j.set()
def C():
 A(b'8')
def t(T,videoname,i):
 g("Looper active")
 g("Video name: "+videoname)
 g("Start pos: "+L(T))
 global J
 while(u):
  q(0.01)
  x=z.position()
  if(x>=i):
   g("Relooping back to:"+L(T))
   z.set_position(T)
  if(videoname!=J):
   g("Video changed!")
   break
def y():
 global J
 g("Seeking thread started")
 q(1)
 g(J)
 while(u):
  q(1)
  g("From seeking thread:")
  g(J)
  if(J=="idle"):
   g("video set to idle")
   T=0
   b=19
   z.set_position(T)
   i=T+b
   t(T,"idle",i)
  if(J=="tappls"):
   g("video set to tappls")
   T=21
   b=14
   z.set_position(T)
   i=T+b
   t(T,"tappls",i)
  if(J=="instruct"):
   g("video set to instruct")
   T=36
   b=14
   z.set_position(T)
   i=T+b
   t(T,"instruct",i)
  if(J=="instruct2"):
   g("video set to instruct2")
   T=51
   b=14
   z.set_position(T)
   i=T+b
   t(T,"instruct2",i)
  if(J=="charge1"):
   g("video set to charge1")
   T=66
   b=14
   z.set_position(T)
   i=T+b
   t(T,"charge1",i)
  if(J=="charge2"):
   g("video set to charge2")
   T=81
   b=14
   z.set_position(T)
   i=T+b
   t(T,"charge2",i)
  if(J=="charge3"):
   g("video set to charge3")
   T=96
   b=14
   z.set_position(T)
   i=T+b
   t(T,"charge3",i)
  if(J=="charge4"):
   g("video set to charge4")
   T=111
   b=14
   z.set_position(T)
   i=T+b
   t(T,"charge4",i)
  if(J=="charge5"):
   g("video set to charge5")
   T=126
   b=14
   z.set_position(T)
   i=T+b
   t(T,"charge5",i)
  if(J=="chargesucc"):
   g("video set to chargesucc")
   T=141
   b=14
   z.set_position(T)
   i=T+b
   t(T,"chargesucc",i)
  if(J=="dispense"):
   g("video set to dispense")
   T=156
   b=14
   z.set_position(T)
   i=T+b
   t(T,"dispense",i)
  if(J=="dispense2"):
   g("video set to dispense2")
   T=171
   b=14
   z.set_position(T)
   i=T+b
   t(T,"dispense2",i)
  if(J=="fail"):
   g("video set to fail")
   T=186
   b=14
   z.set_position(T)
   i=T+b
   t(T,"fail",i)
def F():
 global J
 g("PROGRAM START")
 while(u):
  W()
  J="idle"
  g("From idle thread:")
  g(J)
  p=a() 
  g(p)
  if(p==b"ultra\n"):
   g("Ultra detected")
   e()
   O.set()
   J="tappls"
   o.wait() 
   o.clear()
def Q():
 global J
 while(u):
  j.wait() 
  j.clear()
  f.set() 
  A(b'1')
  J="instruct"
  j.wait()
  j.clear()
  W()
  J="instruct2"
  p=a() 
  if(p==b"yes\n"):
   g("Stage1 complete")
   J="charge1"
  p=a() 
  if(p==b"yes\n"):
   g("Stage2 complete")
   J="charge2"
  p=a() 
  if(p==b"yes\n"):
   g("Stage3 complete")
   J="charge3"
  p=a() 
  if(p==b"yes\n"):
   g("Stage4 complete")
   J="charge4"
  p=a() 
  if(p==b"yes\n"): 
   g("Stage5 complete")
   J="charge5"
  elif(p==b"no\n"):
   pass
  a() 
  g("Stage6 complete")
  p=a() 
  q(3)
  if(p==b"succ\n"):
   g("SUCCESS DISPENSE")
   J="chargesucc"
   q(2)
   J="dispense"
   q(5)
   J="dispense2"
   q(5)
  elif(p==b"fail\n"):
   J="fail"
   q(6)
   g("FAIL NO DISPENSE")
   pass
  q(5)
  o.set()
P=N(target=F)
I=N(target=Q)
V=N(target=Y)
v=N(target=y)
j=d()
O=d()
f=d()
B=d()
o=d()
E=d()
k=c(h,text='TAP',font=myFont,command=G,height=90,width=190)
k.grid(row=1,column=0,sticky=K)
m=c(h,text='BYPASS',font=myFont,command=C,height=90,width=20)
m.grid(row=1,column=1,sticky=K)
if __name__=='__main__':
 P.start()
 I.start()
 V.start()
 v.start()
 h.mainloop()
 g("EXIT EXIT")


