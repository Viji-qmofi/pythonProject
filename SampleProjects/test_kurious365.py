from selenium import webdriver
from selenium.webdriver.chrome.service import service
import unittest
import allure
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui
import select
from webdrivermanager.chrome import


class Testkurious365(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_MavinAcademy(self):
        self.driver.get("https://MavinAcademy.com/")
        self.driver
        elem = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/nav/div[5]/div/span')
        actions.click(elem).perform()




  Scenario: Display the Home Page of Mavin Academy  # features/MavinAcademy.feature:2
    Given launch Chrome browser                     # None
    When open Mavin Web site                        # None
    Then verify that the home page displayed        # None
    And close browser                               # None


Failing scenarios:
  features/MavinAcademy.feature:2  Display the Home Page of Mavin Academy

0 features passed, 1 failed, 0 skipped
0 scenarios passed, 1 failed, 0 skipped
0 steps passed, 0 failed, 0 skipped, 4 undefined
Took 0m0.000s

You can implement step definitions for undefined steps with these snippets:

@given(u'launch Chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given launch Chrome browser')


@when(u'open Mavin Web site')
def step_impl(context):
    raise NotImplementedError(u'STEP: When open Mavin Web site')


@then(u'verify that the home page displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the home page displayed')


@then(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')
