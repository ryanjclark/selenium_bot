# Travels to homepage, submits the alert form, and asserts the banner flashes successfully
# Run a manual test at eateryexchange.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait


fake_email = "example@email.com"

print("Running alert form test with Windows XP, Chrome version 67")
with webdriver.Chrome('opt/WebDriver/bin/chromedriver') as driver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserVersion", "67")
    chrome_options.set_capability("platformName", "Windows XP")
    driver.get("https://eateryexchange.com/")
    driver.find_element(By.ID, "email_alert").send_keys(fake_email)
    select = Select(driver.find_element_by_id('area'))
    select.select_by_value('MN')
    button = driver.find_element(By.ID, "get_alerts")
    assert button.text == "Get Alerts"
    button.click()
    flash = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("alert_flash"))
    print("The green flash at the top of the screen was detected")

print("Running alert form test with Windows XP, Chrome version 81")
with webdriver.Chrome('opt/WebDriver/bin/chromedriver') as driver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserVersion", "81")
    chrome_options.set_capability("platformName", "Windows XP")
    driver.get("https://eateryexchange.com/")
    driver.find_element(By.ID, "email_alert").send_keys(fake_email)
    select = Select(driver.find_element_by_id('area'))
    select.select_by_value('MN')
    button = driver.find_element(By.ID, "get_alerts")
    assert button.text == "Get Alerts"
    button.click()
    flash = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("alert_flash"))
    print("The green flash at the top of the screen was detected")




# TODO: Include tear-down
# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
# def tearDown(self):
#     self.driver.quit()
