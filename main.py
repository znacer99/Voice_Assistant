import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pygetwindow as gw
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("so ?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zehinacer99@gmail.com', '367115')
    server.sendmail('znacer99@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open tell me' in query:
            webbrowser.open("https://www.youtube.com/watch?v=hBUaUGkU97Q&list=RDhBUaUGkU97Q&s tart_radio=1")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play jericho' in query:
            webbrowser.open("https://open.spotify.com/intl-fr/track/4ztdjZ2t7BVo5DLIFQBdJh?si=cf46a55619894f91")

        elif 'play starboy' in query:
            webbrowser.open("https://open.spotify.com/intl-fr/track/7MXVkk9YMctZqd1Srtv4MB?si=7624c0732b594971")

        elif 'party' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Y8qPp4pBNz8")
            
        elif 'lose yourself please' in query:
            webbrowser.open("https://www.youtube.com/watch?v=_Yhyp-_hX2s")

        elif 'no no close it' in query:
            # Close the browser window that was opened with 'open tell me'
            try:
                browser_window = gw.getWindowsWithTitle("YouTube")[0]  # Replace "YouTube" with the actual window title
                browser_window.close()
                speak("Closed the 'open tell me' window")
            except IndexError:
                speak("Window not found")

        elif 'play valorant' in query:
            valorant_path = r'"C:\Riot Games\Riot Client\RiotClientServices.exe"'
            os.startfile(valorant_path)
        
        elif 'open arduino' in query:
            arduino_path = r'"C:\Users\zehin\OneDrive\Bureau\Arduino IDE.lnk"'
            os.startfile(arduino_path)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r'"C:\Users\zehin\OneDrive\Bureau\network protocol\voice.py"'
            os.startfile(codePath)

        elif 'email to myself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zehinacer99@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak('HEY THERE')    
        elif "thank you" in query:
              speak("its my pleasure")
        elif "quit" in query:
           break
        #else:
            #speak("Sorry,can't get that")
