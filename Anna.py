from email.mime import audio
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
okay jannu


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
     hour = int(datetime.datetime.now().hour)
     if hour>0 and hour<12:
         speak("good morning!")
     elif hour>=12 and hour<18:
         speak("good afternoon!")
     else:
         speak("good evening!")

     speak("I am Anna!. please let me know how can i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 0.5
        audio = r.listen(source,None,5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")

    except exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
   # speak("great")
    wish()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'introduce yourself' in query:
            speak(
                "Hello! I Am ANNA built By Alen, Nikhil, Nisarg and  Arsh Technology used Pycharm for backend and PyQT5  for frontend and will surely will be in use after i get my features upgraded.")

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C://Users//pooja//Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open word' in query:
            speak("Opening Word")
            subprocess.call('C://Program Files//Microsoft Office//root//Office16//WINWORD.exe')

        elif 'open excel' in query:
            speak("Opening Excel")
            subprocess.call('C://Program Files//Microsoft Office//root//Office16//EXCEL.exe')

        elif 'open notepad' in query:
            speak("Opening notepad")
            subprocess.call('notepad.exe')

        elif 'quit' in query:
            exit()