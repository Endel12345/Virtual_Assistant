#pip install pyttsxt
#pip install SpeechRecognition
#pip install pyaudio

#import modules
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os

#create TTS engine
engine = pyttsx3 .init()
engine.setProperty('rate', 175)


def speak(text):
    print("Assistant: " , text)
    engine.say(text)
    engine.runAndWait()

#take command fun
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said: " , command)
            return command
        except Exception as e:
            return ""
        
#command taking fun
def run_assistant():
    command = take_command()
        #if command contains "date"
    if "date" in command:
        date = datetime.datetime.now()
        speak(f"Today's date is{date}")
    #if command is open notepad
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system('notepand')
         
    #open youtube in command
    elif 'open youtube' in command:
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")
        
    elif 'okay siri' in command:
        query = command.replace('ok siri', '')
        google_url = f"https://www.google.com/search?q={query}"
        speak(f"Opening {query} on google")
        webbrowser.open(google_url)
        
    elif 'stop' in command:
        speak("Goodbye !")
    else:
        print("Give command like open youtube,open notepad, or ask any question")
        

#main fun
if __name__ == "__main__":
    speak("hey,how are you,today i will assist for your queryes")
    run_assistant()



            
            
         




