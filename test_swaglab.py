import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_swaglab_login():
    #declare the browser to be used or driver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    try:
        #get the title and print it
        print(driver.title)
        assert "Swag Labs" in driver.title


        #ind the element for the username
        username_input= driver.find_element(By.ID, "user-name")
        username_input.clear()
        username_input.send_keys("standard_user")


        #also find the element of the password form
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("secret_sauce")


        #submit
        submit_button = driver.find_element(By.ID, "login-button")
        submit_button.click()

        # Wait a bit to let page load
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )

        #Assert that it successfully logged in with inventory in its url
        assert "inventory.html" in driver.current_url

    finally:
        driver.quit()
