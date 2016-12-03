import tkinter
import speech_recognition as sr
from tkinter import *
from AI import *
from Database import *
from NLG import *
from TTS import *
from Dialogue_Manager import *
from speech_recognizer import *



class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    def initialize(self):

        self.wlabelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.wlabelVariable,anchor="w",fg="red",bg="yellow")
        label.pack()
        self.wlabelVariable.set(u"Welcome to Dialogue Manager!")


        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.pack()
        self.user=StringVar()
        self.syst=StringVar()
        button = tkinter.Button(self,text=u"Send Inquiry!",command=self.OnButtonClick)
        button.pack()
        self.text1=Text(self)
        self.text1.pack()

        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClick(self):
        r = sr.Recognizer()
        NLUDict={}
        DialogDict={}
        NLGO=""
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            text=speechDetector.detect(audio)
        except Exception as e:
            text="Cannot function properly"

        NLUDict=testClassifyNLU.nluClassifier(text)
        DialogDict=dialogmanager.dm(NLUDict)
        NLGO=nlg.getInfo(DialogDict)
        self.entryVariable.set(text)
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.user.set(text)
        self.syst.set(NLGO)
        self.text1.insert(END , 'USER :'+self.user.get()+'\n')

        self.text1.insert(END , 'SYSTEM :'+self.syst.get()+'\n')

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Dialog Model')
    app.mainloop()