import message
import Record

AutoSearch = message.AutoSearch()


def main():
    print("please tell me the website you want to view")
    print("You can speak after hearing the sound")
    qSound = "Please tell me the website you want to view"
    qSound2 = "You can speak after the sound"
    AutoSearch.webSound(qSound)
    AutoSearch.webSound(qSound2)
    #browser = input("what website do you want to see(ebay or amazon)?")
    data = Record.recordAudio()
    if data.lower() == "amazon":
        AutoSearch.amazon()
    if data.lower() == "ebay":
        AutoSearch.ebay()
    else:
        AutoSearch.error()
        main()


if __name__ == '__main__':
    main()
