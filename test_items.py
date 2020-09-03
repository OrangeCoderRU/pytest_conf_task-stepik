import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def element_is_exist(browser, selector):
    try:
        browser.find_element(By.CSS_SELECTOR, selector)
        return True
    except:
        return False

def test_items_link(browser):
    browser.get(link)
    assert element_is_exist(browser, "#add_to_basket_form"),  "Кнопки добавления в корзину нет"
