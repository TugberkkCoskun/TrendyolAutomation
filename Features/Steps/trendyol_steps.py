from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import time
import random

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
        text = "gömlek"
        if result.text != text:
            raise AssertionError
    except NoSuchElementException:
        pass

@given('User shall go to the "https://www.trendyol.com/sr?q=g%C3%B6mlek&qt=g%C3%B6mlek&st=g%C3%B6mlek&os=1"')
def go_to_gömlek_result_page(context):
    context.driver = webdriver.Chrome()
    context.wait = WebDriverWait(context.driver, 15)
    context.driver.get("https://www.trendyol.com/sr?q=g%C3%B6mlek&qt=g%C3%B6mlek&st=g%C3%B6mlek&os=1")
    context.driver.maximize_window()
    context.wait.until(EC.presence_of_element_located((By.ID,"onetrust-accept-btn-handler"))).click()
    time.sleep(3)

@when('User shall randomly select one of the listed results')
def randomly_select(context):
    context.driver.execute_script("window.scrollBy(0, 100)")
    try:
        pop_up_element = context.driver.find_element(By.XPATH,"//div[@class='popup']")
        overlay_element = context.driver.find_element(By.XPATH,"//div[@class='overlay']")
        if pop_up_element.is_displayed() or overlay_element.is_displayed():
            action = ActionChains(context.driver)
            action.move_by_offset(100,100).perform()
            action.click().perform()
    except NoSuchElementException:
        pass
    gomleks = context.driver.find_elements(By.XPATH,"//div[@class='p-card-wrppr with-campaign-view']")
    random_gomlek= random.choice(gomleks)
    random_gomlek.click()
@then('User shall add randomly selected gömlek to the basket')
def add_to_basket(context):
    window= context.driver.current_window_handle
    new_window = context.driver.window_handles[-1]
    context.driver.switch_to.window(new_window)
    context.new_wind_url = context.driver.current_url
    context.price_at_item_page = context.wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='prc-dsc']")))
    context.price_at_item_list =[]
    context.price_at_item_list.append(context.price_at_item_page.text)
    basket_button = context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[component-id='1']")))
    basket_button.click()
@then('User shall verify that the price of the item in the basket is the same with the one on the gömlek page')
def verify_the_price(context):
    my_basket = context.driver.find_element(By.XPATH,"//div[@class='account-nav-item basket-preview']")
    action = ActionChains(context.driver)
    action.move_to_element(my_basket).perform()
    go_to_my_basket = context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.goBasket")))
    go_to_my_basket.click()
    price_at_my_basket = context.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='pb-basket-item-price']")))
    price_at_my_basket_list = []
    price_at_my_basket_list.append(price_at_my_basket.text)

    assert context.price_at_item_list == price_at_my_basket_list

@when('User increase the quantity')
def increase_quantity(context):
    increase_button = context.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ty-numeric-counter-button']")))
    increase_button.click()
    time.sleep(2)
@then('User shall verified that the quantity of the product is 2')
def assertion_quantity(context):
    quantity = context.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='counter-content']")))
    item_count = quantity.get_attribute("value")
    try:
        assert item_count == "2"

    except AssertionError:
        raise AssertionError
@when('User press the bin button')
def press_bin_button(context):
    bin_button = context.wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='i-trash']")))
    context.driver.execute_script("arguments[0].click()",bin_button)
    time.sleep(2)
@then('User shall verify that the basket is empty')
def assertion_of_basket_empty(context):
    bos_sepet = context.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='pb-header']")))
    assertion_of_basket = bos_sepet.text
    try:
        assert assertion_of_basket == "Sepetim (0 Ürün)"
    except AssertionError:
        raise AssertionError
























