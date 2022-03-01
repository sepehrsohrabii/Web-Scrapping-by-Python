from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

email = input("Please Enter your Email:")


def check(email):
    if (re.search(regex, email)):
        #print('ok')
        return
    else:
        print('Invalid Email')
        email = input("Please Enter your Email:")
        check(email)
        return


check(email)
driver = webdriver.Chrome()

url1 = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

driver.get(url1)

email_field = driver.find_element_by_id('user-message')
email_field.clear()
email_field.send_keys(email)

email_button = driver.find_elements_by_xpath("//*[contains(text(), 'Show Message')]")
for btn in email_button:
    btn.click()


a_field = driver.find_element_by_id('sum1')
a_field.clear()
a_field.send_keys('10')
b_field = driver.find_element_by_id('sum2')
b_field.clear()
b_field.send_keys('5')

total_button = driver.find_elements_by_xpath("//*[contains(text(), 'Get Total')]")
for btn in total_button:
    btn.click()

## url2 ##
driver = webdriver.Chrome()

url2 = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
driver.get(url2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = datetime.today().weekday()
today = weekdays[day]
#print(today)

day_input = Select(driver.find_element_by_id('select-demo'))
day_input.select_by_visible_text(today)
