import pandas as pd
from search import search
from parse import parse
from selenium import webdriver
from functools import partial

if __name__ == '__main__':
    max_accounts = 10
    data = {}

    with webdriver.Chrome() as browser:
        parser = partial(parse, browser=browser)
        searcher = search(driver=browser, url=r'https://www.avito.ru/rossiya/lichnye_veschi', max_accounts=max_accounts)
        
        for key, item in parser(next(searcher)).items():
            data[key] = [item]

        for acc_data in map(parser, searcher):
            for key, item in acc_data.items():
                data[key].append(item)
#     df = pd.DataFrame(data)
#     df.to_csv('avito_data.csv')
    print(data)