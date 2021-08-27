from time import sleep
import calendar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver')


#driver.get("https://meet.google.com/xtk-pnhw-cbg")

driver.get("https://www.google.com")

print(driver.title)
#print(calendar.day_name[date.today().weekday()])

search = driver.find_element_by_name("q")
search.send_keys("Gmail")
search.send_keys(Keys.RETURN)


sleep(6)

driver.close()
