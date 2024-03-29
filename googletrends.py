# connect to google 

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-ID', tz=360) 

# build payload

kw_list = ["machine learning"] # list of keywords to get data 

pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

#1 Interest over Time
data = pytrends.interest_over_time() 
data = data.reset_index() 


import plotly.express as px

fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
fig.show() 

pytrends.get_historical_interest(kw_list, year_start=2021, month_start=9, day_start=1, hour_start=0, year_end=2021, month_end=9, day_end=30, hour_end=0, cat=0, sleep=0)

by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)

by_region.head(10) 

# by region greater than 10 searches
by_region[by_region["machine learning"] > 10]

data  = pytrends.related_queries()

data['machine learning']['top'] 

keywords = pytrends.suggestions(keyword='Business Intelligence')
df = pd.DataFrame(keywords)
print(df)


