from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait

driver_path = "chromedriver.exe"
chr_driver = webdriver.Chrome(driver_path)
chr_driver.get("https://www.google.com/search?q=111")
chr_driver.maximize_window()
chr_driver.implicitly_wait(5)
fill_list = chr_driver.find_element_by_class_name('h3.LC20lb MBeuO DKV0Md').click()