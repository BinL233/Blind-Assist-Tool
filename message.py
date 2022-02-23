from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gtts
from playsound import playsound
import os
import Record


class logIn:

    def __init__(self):
        pass

    def loginConfirmation(self):
        print("Do you wanna to log in to this site")
        loginConf = gtts.gTTS("Do you wanna to log in to this site")
        loginConf.save("Audio/loginConf.mp3")
        playsound("Audio/loginConf.mp3")
        os.remove("Audio/loginConf.mp3")

    def keyboardAudio(self, key):
        # Read the input of keybeard.
        pass


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
        print("please tell me what product you are looking for")
        print("You can speak after the beep")
        qSound = "please tell me what product you are looking for"
        qSound2 = "You can speak after the beep"
        self.prodSound(qSound)
        self.prodSound(qSound2)
        #search = input("What product do you want to see?")

        # Record
        self.search = Record.recordAudio()

        if self.search == '':
            self.error()

            return self.elementSearch()

        print("You are looking for " + self.search + ", right?")
        ann2 = gtts.gTTS("You are looking for " + self.search + ", right?")
        ann2.save("Audio/ann2.mp3")
        playsound("Audio/ann2.mp3")
        os.remove("Audio/ann2.mp3")

        for x in range(0, 999):

            print("Please say yes or no after the beep")
            ann3 = gtts.gTTS("Please say YES or NO after the beep")
            ann3.save("Audio/ann3.mp3")
            playsound("Audio/ann3.mp3")
            os.remove("Audio/ann3.mp3")

            ans = Record.recordAudio()

            if ans == 'yes':
                # Waiting audio
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
                ann4 = gtts.gTTS(
                    "Sorry, I did hear that. Could you repeat again?")
                ann4.save("Audio/ann4.mp3")
                playsound("Audio/ann4.mp3")
                os.remove("Audio/ann4.mp3")

    def searchSuccess(self):
        playsound("Audio/Success.mp3")
        search_success = gtts.gTTS(self.search + " search success!")
        search_success.save("Audio/search_success.mp3")
        playsound("Audio/search_success.mp3")
        os.remove("Audio/search_success.mp3")

    def amazon(self):
        self.elementSearch()

        web = webdriver.Chrome()
        web.get("https://www.amazon.com/")

        # If the user wants to login first
        log_in = web.find_element_by_id("nav-link-accountList")
        log_in.click()
        time.sleep(1)
        # the audio said "You are ready to log in, please click enter after you done
        # At time time we will have a feature that it says what the user input is

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

        # Search success audio
        self.searchSuccess()

        sort = web.find_element_by_id("a-autoid-0-announce")
        sort.click()
        time.sleep(1)
        customer_review = web.find_element_by_id("s-result-sort-select_3")
        customer_review.click()
        time.sleep(600)

        # add things to cart and checkout function
        go_to_cart = web.find_element_by_id("nav-cart-count-container")
        add_to_cart = web.find_element_by_id("add-to-cart-button")
        proceed_to_checkout = web.find_element_by_id(
            "proceed-to-checkout-action")
        place_your_order = web.find_elements_by_class_name(
            "a-button-text place-your-order-button")
        if  # the user wants to add to cart:
        add_to_cart.click()
        if  # the user wants to checkout:
        go_to_cart.click()
        time.sleep(0.5)
        proceed_to_checkout.click()
        time.sleep(0.5)
        place_your_order.click()

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

        # Search success audio
        self.searchSuccess()
        time.sleep(600)

    def target(self):

        self.elementSearch()

        web = webdriver.Chrome()
        web.get("https://www.target.com/")
        x = 500
        while x < 4500:
            web.execute_script("window.scrollTo(0," + str(x) + ")")
            x += 100
            time.sleep(0.05)

        fill_in = web.find_element_by_xpath(
            "/html/body/div[1]/div/div[3]/div[2]/nav/div/form/input")
        fill_in.send_keys(self.search)
        button = web.find_element_by_id("search")
        button.click()

        # Search success audio
        self.searchSuccess()

        time.sleep(600)
