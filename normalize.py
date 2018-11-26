def strtodays(s):
    import re
    from datetime import date, timedelta
    
    
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'] 
    
    if s.lower().find('сегодня') >= 0:
        t = date.today()
        return date(t.year, t.month, t.day).toordinal()
    elif s.lower().find('вчера') >= 0:
        t = date.today() - timedelta(days=1)
        return date(t.year, t.month, t.day).toordinal()
    
    m = re.match('.*(\d\d\d\d).*', s)
    year = date.today().year if m is None else int(m.group(1))
    month = 0
    for i in range(12):
        if s.find(months[i]) >= 0:
            month = i + 1
            break
    day = int(re.match('(\d*) .*', s).groups(1)[0])

    return date(year, month, day).toordinal()

def normalize(account):
    import re
    from datetime import date, timedelta
    
    result = dict()
    result['name'] = account['name'].lower()
    result['person_status'] = account['data'][0].lower()
    
    start_date = account['data'][1]
    if start_date.startswith('На Авито с '):
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'] 
        month = 0
        for i in range(12):
            if start_date.find(months[i]) >= 0:
                month = i + 1
                break
        result['start_date'] = str(date(int(re.match('.*(\d\d\d\d).*', start_date).group(1)), month, 1).toordinal())
    else:
        result['start_date'] = ''
        
    result['answer_time'] = account['data'][3]
#     answer_times = ['Редко отвечает на сообщения, рекомендуем звонить', 'Отвечает за несколько часов', 
#                     'Отвечает около часа', 'Отвечает в течение дня']
#     result['answer_call_recomended'] = int(answer_time == 'Редко отвечает на сообщения, рекомендуем звонить')
#     result['answer_several_hours'] = int(answer_time == 'Отвечает за несколько часов')
#     result['answer_one_hour'] = int(answer_time == 'Отвечает около часа')
#     result['answer_one_day'] = int(answer_time == 'Отвечает в течение дня')
    result['first_sold_time'] = '' if len(account['prod_data_finished']) == 0 else str(strtodays(account['prod_data_finished'][-1]))
    result['n_active'] = str(len(account['prod_data_active']))
    result['n_finished'] = str(len(account['prod_data_finished']))
    result['active_finished_ratio'] = str((len(account['prod_data_active']) + 1) / (len(account['prod_data_finished']) + 1))
    
    active_costs = []
    for cost in account['prod_cost_active']:
        active_costs.append(int(re.match('(\d*).*', cost.replace(' ', '')).group(1)))
        
    finished_costs = []
    for cost in account['prod_cost_finished']:
        finished_costs.append(int(re.match('(\d*).*', cost.replace(' ', '')).group(1)))
        
    result['min_active_cost'] = str(min(active_costs)) if len(active_costs) > 0 else ''
    result['max_active_cost'] = str(max(active_costs)) if len(active_costs) > 0 else ''
    result['mean_active_cost'] = str(sum(active_costs) / len(active_costs)) if len(active_costs) > 0 else ''
    
    result['min_finished_cost'] = str(min(finished_costs)) if len(finished_costs) > 0 else ''
    result['max_finished_cost'] = str(max(finished_costs)) if len(finished_costs) > 0 else ''
    result['mean_finished_cost'] = str(sum(finished_costs) / len(finished_costs)) if len(finished_costs) > 0 else ''
    return result