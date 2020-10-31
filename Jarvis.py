import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import datetime
import smtplib
# import time
# import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!!")

    elif hour>12 and hour<=15:
        speak("Good Afternoon!!")

    elif hour>=15 and hour<=18:
        speak("Good Evening!!")

    else:
        speak("Good Night")

    speak("I am jarvis. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        # speak(audio)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Naveen said : {query}\n")
        speak(f"Naveen said : {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Enter your Gmail', 'Password')
    server.sendmail('Enter your Gmail', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    # speak("Naveen is my originator ")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            # print(result)
            speak(result)

        elif 'youtube' in query:
            search = query.split(" ")[1]
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.get().open(url)

        elif 'google' in query:
            search = query.split(" ")[1]
            webbrowser.get().open(f"https://google.com/search?q={search}")

        elif 'ptu result' in query:
            webbrowser.open("m.ptuexam.com")


        # elif 'google' in query:
        #     search = query.split(" ")[1]
        #     webbrowser.get().open(f"https://google.com/search?q={search}")


        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'whatsaap' in query:
            webbrowser.open("https://web.whatsapp.com/share?url=")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'music' in query:
            music_dir = 'E:\\Music\\Old Song'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")

        elif 'pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(codepath)

        elif 'how are you' in query:
            speak("fine sir! and what about you")

        elif 'good' in query:
            speak("great sir")

        elif 'not good' in query:
            speak("please take a rest sir and medicine also")

        elif 'favourite movie' in query:
            speak("Mohabbatein")

        elif 'who is the father robot' in query:
            speak("Naveen")

        elif 'father of naveen' in query:
            speak("hemant kumar")

        elif 'family member' in query:
            speak("there are four member ")

        elif 'president' in query:
            speak("Ram Nath Kovind")

        elif 'corona' in query:
            speak("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")

        elif 'safe' in query:
            speak("Maintain at least 1 metre (3 feet) distance between yourself and others. and Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water")

        elif 'who are you' in query:
            speak("I am robot and be safe stay home and stay safe at your home")

        elif 'naveen and navin' in query:
            speak("he is my originator. and he is a great man and also a fun loving guys and i know his secret hahahaha... but i don't tell you")

        elif 'friend' in query:
            speak("naveen have many friend like dwarika, shiva, shyam, anand, pawan")

        elif 'girlfriend' in query:
            speak("all are Secret i have not permission to tell you")

        elif 'brother and sister' in query:
            speak("vishakha kumari khushi kumari aastha kumari anand kumar seema kumari sawan kumar.! these all are brother and sister")

        elif 'birthday' in query:
            x = datetime.datetime.now().strftime("%m-%d")
            if x == "04-25":
                speak("Happy Birthday sir!!")
            else:
                speak("Today is not you birthday")

        elif 'calculator' in query:
            speak("what you want like addition,subtraction,multiplication and division")

        elif 'addition' in query:
            speak("enter first number")
            x=int(input())
            speak("enter second number")
            y=int(input())
            add=x+y
            speak(add)

        elif 'subtraction' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            sub=x-y
            speak(sub)

        elif 'multiplication' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            mul=x-y
            speak(mul)

        elif 'division' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            div=x/y
            speak(div)

        elif 'detail' in query:
            f = open("detail.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'shayari' in query:
            f = open("shayari.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'quotes' in query:
            f = open("quotes.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'poem' in query:
            f = open("poem.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'company' in query:
            f = open("company.txt")
            content = f.read()
            speak(content)
            f.close()

        # elif 'notes' in query:
        #     f = open("abc.txt", "w")
        #     content = f.write(speak())
        #     speak(content)
        #     f.close()

        elif 'email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'Enter Gmail whom to send'
                sendEmail(to, content)
                print("email has been send")
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry my friend naveen. i am not able too send this email")


        elif 'quit' in query:
            speak("Happy to serve you sir!")
            exit()
