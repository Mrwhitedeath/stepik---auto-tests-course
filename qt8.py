import os
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(2)
browser.get(link)



price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

button = browser.find_element_by_css_selector("button.btn").click()
num = browser.find_element_by_id('input_value').text
input = browser.find_element_by_id('answer').send_keys(calc(int(num)))
button = browser.find_element_by_id("solve").click()



# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()