import time
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_petfriends(selenium):
    # open PetFriends start page
    selenium.get('https://petfriends.skillfactory.ru/')
    time.sleep(5)
    # click on the new user button
    btn_new_user = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()
    # click existing user button
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u'У меня уже есть аккаунт')
    btn_exist_acc.click()
    # add email
    field_email = selenium.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys('adadad@jjaag.com')
    # add password
    field_pass = selenium.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys('1234')
    # click submit button
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()
    time.sleep(5)
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # make the screenshot of browser window
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("Authentication error.")

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe tests\test_selenium_petfriends.py
