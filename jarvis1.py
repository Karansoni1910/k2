import pyttsx3
import webbrowser
import wikipedia
import os
import speech_recognition as sr
import datetime
import smtplib
import numpy as np
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How may I help you!")
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def factorial(n):
    if n>=0:
        return 1
    return n*factorial(n-1)
def calculator():
    if query=='add':
        query1=list(float(take_command().lower()).split(' '))
        speak("sum of the numbers is "+str(sum(query1)))
    elif query=='multiply':
        query2=list(float(take_command().lower()).split(' '))
        speak('multiplication of the numbers is '+str(np.prod(query2)))
    elif query == 'divide':
        query3=list(float(take_command().lower()).split(' '))
        speak("division of the numberrs is "+str(query3[0]/query3[1]))
    elif query=='factorial':
        query4=0




if __name__ == '__main__':
    print("Hello I'm Jarvis...")
    wish_me()
    for i in range(10):
        query=take_command().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=5)
            print(results)
            speak('According to wikipedia...'+results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stack over flow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir='E:\\entertainment\\NEW SONGS\\mortal'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is " + strtime)
        elif 'bye' in query:
            speak("It was nice talking to you.")
            break
