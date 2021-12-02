from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Firefox()
driver.get("http://www.google.com");

search = driver.find_element_by_name('q');
search.clear();
search.send_keys("comcast");
search.send_keys(Keys.RETURN);
time.sleep(10)

driver.close();
