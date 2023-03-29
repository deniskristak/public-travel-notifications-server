from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.chrome.options import Options

from data.trainlines_names import tranline_names


class WebDriver:
    def __init__(self):
        path_to_chrome_driver = os.path.dirname(__file__) + '/utils/chromedriver'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=path_to_chrome_driver, options=chrome_options)


def get_driver(self):
    return self.driver


def quit(self):
    self.driver.quit()


class CPScraper:

    def __init__(self):
        self.driver_obj = WebDriver()
        self.driver = self.driver_obj.get_driver()
        # navigate to the website
        self.driver.get("https://cp.hnonline.sk/vlak/spojenie/")

    def _place_exists(self, place) -> bool:
        # locate the "From" input field by its id
        from_input = self.driver.find_element(By.ID, "From")

        # enter the desired input value
        from_input.send_keys(place)
        sleep(3)

        # locate the "From" label, try to look for a message "We don't know this place"
        unknown_place_element = "//label[@for='From']/span[@class='label-error' and text()='Také miesto nepoznáme.']"
        # if that error message is found, we know the place doesn't exist
        try:
            self.driver.find_element(By.XPATH, unknown_place_element)
            place_exists = False
        except NoSuchElementException:
            place_exists = True
        self.driver.quit()
        return place_exists


for name in tranline_names:
    cp_s = CPScraper()
    if not cp_s._place_exists(name):
        print(f"{name}")
