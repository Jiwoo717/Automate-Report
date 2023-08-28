from selenium import webdriver
from urllib3 import request
import datetime

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
#url launch
driver.get("downloadlink_URL")
#identify link with partial link text
l = driver.find_elements_by_partial_link_text('CASummaryReport'+ datetime.date.today().strftime('%Y%m_%d') + '_1101.xlsx')

#perform click
l.click()
print('Page navigated after click: ' + driver.title)
#driver quit
driver.quit()

URL = "URL_of_choice(hidden_for_privacy)"
response = request.()
