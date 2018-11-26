'''
import random
from datetime import datetime, date, time
from selenium import webdriver
from time import sleep

def random_sleep(offset=1, length=0):
    sleep(random.random() * length + offset)

def parse(browser, url):
    browser.get(url)
    name = browser.find_element_by_class_name('profile-public-name-edUBF')
    data = browser.find_elements_by_class_name('profile-public-summary-item-wFbyw')
    prod = browser.find_elements_by_class_name('styles-date-2vN1V')
    i = 0
    l = len(prod) - 1
    while(l != len(prod)):
        l = len(prod)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep()
        prod = browser.find_elements_by_class_name('styles-date-2vN1V')
        try:
            element = browser.find_element_by_class_name('styles-button-10MP4')
            element.click()
            l = l - 1
            random_sleep()
        except:
            pass
    person_info = {
        'name': name.text,
        'data': list(map(lambda x: x.text, data)),
        'prod_data_active': list(map(lambda x: x.text, prod))
    }
    c = browser.find_element_by_partial_link_text('Завершённые')
    c.click()
    random_sleep()
    prodold = browser.find_elements_by_class_name('styles-date-2vN1V')
    l = len(prodold) - 1
    while(l != len(prodold)):
        l = len(prodold)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep()
        prodold = browser.find_elements_by_class_name('styles-date-2vN1V')
        try:
            element = browser.find_element_by_class_name('styles-button-10MP4')
            element.click()
            l = l - 1
            random_sleep()
        except:
            pass
    person_info['prod_data_finished'] = list(map(lambda x: x.text, prodold))
    return person_info
'''
import random
from datetime import datetime, date, time
from selenium import webdriver
from time import sleep

def random_sleep(offset=1, length=0):
    sleep(random.random() * length + offset)

def parse(browser, url):
    browser.get(url)
    name = browser.find_element_by_class_name('profile-public-name-edUBF')
    data = browser.find_elements_by_class_name('profile-public-summary-item-wFbyw')
    prod = browser.find_elements_by_class_name('styles-date-2vN1V')
    cost = browser.find_elements_by_class_name('styles-price-1RC3V')
    i = 0
    l = len(prod) - 1
    while(l != len(prod)):
        l = len(prod)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep()
        prod = browser.find_elements_by_class_name('styles-date-2vN1V')
        cost = browser.find_elements_by_class_name('styles-price-1RC3V')
        try:
            element = browser.find_element_by_class_name('styles-button-10MP4')
            element.click()
            l = l - 1
            random_sleep()
        except:
            pass
    person_info = {
        'name': name.text,
        'data': list(map(lambda x: x.text, data)),
        'prod_data_active': list(map(lambda x: x.text, prod)),
        'prod_cost_active': list(map(lambda x: x.text, cost))
    }
    c = browser.find_element_by_partial_link_text('Завершённые')
    c.click()
    random_sleep()
    prodold = browser.find_elements_by_class_name('styles-date-2vN1V')
    costold = browser.find_elements_by_class_name('styles-price-1RC3V')
    l = len(prodold) - 1
    while(l != len(prodold)):
        l = len(prodold)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep()
        prodold = browser.find_elements_by_class_name('styles-date-2vN1V')
        costold = browser.find_elements_by_class_name('styles-price-1RC3V')
        try:
            element = browser.find_element_by_class_name('styles-button-10MP4')
            element.click()
            l = l - 1
            random_sleep()
        except:
            pass
    person_info['prod_data_finished'] = list(map(lambda x: x.text, prodold))
    person_info['prod_cost_finished'] = list(map(lambda x: x.text, costold))
    return person_info