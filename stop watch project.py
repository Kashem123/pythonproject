from tkinter import *
import time
def Main():
    global root
    root = Tk()
    root.title("StopWatch made by @StudyMart")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    root.geometry("%dx%d+%d+%d"%(width,height,x,y))
    Top = Frame(root,width=400)
    Top.pack(side=Top)
    stopWatch = StopWatch(root)
    stopWatch.pack(side = Top)
    Bottom = Frame(root,width=400)
    Bottom.pack(side=BOTTOM)
    Start = Button(Bottom, text="START",command=stopWatch.Start,width=10,height=3)
    Start.pack(side=LEFT)
    Stop = Button(Bottom,text="STOP",command=stopWatch.Stop,width=10,height=3)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom,text="RESET",command=stopWatch.Reset,width=10,height=3)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom,text="EXIT",command=stopWatch.Exit,width=10,height=3)
    Exit.pack(side=LEFT)
    Title = Label(Top,text="StopWatch @studymart",font=("arial",24),fg="white",bg="black")
    Title.pack(fill=x)
    root.config(bg="black")
    root.mainloop()
class StopWatch(Frame):
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()
    def MakeWidget(self):
        timeText=Label(self,textvariable=self.timestr,font=("times nwe roman",45),fg="white",bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=x,expand=No,pady=5,padx=10)

    def Updater(self):
        self.nextTime=time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50,self.Updater)

    def SetTime(self,nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)
        self.timestr.set("%02d:%02d:%02d"%(minutes,seconds,miliSeconds))

    def Start(self):
        if self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning=1

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Exit(self):
        root.destroy()
        exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)






















