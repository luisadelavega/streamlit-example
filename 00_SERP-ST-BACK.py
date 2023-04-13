#imports
import pandas as pd
import warnings
import requests
from datetime import date, timedelta
warnings.filterwarnings('ignore')

#API KEY
#API_key = 'B7F057A0D22147D8958DD77E300D9EA3' (I don't know why there is a separate key)
API_key = '4DE19AF3BC48476BA672A24D03BCAF2E'

#the search query
query = 'COP27'

#DATE
start = date(2022,11,1) #including this day
end = date(2022,11,30) #excluding this day
delta = end - start   # returns timedelta
days = []
for i in range(delta.days + 1):
    day = start + timedelta(days=i)
    days.append(day.strftime("%m-%d-%Y"))

#COUNTRIES
countries = ['United+States', 'United+Kingdom']

#RESULTS
results = []
for i in range(0, len(days)-1):
    for country in countries:
        params = {
            'api_key': API_key,
            'search_type': 'news',
            'q': query,
            'news_type': 'all',
            'location': country,
            'hl': 'en',
            'lr':'lang_en',
            'time_period': 'custom',
            'time_period_min': days[i],
            'time_period_max': days[i+1],
            'num': '100'
        }
         # make the http GET request to Scale SERP
        try:
            api_result = requests.get('https://api.scaleserp.com/search', params)
            df = pd.DataFrame(api_result.json()['news_results'])
            df['date'] = days[i]
            results.append(df)
        except Exception as e:
            continue
        print(i)

#OUTPUT
df.to_csv('news.csv')