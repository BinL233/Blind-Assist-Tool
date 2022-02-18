import message
import Record
import os


def main():
    print("please tell me the website you want to view")
    print("You can speak after the beep")
    qSound = "Please tell me the website you want to view"
    qSound2 = "You can speak after the beep"
    AutoSearch.webSound(qSound)
    AutoSearch.webSound(qSound2)
    #browser = input("what website do you want to see(ebay or amazon)?")
    data = Record.recordAudio()

    #Find website from sound file
    if data.lower() == "amazon":
        AutoSearch.amazon()
    if data.lower() == "ebay":
        AutoSearch.ebay()
    if data.lower() == "costco":
        AutoSearch.costco()
    else:
        AutoSearch.error()
        main()


if __name__ == '__main__':
    AutoSearch = message.AutoSearch()
    
    #Check whether gtts mp3 files are not exist
    if os.path.exists("Audio/web.mp3") == True:
        os.remove("Audio/web.mp3")

    if os.path.exists("Audio/prod.mp3") == True:
        os.remove("Audio/prod.mp3")

    if os.path.exists("Audio/error.mp3") == True:
        os.remove("Audio/error.mp3")

    if os.path.exists("AUdio/ann.mp3") == True:
        os.remove("Audio/ann.mp3")

    if os.path.exists("Audio/ann2.mp3") == True:
        os.remove("Audio/ann2.mp3")

    if os.path.exists("Audio/ann3.mp3") == True:
        os.remove("Audio/ann3.mp3")

    if os.path.exists("Audio/ann4.mp3") == True:
        os.remove("Audio/ann4.mp3")

    if os.path.exists("AUdio/search_success.mp3") == True:
        os.remove("Audio/search_success.mp3")

    main()
