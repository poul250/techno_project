import pandas as pd
from search import search
from parse import parse
from normalize import normalize
from selenium import webdriver
from functools import partial

if __name__ == '__main__':
    max_accounts = 2
    url = r'https://www.avito.ru/rossiya/lichnye_veschi'
    data = {}

    with webdriver.Chrome() as browser:
        parser = partial(parse, browser)
        searcher = search(driver=browser, url=url, max_accounts=max_accounts)

        for key, item in normalize(parser(next(searcher))).items():
            data[key] = [item]

        for acc_data in map(parser, searcher):
            for key, item in normalize(acc_data).items():
                data[key].append(item)
#     df = pd.DataFrame(data)
#     df.to_csv('avito_data.csv')
    print(data)
