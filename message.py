from distutils.log import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gtts
from playsound import playsound
import os
import Record
from pynput.keyboard import Key, Controller
import pyautogui


class WebCrawler:

    def __init__(self):
        pass

    def productTitle():
        pass


class logIn:

    def __init__(self):
        pass

    def loginConfSound(self):
        print("Do you wanna to login?")
        loginConf = gtts.gTTS("Do you wanna to login?")
        loginConf.save("Audio/loginConf.mp3")
        playsound("Audio/loginConf.mp3")
        os.remove("Audio/loginConf.mp3")

    def loginConf(self):
        self.loginConfSound()
        ans = Record.recordAudio()
        if ans == "Yes":
            return True

        elif ans == "No":
            return False

        else:
            i = AutoSearch()
            i.error()
            return self.loginConf()

    def keyboardAudio(self, key):
        # Read the input of keybeard.
        pass


class AutoSearch:

    def __init__(self):
        self.search = None

    def autoType(self, input):
        keyboard = Controller()
        keyboard.press(input)

    def autoMouse(self, x, y):
        pyautogui.move(x, y)
        pyautogui.click()

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

    def addToCart(self):
        atc = gtts.gTTS(
            "Do you want to add it to cart?")
        atc.save("Audio/atc.mp3")
        playsound("Audio/atc.mp3")
        os.remove("Audio/atc.mp3")

        ans = Record.recordAudio()
        if ans == "Yes":  # the user wants to add to cart:
            self.add_to_cart.click()

        elif ans == "No":
            self.cancelScs()

        else:
            self.error()
            return self.addToCart()

    def addToCartScs(self):
        self.searchSuccess()
        atcS = gtts.gTTS("Add to cart successfully")
        atcS.save("Audio/atcS.mp3")
        playsound("Audio/atcS.mp3")
        os.remove("Audio/atcS.mp3")

    def checkOut(self):
        checkOut = gtts.gTTS(
            "Do you want to check out? Please say yes or no after the beep")
        checkOut.save("Audio/checkOut.mp3")
        playsound("Audio/checkOut.mp3")
        os.remove("Audio/checkOut.mp3")

        ans = Record.recordAudio()
        if ans == "Yes":
            if self.checkOutConfirm() == True:
                self.go_to_cart.click()
                time.sleep(0.5)
                self.proceed_to_checkout.click()
                time.sleep(0.5)
                self.place_your_order.click()

            else:
                self.cancelScs()

        elif ans == "No":
            self.cancelScs()

        else:
            self.error()
            return self.checkOut()

    def checkOutScs(self):
        self.searchSuccess()
        checkOutScs = gtts.gTTS("Check out successfully")
        checkOutScs.save("Audio/checkOutScs.mp3")
        playsound("Audio/checkOutScs.mp3")
        os.remove("Audio/checkOutScs.mp3")

    def checkOutConfirm(self):
        checkOutConf = gtts.gTTS(
            "Are you sure you want to check out? Please say yes or no after the beep")
        checkOutConf.save("Audio/checkOutConf.mp3")
        playsound("Audio/checkOutConf.mp3")
        os.remove("Audio/checkOutConf.mp3")

        ans = Record.recordAudio()

        if ans == "Yes":
            return True

        elif ans == "No":
            return False

        else:
            self.error()
            return self.checkOutConfirm()

    def goToCart(self):
        goToCart = gtts.gTTS(
            "Do you want to go to your cart? Please say yes or no after the beep")
        goToCart.save("Audio/goToCart.mp3")
        playsound("Audio/goToCart.mp3")
        os.remove("Audio/goToCart.mp3")

        ans = Record.recordAudio()
        if ans == "Yes":
            self.go_to_cart.click()

        elif ans == "No":
            self.cancelScs()

        else:
            self.error()
            return self.goToCart()

    def goToCartScs(self):
        goToCartScs = gtts.gTTS("Go to cart successfully")
        goToCartScs.save("Audio/goToCartScs.mp3")
        playsound("Audio/goToCartScs.mp3")
        os.remove("Audio/goToCartScs.mp3")

    def cancelScs(self):
        cancel = gtts.gTTS("Cancel success")
        cancel.save("Audio/Cancel.mp3")
        playsound("Audio/Cancel.mp3")
        os.remove("Audio/Cancel.mp3")

    def error(self):
        error = gtts.gTTS("I'm not sure I understand. Please say that again.")
        error.save("Audio/error.mp3")
        playsound("Audio/error.mp3")
        os.remove("Audio/error.mp3")

    def addOrCheck(self):
        conf = gtts.gTTS("You want to add to your cart or check out directly")
        conf = gtts.gTTS("Please say add to cart or check out after the beep")
        conf.save("Audio/conf.mp3")
        playsound("Audio/conf.mp3")
        os.remove("Audio/conf.mp3")

        ans = Record.recordAudio()

        if ans == "Add to cart":
            self.addToCart()
            self.addToCartScs()

        elif ans == "Check out":
            self.checkOut()
            self.checkOutScs()

        else:
            self.error()
            return self.addOrCheck()

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

    def recommand(self):
        recommand = gtts.gTTS("Do you want some recommandations?")
        recommand.save("Audio/recommand.mp3")
        playsound("Audio/recommand.mp3")
        os.remove("Audio/recommand.mp3")

        ans = Record.recordAudio()

        if ans == 'yes':
            web = webdriver.Chrome()
            web.get("https://www.google.com/")
            fill_in = web.find_element_by_xpath(
                "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
            fill_in.send_keys('ps5')  # self.search)
            self.autoType(Key.enter)

        elif ans == 'no':
            pass

        else:
            self.error()
            return recommand()

    def amazon(self):
        self.elementSearch()
        login = logIn()
        web = webdriver.Chrome()
        web.get("https://www.amazon.com/")

        # If the user wants to login first
        if login.loginConf == True:
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

        self.recommand()

        sort = web.find_element_by_id("a-autoid-0-announce")
        sort.click()
        time.sleep(1)
        customer_review = web.find_element_by_id("s-result-sort-select_3")
        customer_review.click()

        # add things to cart and checkout function
        self.go_to_cart = web.find_element_by_id("nav-cart-count-container")
        self.add_to_cart = web.find_element_by_id("add-to-cart-button")
        self.proceed_to_checkout = web.find_element_by_id(
            "proceed-to-checkout-action")
        self.place_your_order = web.find_elements_by_class_name(
            "a-button-text place-your-order-button")

        self.addOrCheck()

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
