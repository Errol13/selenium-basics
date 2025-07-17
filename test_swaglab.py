import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#helpfer function for repeatable login steps
def perform_login(driver, username, password):
    #visit the site
    driver.get("https://www.saucedemo.com/")
    print("Performing login...")

    #find the element for the username
    username_input= driver.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys(username)


    #also find the element of the password form
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)


    #submit
    submit_button = driver.find_element(By.ID, "login-button")
    submit_button.click()


#create parameters for different valid credentials 
@pytest.mark.parametrize("username",[
    ("standard_user"),
    ("visual_user"),
    ("performance_glitch_user")
])
def test_swaglab_valid_credentials(username):
    driver = webdriver.Chrome()
    
    try:
        # call the perform login
        perform_login(driver, username, "secret_sauce")
        
        #wait until it is successfully logged in
        WebDriverWait(driver,10).until(
            EC.url_contains("inventory")
        )

        #assert if it contains inventory
        assert "inventory" in driver.current_url
    
    finally:
        try:
            driver.quit()
        except:
            print("Browser already closed!, skipping quit")


#create parameters for different invalid credentials 
@pytest.mark.parametrize("username, password",[
    ("standard_user", "wrong_pass"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "grr-angrr")
])
def test_swaglab_invalid_credentials(username, password):
    driver = webdriver.Chrome()
    
    try:
        # call the perform login
        perform_login(driver, username, password)
        
        #wait until it is successfully logged in
        error = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        #assert if it contains error message 
        assert error.is_displayed()
    
    finally:
        try:
            driver.quit()
        except:
            print("Browser was already closed! skipping quit")