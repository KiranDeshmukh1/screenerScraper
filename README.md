
# StockScreener Scraper

A web scraper that scrapes data off from Screener.in
currently it is able to scrape core Financials and Sector





## Usage/Examples

```

from main import fundamentals

data = fundamentals('TCS','Quarterly Results')
print(data)

data_list = fundamentals(['TCS','INFY','SSWL'],'Cash Flows')
print(data_list)
```
Key available - 

Keys = 'Quarterly Results', 'Profit & Loss','Balance Sheet', 
            'Cash Flows', 'Ratios', 'Shareholding Pattern q', 
            'Shareholding Pattern y']





    Example 2

```
format - Sector(symbols)

data = Sector('TCS')
data_list = Sector(['TCS','INFY','SSWL'])