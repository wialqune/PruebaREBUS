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

class TestValidaciondebuscador():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validaciondebuscador(self):
    self.driver.get("https://www.mercadolibre.com.co/")
    self.driver.set_window_size(1936, 1066)
    element = self.driver.find_element(By.CSS_SELECTOR, ".andes-carousel-snapped__slide:nth-child(2) img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "cb1-edit").click()
    self.driver.find_element(By.ID, "cb1-edit").send_keys("aspiradora carro")
    element = self.driver.find_element(By.ID, "cb1-opt1-6")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".andes-carousel-snapped__slide--active img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.ID, "cb1-edit").click()
    self.driver.find_element(By.ID, "cb1-edit").send_keys("lavadora")
    self.driver.find_element(By.CSS_SELECTOR, ".nav-icon-search").click()
  
