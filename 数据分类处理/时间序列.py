import pandas as pd
def get_date_list(begin_date,end_date):
    date_list=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(begin_date,end_date))]
    return date_list
print(get_date_list('2019-09-17','2019-11-08'))
    