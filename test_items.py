import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items_link(browser):
    browser.get(link)
    time.sleep(10)
