from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gtts
from playsound import playsound
import os
import Record

class AutoSearch:

    def __init__(self):
        self.search = None
    
    def webSound(self, q):
        web = gtts.gTTS(q)
        web.save("Audio/web.mp3")
        playsound("Audio/web.mp3")
        os.remove("Audio/web.mp3")

    def prodSound(self, q):
        prod = gtts.gTTS(q)
        prod.save("Audio/prod.mp3")
        playsound("Audio/prod.mp3")
        os.remove("Audio/prod.mp3")

    def error(self):
        error = gtts.gTTS("I'm not sure I understand. Please say that again.")
        error.save("Audio/error.mp3")
        playsound("Audio/error.mp3")
        os.remove("Audio/error.mp3")

    def elementSearch(self):
        for x in range(0,999):
            print("please tell me what product you are looking for")
            print("You can speak after hearing the b sound")
            qSound = "please tell me what product you are looking for"
            qSound2 = "You can speak after hearing the b sound"
            self.prodSound(qSound)
            self.prodSound(qSound2)
            #search = input("What product do you want to see?")

            #Record
            self.search = Record.recordAudio()

            if self.search == '':
                self.error()
            
                return self.elementSearch()

            print("You are looking for " + self.search + ", right?")
            ann2 = gtts.gTTS("You are looking for " + self.search + ", right?")
            ann2.save("Audio/ann2.mp3")
            playsound("Audio/ann2.mp3")
            os.remove("Audio/ann2.mp3")

            print("Please say yes or no after hearing the b sound")
            ann3 = gtts.gTTS("Please say yes or no after hearing the b sound")
            ann3.save("Audio/ann3.mp3")
            playsound("Audio/ann3.mp3")
            os.remove("Audio/ann3.mp3")

            ans = Record.recordAudio()

            
            if ans == 'yes':
                #Waiting audio
                print("Okay...Give me one second")
                ann = gtts.gTTS("Okay...Give me one second")
                ann.save("Audio/ann.mp3")
                playsound("Audio/ann.mp3")
                os.remove("Audio/ann.mp3")
                break

            elif ans == 'no':
                return self.elementSearch()

            else:
                print("Sorry, I did hear that. Could you repeat again?")
                ann4 = gtts.gTTS("Sorry, I did hear that. Could you repeat again?")
                ann4.save("Audio/ann4.mp3")
                playsound("Audio/ann4.mp3")
                os.remove("Audio/ann4.mp3")

    def searchSuccess(self):
        search_success = gtts.gTTS(self.search + " search success!")
        search_success.save("Audio/search_success.mp3")
        playsound("Audio/search_success.mp3")
        os.remove("Audio/search_success.mp3")

    def amazon(self):
        self.elementSearch()

        web = webdriver.Chrome()
        web.get("https://www.amazon.com/")

        x = 500
        while x < 4500:
            web.execute_script("window.scrollTo(0," + str(x) + ")")
            x += 100
            time.sleep(0.05)

        fill_in = web.find_element_by_xpath(
            "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        fill_in.send_keys(self.search)
        time.sleep(1)
        button = web.find_element_by_id("nav-search-submit-button")
        button.click()

        #Search success audio
        self.searchSuccess()

        sort = web.find_element_by_id("a-autoid-0-announce")
        sort.click()
        time.sleep(1)
        customer_review = web.find_element_by_id("s-result-sort-select_3")
        customer_review.click()
        time.sleep(600)


    def ebay(self):
        
        
        self.elementSearch()



        web = webdriver.Chrome()
        web.get("https://www.ebay.com/")
        x = 500
        while x < 4500:
            web.execute_script("window.scrollTo(0," + str(x) + ")")
            x += 100
            time.sleep(0.05)

        fill_in = web.find_element_by_xpath(
            "/html/body/header/table/tbody/tr/td[5]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
        fill_in.send_keys(self.search)
        button = web.find_element_by_id("gh-btn")
        button.click()
        
        #Search success audio
        self.searchSuccess()

        time.sleep(600)