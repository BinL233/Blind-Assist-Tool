import message
import Record
import os
import gtts
from playsound import playsound


def main():
    print("\nTell me the website after the beep")
    qSound = "Tell me the website after the beep"
    AutoSearch = message.AutoSearch()
    AutoSearch.webSound(qSound)
    #browser = input("what website do you want to see(ebay or amazon)?")
    data = Record.recordAudio()

    # Find website from sound file
    if data.lower() == "amazon":
        AutoSearch.amazon()
    if data.lower() == "ebay":
        AutoSearch.ebay()
    if data.lower() == "target":
        AutoSearch.target()
    else:
        AutoSearch.error()
        main()


def start():
    # Install pyaudio wheel
    #os.system("pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
    #print("Please press space to start")
    #start = gtts.gTTS("Please press space to start")
    # start.save("Audio/start.mp3")
    # playsound("Audio/start.mp3")
    # os.remove("Audio/start.mp3")
    '''
    if keyboard.read_key() == 'space':
        time.sleep(2)
        main() 

    else:
        pass

    '''

    print('If you want to speak, please press any key for speaking.')
    speak = gtts.gTTS(
        'If you want to speak, please press any key for speaking')
    speak.save("Audio/speak.mp3")
    playsound("Audio/speak.mp3")
    os.remove("Audio/speak.mp3")

    main()
