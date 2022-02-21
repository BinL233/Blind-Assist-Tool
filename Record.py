import speech_recognition as sr
from playsound import playsound

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Record")
        playsound("Audio/Bi.mp3")
        audio = r.listen(source)
    data = ""
    try:
        print('1')
        data = r.recognize_google(audio)
        print('2')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
    return data
