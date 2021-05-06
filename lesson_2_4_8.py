# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
#     - Открыть страницу http://suninjuly.github.io/explicit_wait2.html/explicit_wait2.html
#     - Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#     - Нажать на кнопку "Book"
#     - Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_id("book")
    button1.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
