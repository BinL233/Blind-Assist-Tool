from distutils.log import error
from numpy import record
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gtts
from playsound import playsound
import os
import Record
from pynput.keyboard import Key, Controller
import pyautogui
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import requests


class WebCrawler:

    def __init__(self):
        pass

    def productTitle(search):

        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://www.amazon.com/s?k=' + search
        resp = requests.get(url, headers=headers)
        resp.encoding
        return resp


class logIn:

    def __init__(self):
        pass

    def loginConfSound(self):
        print("\nDo you wanna to login?")
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
        print("\nDo you want to add it to cart?")
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
        print("\nAdd to cart successfully")
        atcS = gtts.gTTS("Add to cart successfully")
        atcS.save("Audio/atcS.mp3")
        playsound("Audio/atcS.mp3")
        os.remove("Audio/atcS.mp3")

    def checkOut(self):
        print("\nDo you want to check out?")
        checkOut = gtts.gTTS(
            "Do you want to check out?")
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
        print("\nCheck out successfully")
        checkOutScs = gtts.gTTS("Check out successfully")
        checkOutScs.save("Audio/checkOutScs.mp3")
        playsound("Audio/checkOutScs.mp3")
        os.remove("Audio/checkOutScs.mp3")

    def checkOutConfirm(self):
        print("\nAre you sure you want to check out?")
        checkOutConf = gtts.gTTS(
            "Are you sure you want to check out?")
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
        print("\nDo you want to go to your cart?")
        goToCart = gtts.gTTS(
            "Do you want to go to your cart?")
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
        print("\nGo to cart successfully")
        goToCartScs = gtts.gTTS("Go to cart successfully")
        goToCartScs.save("Audio/goToCartScs.mp3")
        playsound("Audio/goToCartScs.mp3")
        os.remove("Audio/goToCartScs.mp3")

    def cancelScs(self):
        print("\nCancel success")
        cancel = gtts.gTTS("Cancel success")
        cancel.save("Audio/Cancel.mp3")
        playsound("Audio/Cancel.mp3")
        os.remove("Audio/Cancel.mp3")

    def error(self):
        print("\nI'm not sure I understand. Please say that again.")
        error = gtts.gTTS("I'm not sure I understand. Please say that again.")
        error.save("Audio/error.mp3")
        playsound("Audio/error.mp3")
        os.remove("Audio/error.mp3")

    def addOrCheck(self):
        print("\nDo you want to add to your cart or check out directly")
        conf = gtts.gTTS(
            "Do you want to add to your cart or check out directly")
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
        print("\nTell me the product after the beep")
        qSound = "Tell me the product after the beep"
        self.prodSound(qSound)
        #search = input("What product do you want to see?")

        # Record
        self.search = Record.recordAudio()

        if self.search == '':
            self.error()

            return self.elementSearch()

        print("\nYou are looking for " + self.search + ", right?")
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
                print("\nOkay...Give me one second")
                ann = gtts.gTTS("Okay...Give me one second")
                ann.save("Audio/ann.mp3")
                playsound("Audio/ann.mp3")
                os.remove("Audio/ann.mp3")
                break

            elif ans == 'no':
                return self.elementSearch()

            else:
                print("\nSorry, I did hear that. Could you repeat again?")
                ann4 = gtts.gTTS(
                    "Sorry, I did hear that. Could you repeat again?")
                ann4.save("Audio/ann4.mp3")
                playsound("Audio/ann4.mp3")
                os.remove("Audio/ann4.mp3")

    def searchSuccess(self):
        output = "\n" + str(self.search) + " search success!"
        print(output)
        playsound("Audio/Success.mp3")
        search_success = gtts.gTTS(self.search + " search success!")
        search_success.save("Audio/search_success.mp3")
        playsound("Audio/search_success.mp3")
        os.remove("Audio/search_success.mp3")

    def recommand(self):
        print("\nDo you want some recommandations?")
        recommand = gtts.gTTS("Do you want some recommandations?")
        recommand.save("Audio/recommand.mp3")
        playsound("Audio/recommand.mp3")
        os.remove("Audio/recommand.mp3")

        ans = Record.recordAudio()

        if ans == 'yes':
            driver_path = "chromedriver.exe"
            chr_options = Options()
            chr_options.add_experimental_option("detach", True)
            chr_driver = webdriver.Chrome(driver_path, options=chr_options)
            chr_driver.get("https://www.google.com/")
            fill_in = chr_driver.find_element_by_xpath(
                "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
            fill_in.send_keys(self.search)
            self.autoType(Key.enter)
            Reconnmad_list = chr_driver.find_elements_by_class_name("EyxGV")
            Reconnmad_list.click()

        elif ans == 'no':
            print("\nOkay")
            okay = gtts.gTTS("Okay")
            okay.save("Audio/Okay.mp3")
            playsound("Audio/Okay.mp3")
            os.remove("Audio/Okay.mp3")

        else:
            self.error()
            return self.recommand()

    def productChoose(self):
        print("\nWhich product you wanna see details?")
        chooseD = gtts.gTTS("Which product you wanna see details?")
        chooseD.save("Audio/chooseD.mp3")
        playsound("Audio/chooseD.mp3")
        os.remove("Audio/chooseD.mp3")

        ans = Record.recordAudio()
        ans = ans.rstrip()

        if ans.isdigit() == True:
            ans = int(ans)

            if ans >= 1 and ans <= 10:
                pass

            elif ans > 10 or ans < 1:
                print("\nMake sure the number between one to ten")
                error2 = gtts.gTTS("Make sure the number between one to ten")
                error2.save("Audio/error2.mp3")
                playsound("Audio/error2.mp3")
                os.remove("Audio/error2.mp3")
                return self.productChoose()

            else:
                self.error()
                return self.productChoose()

        else:
            self.error()
            return self.productChoose()

        return ans

    '''
    def productTitle(self):
        fill_list = chr_driver.find_element_by_class_name("a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

        print(fill_list)
        
        return fill_list
    '''

    def amazon(self):
        self.elementSearch()
        login = logIn()
        driver_path = "chromedriver.exe"
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        chr_driver = webdriver.Chrome(driver_path, options=chr_options)
        chr_driver.get("https://www.amazon.com/")
        chr_driver.maximize_window()

        # If the user wants to login first
        if login.loginConf == True:
            log_in = chr_driver.find_element_by_id("nav-link-accountList")
            log_in.click()
        # the audio said "You are ready to log in, please click enter after you done
        # At time time we will have a feature that it says what the user input is

        fill_in = chr_driver.find_element_by_xpath(
            "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        fill_in.send_keys(self.search)
        time.sleep(1)
        button = chr_driver.find_element_by_id("nav-search-submit-button")
        button.click()

        # Search success audio
        self.searchSuccess()

        chr_driver.implicitly_wait(5)

        ans = self.productChoose()

        button1 = chr_driver.find_element_by_xpath(
            '(//*[@class="a-link-normal"])[' + str(ans) + ']')
        button1.click()

        self.recommand()

        sort = chr_driver.find_element_by_id("a-autoid-0-announce")
        sort.click()
        time.sleep(1)
        customer_review = chr_driver.find_element_by_id(
            "s-result-sort-select_3")
        customer_review.click()

        # add things to cart and checkout function
        self.go_to_cart = chr_driver.find_element_by_id(
            "nav-cart-count-container")
        self.add_to_cart = chr_driver.find_element_by_id("add-to-cart-button")
        self.proceed_to_checkout = chr_driver.find_element_by_id(
            "proceed-to-checkout-action")
        self.place_your_order = chr_driver.find_elements_by_class_name(
            "a-button-text place-your-order-button")

        self.addOrCheck()

    def ebay(self):

        self.elementSearch()

        driver_path = "chromedriver.exe"
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        chr_driver = webdriver.Chrome(driver_path, options=chr_options)
        chr_driver.get("https://www.ebay.com/")
        chr_driver.maximize_window()
        fill_in = chr_driver.find_element_by_xpath(
            "/html/body/header/table/tbody/tr/td[5]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
        fill_in.send_keys(self.search)
        button = chr_driver.find_element_by_id("gh-btn")
        button.click()

        # add it to cart function
        is_cart = chr_driver.find_element_by_id("isCartBtn_btn")
        is_cart.click()
        # above is to ask the user if they want to add to cart

        # under is to ask the user if they want to checkout
        go_to_cart = chr_driver.find_element_by_id("gh-cart-n")
        go_to_cart.click()
        go_to_checkout = chr_driver.find_elements_by_class_name(
            "cartsummary-cta")

        # Search success audio
        self.searchSuccess()

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
