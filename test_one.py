import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.tinkoff.ru")


#поиск элемента
#elem = driver.find_element_by_xpath(‘//span[@class='SecondMenu__tabsItem_VWx1A'][contains(text(),'Платежи')]’)
driver.find_element_by_xpath("//span[@class='SecondMenu__tabsItem_VWx1A'][contains(text(),'Платежи')]").click()
time.sleep(5)
driver.find_element_by_partial_link_text("ЖКХ").click()
time.sleep(5)
driver.find_element_by_partial_link_text("ЖКУ-Москва").click()


#ввод в инпут
#elem.send_keys("Hello WebDriver!")

#нажатие Enter
#elem.submit()

#print(driver.title)





#driver.find_element_by_id("submit_btn").click() # Клик по кнопке
#driver.find_element_by_id("cancel_link").click() # Клик по ссылке
#driver.find_element_by_id("username").send_keys("agileway") # Ввод символов
#driver.find_element_by_id("alert_div").text # Получаем текст