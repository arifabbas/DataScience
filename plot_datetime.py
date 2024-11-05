import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import pandas as pd
plt.style.use('fivethirtyeight')


df=pd.read_csv('data-date.csv')
df['Date']= pd.to_datetime(df['Date'])
df.sort_values('Date',inplace=True)

price_date=df['Date']
price_close=df['Close']

plt.plot_date(price_date,price_close, linestyle='solid')
plt.gcf().autofmt_xdate()

date_format=mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.title('Price Action')
plt.xlabel('Date')
plt.ylabel('Price')

plt.tight_layout()

plt.show()