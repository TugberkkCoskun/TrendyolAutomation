from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import time

@given('User shall go to the www.trendyol.com and saw the main page is opened')
def go_to_main_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.trendyol.com/")
@then('User shall verify that the opened page is trendyols main page')
def verify_the_main_page(context):
    time.sleep(2)
    assert "https://www.trendyol.com" in context.driver.current_url

@when('User shall close the pop-up and enters "şort" in the text box')
def text_box_value_sort(context):
    pop_up = context.driver.find_element(By.ID,"Combined-Shape")
    pop_up.click()
    text_box = context.driver.find_element(By.CSS_SELECTOR,"[data-testid ='suggestion']")
    text_box.send_keys('şort')
    action = ActionChains(context.driver)
    context.text_box = text_box
@when('User shall clears the text box')
def clear_text_box(context):
    context.text_box.clear()
@when('User enters "gömlek" in the text box')
def text_box_value_gomlek(context):
    context.text_box.send_keys('gömlek')
@when('User shall presses the enter key on the keyboard')
def press_enter_button(context):
    context.text_box.send_keys(Keys.ENTER)
@then('User shall see the gömlek results are displayed')
def gomlek_results(context):
    try:
        result = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/h1")
        text = "gomlek"
        if result.text != text:
            raise
















