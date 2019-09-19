import numpy as np
import cv2
import pickle
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
from time import *
import threading
from pygame import mixer
import pyautogui
import requests

mixer.init()
name = "abc"
dob_year = 2019
dob_month = 7
dob_date = 25

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

active_voice = "jarvis"


def weather():
    city = "bangalore"

    url = 'https://samples.openweathermap.org/data/2.5/weather?q=(),uk&appid=975b02324618962ef359cc9384e43e24'.format(
        city)
    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    speak('Temperature is {} fahrenheit'.format(temp))
    speak('Wind Speed is {} meter per second'.format(wind_speed))
    speak('Latitude is {}'.format(latitude))
    speak('Longitude is {}'.format(longitude))
    speak('Description is {}'.format(description))


def countdown():
    global my_timer
    my_timer = 10
    for x in range(10):
        my_timer = my_timer-1
        sleep(1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    speak("Welcome Sumant")
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis. How may I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in')
        print(f"You said :{query1}\n")

    except sr.UnknownValueError:
        print("Sorry could not recognize")
        speak("Sorry could not recognize")
        query1 = take_command().lower()
    return query1


def assistant():
    global active_voice
    while True:
        query = take_command().lower()
        if 'reset' in query:
            continue

        elif 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'youtube search' in query:
            speak("searching")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            query = query.replace("youtube search", "")
            f_text = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.get(chrome_path).open(f_text)

        elif 'google search' in query:
            speak("searching")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            query = query.replace("google search", "")
            f_text = 'https://www.google.com/search?q=' + query
            webbrowser.get(chrome_path).open(f_text)

        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = 'https://www.youtube.com'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = 'https://www.google.com'
            webbrowser.get(chrome_path).open(url)

        elif 'privacy' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
            url = 'https://www.google.com'
            webbrowser.get(chrome_path).open_new(url)
            continue

        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'weather' in query:
            weather()

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'quit'in query or 'stop' in query:
            sys.exit(0)

        elif 'hello' in query:
            speak("Hello sumant")

        elif 'who are you' in query:
            mixer.music.load("jarvis.wav")
            mixer.music.play()
            sleep(25)

        elif 'what is up' in query:
            speak("Nothing much!")

        elif 'whatsapp' in query:
            speak("Nothing much!")

        elif 'what is your name' in query:
            if active_voice == "jarvis":
                speak("My name is jarvis")
            else:
                speak("My name is friday")

        elif 'what is' in query:
            try:
                query = query.replace("what is", "")
                results = wikipedia.summary(query, sentences=2)
                speak(results)

            except Exception:
                speak("Sorry, does not match any pages")
                query = take_command().lower()

        elif 'how are you' in query:
            speak("I am fine")
            speak("what about you ?")

        elif 'play suits' in query:
            pyautogui.click(1241, 2)
            sleep(1)
            pyautogui.doubleClick(40, 465)
            sleep(1)
            pyautogui.doubleClick(567,380)
            sleep(1)
            pyautogui.doubleClick(281, 590)
            sleep(1)
            pyautogui.doubleClick(321, 205)
            sleep(30)
            pyautogui.press('esc')
            sleep(3)
            pyautogui.click(1348, 4)
            sleep(1)
            pyautogui.click(1348, 4)
            sleep(1)
            pyautogui.moveTo(755, 754)
            sleep(1)
            pyautogui.click(755, 754)
            continue

        elif 'switch to friday' in query:
            active_voice = "friday"
            speak("transferring control to friday")
            engine.setProperty('voice', voices[1].id)
            speak("Hello sumant")

        elif 'switch to jarvis' in query:
            active_voice = "jarvis"
            speak("Transferring control to jarvis")
            engine.setProperty('voice', voices[0].id)
            speak("hello sumant")

        elif 'joke' in query:
            speak("I used to be a werewoolf. But I'm much better noooow !")

        elif 'motivate' in query or 'quotes' in query:
            speak("The difference between men and boys is the price of their toys")

        elif 'wait' in query:
            sleep(10)

        elif 'age' in query:
            current_year = datetime.datetime.now().year
            current_month = datetime.datetime.now().month
            current_date = datetime.datetime.now().day
            age_year = str(current_year - dob_year)
            age_month = str(current_month - dob_month)
            age_day = str(current_date - dob_date)
            strr1 = "i am "+age_year
            strr2 = age_month + "months"
            strr3 = age_day + "days old"
            speak(strr1)
            speak("years")
            speak(strr2)
            speak(strr3)

        else:
            speak(query)


labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for(x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45 and conf <=60:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            if name == "sumanth":
                cap.release()
                cv2.destroyAllWindows()
                break
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)
    elif name == "sumanth":
        cap.release()
        cv2.destroyAllWindows()
        break
    elif my_timer <= 0:
        speak("Unauthorized access")
        speak("Try again")
        cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)

wish_me()
assistant()
