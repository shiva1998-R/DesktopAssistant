from tkinter import *
from sys import exit

import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os

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
            audio=r.listen(source,phrase_time_limit=5)
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





