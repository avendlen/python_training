# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://prod.askona.ru/")
    self.driver.set_window_size(1283, 680)
    self.driver.find_element(By.LINK_TEXT, "Войти").click()
    self.driver.find_element(By.NAME, "USER_PASSWORD").send_keys("u0418u041c")
    self.driver.find_element(By.CSS_SELECTOR, ".popup__inner").click()
    self.driver.find_element(By.NAME, "USER_LOGIN").send_keys("autotest@askona.ru")
    self.driver.find_element(By.NAME, "USER_PASSWORD").send_keys("367641")
    self.driver.find_element(By.NAME, "Login").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#slick-slide20 .main-slider__item-img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Личный кабинет").click()
    self.driver.find_element(By.LINK_TEXT, "Персональные данные").click()
    self.driver.find_element(By.LINK_TEXT, "Личный кабинет").click()
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()
  
