import pyttsx3  # converts text to voice
import datetime
import speech_recognition as sr  #for speech recognition
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui #for screenshot
import pyjokes
from translate import Translator


engine = pyttsx3.init()


def speak(audio):        #what ever we want to convert into audio
    engine.say(audio)    #text to speech
    engine.runAndWait()  #till finish speaking



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back sir!")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<24:
        speak("good evening Sir!")
    else:
        speak("good night sir")
    speak("Mark45 reporting to you and please tell me how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # waits 1 second and listen to audio
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query  = r.recognize_google(audio,language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query

def sentEmail(to,content): #to=receviers email id and content of the mail
    server = smtplib.SMTP('smtp.gmail.com',587) #use our gmail to send & port gamil usally uses 587 port
    server.ehlo()
    server.starttls()
    server.login('painamswaroopkumar@gmail.com','Yugalika@134')
    server.sendmail('painamswaroopkumar@gmail.com', to, content)
    server.close() 

def screenShot():
    img = pyautogui.screenshot()
    img.save("E:\\Mark45\\ss.png")

def joke ():
    speak(pyjokes.get_joke())




    
if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("it is searching..")
            query = query.replace("wikipedia","") #want to search specific word and removing wikipedia
            result = wikipedia.summary(query,sentences= 2) #sumary of search and returns second sentence of it
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what message that you want to sent")
                content = takeCommand()
                speak(content)
                to = 'ravindrareddy9875@gamil.com'
                sentEmail(to, content)
                speak("Email successfully sent")
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'search' in query:
            speak("what should i search ?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system("shutdown-1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'remember that' in query:
            speak("what should i remember..")
            data = takeCommand()
            speak("You said to me to remember that" +data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that" + remember.read())
        elif 'screenshot' in query:
            screenShot()
            speak("The screenshot has taken")
        elif 'joke' in query:
            joke()
        elif 'translate' in query:
            text = takeCommand()
            translator = Translator(to_lang="fr")
            translation = translator.translate(text)
            translated_text = translation
            speak(translated_text)
        elif "offline" in query:
            quit() 