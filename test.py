import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://129.204.62.26/fsmarket/user.php?act=register")
time.sleep(3)
driver.find_element_by_css_selector("[name='extend_field5']").send_keys("abc")
