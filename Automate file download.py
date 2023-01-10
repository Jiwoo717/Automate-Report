from selenium import webdriver
from urllib3 import request
import datetime

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
#url launch
driver.get("https://rivian.sharepoint.com/sites/EngineeringPLM/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FEngineeringPLM%2FShared%20Documents%2FEngineering%20Processes%20%26%20Tools%2FTools%2FE%2EBoM%20Metric%2FDaily%20BoMs%2FDaily%20CA%20Report&viewid=dff43317%2D8837%2D48ce%2Db7bc%2D534aaa89c1ea")
#identify link with partial link text
l = driver.find_elements_by_partial_link_text('CASummaryReport'+ datetime.date.today().strftime('%Y%m_%d') + '_1101.xlsx')

#perform click
l.click()
print('Page navigated after click: ' + driver.title)
#driver quit
driver.quit()

URL = "https://rivian.sharepoint.com/sites/EngineeringPLM/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FEngineeringPLM%2FShared%20Documents%2FEngineering%20Processes%20%26%20Tools%2FTools%2FE%2EBoM%20Metric%2FDaily%20BoMs%2FDaily%20CA%20Report&viewid=dff43317%2D8837%2D48ce%2Db7bc%2D534aaa89c1ea"
response = request.()