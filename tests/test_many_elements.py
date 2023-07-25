import pytest
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    # go to navigation page
    pytest.driver.get("http://petfriends.skillfactory.ru/login")
    yield
    pytest.driver.quit()


def test_show_my_pets():
    # email
    pytest.driver.find_element(By.ID, "email").send_keys("adadad@jjaag.com")
    # password
    pytest.driver.find_element(By.ID, "pass").send_keys("1234")
    # click login button
    pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # check main page of user
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"
