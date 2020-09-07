from selenium import webdriver
from time import sleep
import datetime

def login(driver):
    driver.find_element_by_xpath("//*[@id=\"login_field\"]").send_keys("Username")
    driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("Password")
    driver.find_element_by_xpath("//*[@id=\"login\"]/form/div[4]/input[9]").click()

driver = webdriver.Chrome()
driver.get("https://github.com/Account-Name/Repository-Name/edit/master/README.md")
login(driver)
while True:
    try:
        now = datetime.datetime.now()
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"new_blob\"]/div[5]/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre/span").send_keys("\n Automated Contibution at " + str(now) + "<br>")
        driver.find_element_by_xpath("//*[@id=\"submit-file\"]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div[3]/div[1]/div[2]/div[2]/form[1]/button").click()
    except:
        print("Error, please comment out try/except to debug.")
        sleep(10)
