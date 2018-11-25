import pandas as pd
from search import search
from parse import parse

if __name__ == '__main__':
    max_accounts = 100000
    searcher = search(max_accounts=max_accounts)
    data = {}

    for key, item in parse(next(searcher)).items():
        data[key] = [item]

    for acc_data in map(parse, searcher):
        for key, item in acc_data.items():
            data[key].append(item)
    df = pd.DataFrame(data)
    df.to_csv('avito_data.csv')
