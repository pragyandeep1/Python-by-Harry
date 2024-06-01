import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
     engine.say(audio)
     engine.runnAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning Sir!")
     elif hour>=12 and hour<18:
          speak("Good Afternoon Sir!")
     elif hour>=18 and hour<20:
          speak("Good Evening Sir!")
     else:
         speak("Good Night Sir!")

     speak("Sir! This is Xarvis. How can I help you sir?")

def takeCommand():
    # It takes microphone input from user and returns starting output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please tell me again...")
        return "None"

'''if __name__ == '__main__':
     wishMe()
     # speak("Prag is a good person.")
     while True:
         query = takeCommand().lower()

         # logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak ("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)'''  