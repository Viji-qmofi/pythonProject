import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui
import select
from webdrivermanager.chrome import





class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path='C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_artofliving(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Art of Living")
        self.driver.find_element_by_name("btnK").click()



    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()











