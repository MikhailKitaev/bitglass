from datetime import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import links_header

driver = webdriver.Firefox()
driver.get("http://www.bitglass.com")
driver.find_element_by_xpath(links_header.free_trial).click()

