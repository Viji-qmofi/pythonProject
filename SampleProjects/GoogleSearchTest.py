from selenium import webdriver
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()


    def test_search_artofliving(self):
        self.driver.get("https://mavinacademy.com/")
        #self.driver.find_element_by_name("q").send_keys("Art of Living")
        #self.driver.find_element_by_name("btnK").click()
        # get element
        element=self.driver.find_element_by_xpath(
            //button[@aria-label='open drawer']//span[@class='MuiIconButton-label']//*[local-name()='svg']")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




