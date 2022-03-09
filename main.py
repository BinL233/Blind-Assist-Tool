import message
import Record
import os


def main():
    print("Tell me the website after the beep")
    qSound = "Tell me the website after the beep"
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


if __name__ == '__main__':

    # Install pyaudio wheel
    #os.system("pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl")

    AutoSearch = message.AutoSearch()

    main()
