import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_browser():
    # Setup Chrome options
    options = Options()
    options.headless = False  # Set to True if you don't want the browser window to open
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver  # This allows the test to run and interact with the driver
    driver.quit()  # Quit the driver after the test is done


def test_login_valid_user(setup_browser):
    driver = setup_browser
    # Navigate to the demo website
    driver.get("https://www.saucedemo.com/")

    # Find the username, password fields and login button by their name/ID attributes
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Perform login with valid credentials
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    wait = WebDriverWait(driver, 10)  # Timeout after 10 seconds

    # Check if the login was successful (by checking the URL or a visible element)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert "Products" in driver.page_source  # This verifies that the "Products" text is present on the page


def test_login_invalid_user(setup_browser):
    driver = setup_browser
    driver.get("https://www.saucedemo.com/")

    # Find the username, password fields and login button
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Perform login with invalid credentials
    username.send_keys("invalid_user")
    password.send_keys("invalid_password")
    login_button.click()

    # Check if the error message is displayed
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    assert "Epic sadface" in error_message.text  # Check for the presence of the error message text


def test_add_to_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.saucedemo.com/")

    # Find the username, password fields and login button
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Perform login with invalid credentials
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # Check if the login was successful (by checking the URL or a visible element)
    print(driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert "Products" in driver.page_source  # This verifies that the "Products" text is present on the page

    #Check first item name is Sauce Labs Backpack
    firstitem = driver.find_element(By.XPATH,"//div[@class='inventory_item_name '][text()='Sauce Labs Backpack']")
    print(firstitem.text)  #print on Console
    assert firstitem.text== "Sauce Labs Backpack"

    # Click on add to cart button
    addtocart=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
    addtocart.click()

    # Use WebDriverWait to wait for the "Remove" button to be visible after clicking the add to cart button
    removebutton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack"))
    )

    # Now verify if the "Remove" button is visible
    assert removebutton.is_displayed(), "Remove button is not visible!"

    # Print confirmation to the console
    print("Remove button is visible on the screen after adding to cart.")

    # Click on cart icon and verify number of item added
    cartIcon=driver.find_element(By.XPATH,"//a/child::span")
    cartIcon.click()
    print("Icon clicked")



    #All Items List

    # allitems=driver.find_elements(By.XPATH,"//div[@class='cart_item']")
    # print("Item list length-->", len(allitems))
    # for item in allitems:
    #     print(item.text)

    # Click checkout
    driver.find_element(By.ID,"checkout").click()

     #PUT Checkout Information
    firstname=driver.find_element(By.ID,"first-name")
    lastname=driver.find_element(By.ID,"last-name")
    postalcode=driver.find_element(By.ID,"postal-code")

    firstname.send_keys("Ayush")
    lastname.send_keys("Singh")
    postalcode.send_keys("482001")

    # Click on continue button
    driver.find_element(By.XPATH,"//input[@type='submit']").click()

    # Check if the login was successful (by checking the URL or a visible element)
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    assert "Checkout: Overview" in driver.page_source  # This verifies that the "Products" text is present on the page

    # Checkout and Finish Order placement
    finish=driver.find_element(By.ID,"finish")
    finish.click()

    expected_text=driver.find_element(By.XPATH,"//h2[contains(text(),'Thank you for your order!')]").text
    assert expected_text in driver.page_source, f"Text '{expected_text}' not found in the page source"
    print(expected_text)





