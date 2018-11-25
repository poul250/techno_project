import random
from selenium import webdriver
from time import sleep

def random_sleep(offset=1.5, length=4):
    sleep(random.random() * length + offset)

def parse(browser, url):
    browser.get(url)
    name = browser.find_element_by_class_name('profile-public-name-edUBF')
    data = browser.find_elements_by_class_name('profile-public-summary-item-wFbyw')
    prod = browser.find_elements_by_class_name('styles-date-2vN1V')
    person_info = {
        'name': name.text,
        'data': list(map(lambda x: x.text, data)),
        'prod_data_active': list(map(lambda x: x.text, prod))
    }
    c = browser.find_element_by_partial_link_text('Завершённые')
    c.click()
    random_sleep()
    prod = browser.find_elements_by_class_name('styles-date-2vN1V')
    person_info['prod_data_finished'] = list(map(lambda x: x.text, prod))
    return person_info
