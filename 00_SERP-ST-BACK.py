#imports
import pandas as pd
import warnings
import requests
from datetime import date, timedelta
warnings.filterwarnings('ignore')


def serp_00(api_key, data_source, date_start, date_end, date_frequency='', language, locations, keywords, domains='', filtering_criteria='',):
    #defining the days
    start = date(date_start)
    end = date(date_end)
    delta = end - start
    days = []
    for i in range(delta.days+1):
        day = start + timedelta(days=i)
        days.append(day.strftime('%m-%d-%Y'))
    #results
    results = []
    for i in range(0, len(days)-1):
        for location in locations:
            params = {
                'api_key': api_key,
                'search_type': data_source,
                'q':
            }
