"""
Testenium Automation TestCase

1. www.trendyol.com sitesi açılır
2. Ana sayfanın açıldığı kontrol edilir
3. Arama kutucuğuna "şort" kelimesi girilir
4. Arama kutucuğundan "şort" kelimesi silinir
5. Arama kutucuğuna "gömlek" kelimesi girilir
6. Klavye üzerinden enter tuşuna bastırılır
7. Sonuca göre sergilenen ürünlerden rastgele bir ürün seçilir
8. Seçilen ürünün ürün bilgisi ve tutar bilgisi txt dosyasına yazdırılır
9. Seçilen ürün sepete eklenir
10. Ürün sayfasındaki fiyat ile sepette yer alan ürün fiyatının doğruluğu karşılaştırılır
11. Adet arttırılarak ürün adedinin 2 olduğu doğrulanır
12. Ürün sepetten silinerek sepetin boş olduğu kontrol edilir

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

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,15)

driver.get("https://www.trendyol.com/")
main_page_url = driver.current_url
action = ActionChains(driver)

class MainPage():
    def __init__(self,driver):
        self.driver = driver
        self.search_box =(By.CSS_SELECTOR, "[data-testid='suggestion']")
        self.login_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p")
        self.search_button = (By.CSS_SELECTOR,"[data-testid='search-icon']")
        self.pop_up = (By.ID,"Combined-Shape")
    def assert_the_web_page(self):
        assert "https://www.trendyol.com/" in main_page_url
    def pop_up_delete(self):
        self.driver.find_element(*self.pop_up).click()
    def write_text_in_search_box(self,text):
        self.driver.find_element(*self.search_box).send_keys(text)
    def clear_search_box(self):
        self.driver.find_element(*self.search_box).clear()
    def enter_text_in_search_box(self):
        enter = self.driver.find_element(*self.search_box)
        enter.send_keys(Keys.ENTER)


main_page = MainPage(driver)
main_page.assert_the_web_page()
main_page.pop_up_delete()
main_page.write_text_in_search_box("şort")
main_page.clear_search_box()
main_page.write_text_in_search_box("gömlek")
main_page.enter_text_in_search_box()
time.sleep(20)


