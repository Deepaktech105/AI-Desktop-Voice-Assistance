import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecongnition
import datetime
import wikipedia   #pip install wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    print(datetime.datetime.now())
    print((datetime.datetime.now().second))
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("Hare Krishna!")

    else:
        speak("good evening")
        speak("i am AI Assistance. please tell me how may i help you")


def takecommand():
    # it take microphone input from the user and return strig output

    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(s)
        print("listening ended|")
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print('Now logining..')
    server.login('Sender email','Sender Password')
    print('logged in')
    server.sendmail('Sender email', to, content)
    server.close()

query = ""
if __name__ == "__main__":
    wishme()
    while True:
        #if 1:
        query = takecommand().lower()
        # print("Variendra is good boy")

        # logic for executing tasks  based on query
        if 'wikipedia' in query:
                speak('searching wikipedia.....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
        elif 'open youtube' in query:
                webbrowser.open("youtube.com")  

        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
                music_dir = 'C:\\Users\\Krishna\\OneDrive\\Desktop\\Jarvis\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
                codePath = "D:\\Setup\\Microsoft VS Code\\code.exe"
                os.startfile(codePath)

        elif 'email to deepak' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                # speak("Tell me receiver email id")
                # to = 'deepak10sonu@gmail.com'
                to = 'Receive mail'
                sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Deepak Kumar. I am not able to send this email")
        elif 'exit' in query:
            speak("Take care Deepak sir! Good bye!")
            break
