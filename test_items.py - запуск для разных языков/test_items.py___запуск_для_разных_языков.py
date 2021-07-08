import pytest 
from selenium import webdriver 
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link_product = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def browser(): 
    print("\nstart browser for test..") 
    browser = webdriver.Chrome() 
    yield browser 
    print("\nquit browser..") 
    browser.quit() 


   
class TestMainPage1(): 
   
    def test_language(self, browser, lin_k): 
        browser.get(lin_k)
        browser.implicitly_wait(10)
                 
        yes_submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@value="Добавить в корзину"]')))
        assert yes_submit == True, "Кнопка недоступна"  

        
                 

if __name__ == "__main__":
    test_language()  
