import pyttsx3
from tkinter import *
from functools import partial
# from bs4 import BeautifulSoup
# import requests
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    # speak("hello sir,how are you! Jarvis here...")
    root=Tk()
    root.title("READ IT ALOUD JARVIS")
    root.geometry("400x600")
    frame1=Frame(root,bg="#f4a460")
    text="Andre Russell claimed a five-wicket haul to register his best IPL bowling figures as Kolkata Knight Riders\n bowled out Mumbai Indians for 152 at MA Chidambaram Stadium in Chennai.\n Russell returned with the figures of 5/15 in 2 overs to register\n his best bowling figures in IPL. Suryakumar Yadav top-scored \nwith 56 off 36 balls while the MI captain contributed with 43 off 32\n balls. Earlier, KKR won the toss and opted to field first. KKR had a \nterrific start to their campaign as they defeated SRH in their previous \nencounter. MI, on the other hand, would be desperate to register\n their first win of the season after losing the season opener to RCB.\n"
    text1=text.split("\n")
    # print(text1)

    l1=Label(frame1,text="PRANAV'S eDGE",bg="#f4a460",fg="white",font="Helvetia 10 bold")
    l1.pack()
    frame1.pack(fill=X)
    frame2=Frame(root,bg="brown")
    frame2.pack(expand=True,fill=BOTH)
    bt1=Button(frame2,text="Speak")
    bt1.place(relheight=0.1,relwidth=0.15,rely=0.83,relx=0.8)
    listbox=Listbox(frame2)
    listbox.place(relheight=0.8,relwidth=1,rely=0.001)
    scroll=Scrollbar(listbox)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=listbox.yview)
    scroll1 = Scrollbar(listbox)
    scroll1.pack(side=BOTTOM, fill=X)
    scroll1.config(command=listbox.xview)
    listbox.config(yscrollcommand=scroll.set,xscrollcommand=scroll1.set)

    # listbox.config(xscrollcommand=scroll1.set)
    for item in text1:
        listbox.insert(END,f"{item}")


    root.mainloop()
