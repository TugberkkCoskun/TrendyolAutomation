"""

Testenium Automation TestCase

1. www.trendyol.com sitesi açılır
2. Ana sayfanın açıldığı kontrol edilir
3. Arama kutucuğuna "şort" kelimesi girilir
4. Arama kutucuğundan "şort" kelimesi silinir
5. Arama kutucuğuna "gömlek" kelimesi girilir
6. Klavye üzerinden enter tuşuna bastırılır
7. Sonuca göre sergilenen ürünlerden rastgele bir ürün seçilir
8. Seçilen ürün sepete eklenir
9. Ürün sayfasındaki fiyat ile sepette yer alan ürün fiyatının doğruluğu karşılaştırılır
10. Adet arttırılarak ürün adedinin 2 olduğu doğrulanır
11. Ürün sepetten silinerek sepetin boş olduğu kontrol edilir

NOT: Proje Page Object Pattern kullanılarak yazılmalıdır.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import re

class MainPage():
    def __init__(self,driver):
        self.driver = driver
        self.search_box =(By.CSS_SELECTOR, "[data-testid='suggestion']")
        self.pop_up = (By.ID,"Combined-Shape")
    def assert_the_web_page(self):
        expected_url = "https://www.trendyol.com/"
        main_page_url = self.driver.current_url
        assert expected_url == main_page_url
    def pop_up_delete(self):
        self.driver.find_element(*self.pop_up).click()
    def write_text_in_search_box(self,text):
        self.driver.find_element(*self.search_box).send_keys(text)
    def clear_search_box(self):
        self.driver.find_element(*self.search_box).clear()
    def enter_text_in_search_box(self):
        enter = self.driver.find_element(*self.search_box)
        enter.send_keys(Keys.ENTER)
class SearchResultPage():
    def __init__(self,driver):
        self.driver = driver
        self.search_results = self.driver.find_elements(By.XPATH,"//div[@class='p-card-wrppr with-campaign-view']")
    def small_pop_up_deleter(self):
        driver.execute_script("window.scrollBy(0, 100)")
        try:
            overlay_element =self.driver.find_element(By.XPATH,"//div[@class='overlay']")
            popup_element = self.driver.find_element(By.XPATH,"//div[@class='popup']")
            if overlay_element.is_displayed() or popup_element.is_displayed():
                action = ActionChains(self.driver)
                action.move_by_offset(100,100).click().perform()
        except NoSuchElementException:
            pass
    def click_random_result(self):
        random_result = random.choice(self.search_results)
        random_result.click()

class ItemPage():
    def __init__(self, driver):
        self.driver = driver
        self.go_to_basket = (By.XPATH,"//div[@class='account-nav-item basket-preview']")
        self.price_at_item_page = []
        self.price_at_basket_page =[]

    def delete_item_pop_up(self):
        driver.execute_script("window.scrollBy(0, 100)")
        try:
            campain_pop_up = self.driver.find_element(By.XPATH, "//div[@class='campaign-button bold']")
            if campain_pop_up.is_displayed():
                action = ActionChains(self.driver)
                action.move_by_offset(100, 100).click().perform()
        except NoSuchElementException:
            pass
    def window_change(self):
            current_window = self.driver.current_window_handle
            new_window = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_window)
            new_window_url = self.driver.current_url
    def add_to_basket_button(self):
        price_item = self.driver.find_element(By.XPATH,"//span[@class='prc-dsc']")
        price2 = price_item.text
        self.price_at_item_page.append(price2)
        self.add_to_basket = self.driver.find_element(By.CSS_SELECTOR,"[component-id = '1'")
        self.add_to_basket.click()

    def check_item_added_to_basket(self):
        try:
            basket_item_count = self.driver.find_element(By.XPATH, "//div[@class='basket-item-count-container visible']")
            added_to_basket = self.driver.find_element(By.XPATH, "//div[@class='add-to-basket-button-text-success']")
            if basket_item_count.text == "1" and added_to_basket.text == "Sepete Eklendi":
                return True
        except NoSuchElementException:
            pass
        return False
    def move_mouse_to_basket_click(self):
        basket_preview = self.driver.find_element(*self.go_to_basket)
        action = ActionChains(self.driver)
        action.move_to_element(basket_preview).perform()
        go_to_basket_button = self.driver.find_element(By.CSS_SELECTOR,"a.goBasket")
        go_to_basket_button.click()
    def compare_prices(self):
        price_at_basket = self.driver.find_element(By.XPATH,"//div[@class='pb-basket-item-price']")
        price = price_at_basket.text
        self.price_at_basket_page.append(price)
        if self.price_at_item_page == self.price_at_basket_page:
            pass
    def press_plus_button(self):
        plus_button = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'ty-numeric-counter-button']")))
        driver.execute_script("arguments[0].click()",plus_button)
        value = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class = 'counter-content']")))
        item_count = value.get_attribute("value")
        if item_count == "2":
            pass
    def clear_basket(self):
        trash_button = wait.until(EC.presence_of_element_located((By.XPATH,"//i[@class='i-trash']")))
        driver.execute_script("arguments[0].click()",trash_button)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,"//i[@class = 'i-bagg']")))
        except NoSuchElementException:
            print("Kaldırıldı yazısı yok")


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,15)
driver.get("https://www.trendyol.com/")

main_page = MainPage(driver)
main_page.assert_the_web_page()
main_page.pop_up_delete()
main_page.write_text_in_search_box("şort")
time.sleep(2)
main_page.clear_search_box()
main_page.write_text_in_search_box("gömlek")
main_page.enter_text_in_search_box()
time.sleep(2)
search_result_page = SearchResultPage(driver)
search_result_page.small_pop_up_deleter()
search_result_page.click_random_result()
time.sleep(2)
item_page = ItemPage(driver)
item_page.window_change()
item_page.delete_item_pop_up()
time.sleep(2)
item_page.add_to_basket_button()
item_page.check_item_added_to_basket()
time.sleep(2)
item_page.move_mouse_to_basket_click()
item_page.window_change()
item_page.compare_prices()
driver.refresh()
item_page.press_plus_button()
item_page.clear_basket()
time.sleep(3)
driver.close()