def get_accounts_from_page(driver, url):
    driver.get(url)
    items = driver.find_elements_by_class_name('item-description-title-link')
    results = []
    links = []
    for item in items:
        links.append(item.get_attribute('href'))
    for item_url in links:
        driver.get(item_url)
        seller = driver.find_element_by_class_name('seller-info-name').find_element_by_tag_name('a').get_attribute('href')
        results.append(seller)
    return results

def search(driver, url, max_accounts = 0):
    '''
    url - ссылка на страничку авито, где есть товары и прокрутка страниц, чтобы можно было добавить
    "?p=<номер страницы> в конец url
    
    max_accounts - максимальное количество аккаунтов, которое вытаскивает функция search
    
    '''
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    from selenium import webdriver
    from random import randint

    url = url + r'?p={}'
    cur_account = 0
    accounts = set()
    links = []
    page = 1
    while True:
        if cur_account >= max_accounts:
            break
        if len(links) == 0:
            links = get_accounts_from_page(driver, url.format(page))
            page += 1
        account = links.pop()
        if not (account in accounts) and account.startswith('https://www.avito.ru/user/'):
            accounts.add(account)
            cur_account += 1
            yield account