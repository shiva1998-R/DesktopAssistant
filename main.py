import tkinter as tk
import os
import shutil
import os.path
from tkinter.filedialog import askdirectory, askopenfile, askopenfilename

# voice assistant module
from tkinter import *
from sys import exit

import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime


import threading

# utilities for voice assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """
    Speaks audio
    """
    engine.say(audio)
    engine.runAndWait()


def command():
    """
    Listens to commands
    """
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=2)
            speak('Alexa: Listening...')
            audio=r.listen(source,phrase_time_limit=10)
            try:
                query = r.recognize_google(audio)
                speak(f"You said: {query}")
                return query
            except:
                speak("Try Again")


def clickVoiceAssistantButton():
    def VoiceAssistantButtonActions():
        while True:
            query = command().lower()  ## takes user command

            if 'name' in query:
                speak("Hello Machine! My  Name is Alexa")
            elif 'are you single' in query:
                answers = ['I am in a relationship with wifi',
                            'No, I love spending time thinking about my crush wifi']
                speak(random.choice(answers))
            elif 'hate' in query:
                speak("I hate when people called me a machine")
            elif 'love' in query:
                speak("I loves to chat with machines like you")
            ### time
            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f"It's {time} master")

            ### celebrity
            elif 'who is' in query:
                query = query.replace('who is', "")
                speak(wikipedia.summary(query, 2))

            ### Joke
            elif 'joke' in query:
                speak(pyjokes.get_joke())

            ### news
            elif 'news' in query:
                def trndnews():
                    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                    page = requests.get(url).json()
                    article = page["articles"]
                    results = []
                    for ar in article:
                        results.append(ar["title"])

                    results = results[:3]
                    speak("here are the top trending news....!!")
                    speak("Do yo want me to read!!!")
                    reply = command().lower()
                    reply = str(reply)
                    if reply == "yes":
                        speak(results)
                    else:
                        speak('ok!!!!')
                        pass

                trndnews()


            ### music
            elif 'music' in query:
                with open(r'C://Desktop Assistant/music_folder_location.txt') as f:
                    music_dir = f.read()
                songs = os.listdir(music_dir)
                song = random.randint(0, len(songs) - 1)
                print(songs[song])
                speak(f"playing {songs[song]}")
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "exit" in query:
                speak("Have a nice day ! ")
                break
            else:
                speak("I don't understand what you are saying")
    t=threading.Thread(target=VoiceAssistantButtonActions)
    t.daemon=True
    t.start()

def clickOpenApplicationsButton():

    speak('Opening Applications...')
    def OpenAppsActions():
        import subprocess
        with open(r'C://Desktop Assistant/app_exe_locations.txt') as f:
            lines=f.readlines()
            lines=[line.strip() for line in lines]
            for exe_location in lines:
                subprocess.Popen(exe_location)
    t=threading.Thread(target=OpenAppsActions)
    t.daemon = True
    t.start()


def clickMusicPlayerButton():

    speak('Playing music...')
    def PlayMusicActions():
        with open(r'C://Desktop Assistant/music_folder_location.txt') as f:
              music_dir = f.read()
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs) - 1)
        print(songs[song])
        speak(f"playing {songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))
    t=threading.Thread(target=PlayMusicActions)
    t.daemon = True
    t.start()


# Information to ask when installing app for first time 
# - C://Desktop Assistant/music_folder_location.txt
# C://Desktop Assistant/app_exe_locations.txt
# if os.path.isdir(r'C://Desktop Assistant'):
#     shutil.rmtree(r'C://Desktop Assistant', ignore_errors=True)

if not os.path.isdir(r'C://Desktop Assistant'):
    os.mkdir(r"C://Desktop Assistant")

    # Muisc part
    window=tk.Tk()
    window.title('Music folder location info')

    window.rowconfigure(list(range(3)),minsize=40,weight=1)
    window.columnconfigure(list(range(1)),minsize=100,weight=1)
    def open_folder():
        folder_name=askdirectory()
        lbl_flr_name['text']=f"You selected {folder_name}"
        with open(r'C://Desktop Assistant/music_folder_location.txt','w') as f:
            f.write(folder_name)

    lbl_info=tk.Label(master=window,text='Please select folder location of music files.',font=("TkDefaultFont", 20))
    btns_frame=tk.Frame(master=window)
    btns_frame.rowconfigure(0,weight=1)
    btns_frame.columnconfigure(list(range(2)),weight=1)
    btn_open=tk.Button(master=btns_frame,text='Open',command=open_folder,width=10,height=1,font=("TkDefaultFont", 15))
    btn_done=tk.Button(master=btns_frame,text='Done',command=lambda: window.destroy(),width=10,height=1,font=("TkDefaultFont", 15))
    btn_open.grid(row=0,column=0,padx=5,pady=5)
    btn_done.grid(row=0,column=1,padx=5,pady=5)

    lbl_flr_name=tk.Label(master=window,text='Selected folder will be displayed here.',font=("TkDefaultFont", 10))

    lbl_info.grid(row=0,column=0,padx=5,pady=5)
    btns_frame.grid(row=1,column=0,padx=5,pady=5,sticky='nsew')
    lbl_flr_name.grid(row=2,column=0,padx=5,pady=5)

    height=400
    width=600
    window.geometry(f'{width}x{height}')
    window.mainloop()


    # Applications part
    window=tk.Tk()
    window.title('App exes location info')

    window.rowconfigure(list(range(3)),minsize=40,weight=1)
    window.columnconfigure(list(range(1)),minsize=100,weight=1)
    def open_file():
        file_name=askopenfilename()
        if lbl_file_names['text']=='Selected files will be displayed here.':
            lbl_file_names['text']=f"You selected:\n{file_name}"
        else:
            lbl_file_names['text']+=f"\n{file_name}"

        mode = 'r+' if os.path.exists(r'C://Desktop Assistant/app_exe_locations.txt') else 'w'
        with open(r'C://Desktop Assistant/app_exe_locations.txt',mode) as f:
            if mode=='w':
                write_text=file_name
            if mode=='r+':
                lines=f.readlines()
                lines=[line.strip() for line in lines]
                if file_name in lines:
                    write_text=''
                else:
                    write_text='\n'+file_name
            f.write(write_text)

    lbl_info=tk.Label(master=window,text='Please select file locations of app executables.',font=("TkDefaultFont", 20))
    btns_frame=tk.Frame(master=window)
    btns_frame.rowconfigure(0,weight=1)
    btns_frame.columnconfigure(list(range(2)),weight=1)
    btn_open=tk.Button(master=btns_frame,text='Open',command=open_file,width=10,height=1,font=("TkDefaultFont", 15))
    btn_done=tk.Button(master=btns_frame,text='Done',command=lambda: window.destroy(),width=10,height=1,font=("TkDefaultFont", 15))
    btn_open.grid(row=0,column=0,padx=5,pady=5)
    btn_done.grid(row=0,column=1,padx=5,pady=5)
    lbl_file_names=tk.Label(master=window,text='Selected files will be displayed here.',font=("TkDefaultFont", 10))

    lbl_info.grid(row=0,column=0,padx=5,pady=5)
    btns_frame.grid(row=1,column=0,padx=5,pady=5,sticky='nsew')
    lbl_file_names.grid(row=2,column=0,padx=5,pady=5)

    height=400
    width=600
    window.geometry(f'{width}x{height}')
    window.mainloop()

window=tk.Tk()
window.title('Desktop Assistant')

# configuring main window cells properties
window.rowconfigure(0,minsize=100,weight=1)
window.columnconfigure(0,minsize=200,weight=1)

# configuring buttons frame cells properties
btns_frame=tk.Frame(master=window,relief=tk.RAISED, bd=3)
btns_frame.rowconfigure(0,weight=1)
btns_frame.columnconfigure(list(range(3)),weight=1)

# Adding buttons
btn_voice_ass = tk.Button(master=btns_frame,text='Voice Assistant 🎤',command= clickVoiceAssistantButton,font=("TkDefaultFont", 15))
btn_open_apps=tk.Button(master=btns_frame,text='Open Applications',command= clickOpenApplicationsButton,font=("TkDefaultFont", 15))
btn_music_player=tk.Button(master=btns_frame,text='Play music',command= clickMusicPlayerButton,font=("TkDefaultFont", 15))

# Placing buttons
btn_voice_ass.grid(row=0,column=0)
btn_open_apps.grid(row=0,column=1)
btn_music_player.grid(row=0,column=2)
# Placing frame
btns_frame.grid(row=0, column=0,sticky='nsew')

# starting mainloop
height=400
width=700
window.geometry(f'{width}x{height}')
window.mainloop()