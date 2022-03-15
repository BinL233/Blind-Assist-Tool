import speech_recognition as sr
from playsound import playsound
import keyboard

def recordAudio():
    r = sr.Recognizer()

    while True:

        if keyboard.read_key() != '': 

            with sr.Microphone() as source:
                print("Start Record")
                playsound("Audio/Bi.mp3")
                audio = r.listen(source)
            data = ""
            try:
                data = r.recognize_google(audio)
                print("You said: " + data)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Speech Recognition service; {0}".format(e))
            return data

        else:
            pass
