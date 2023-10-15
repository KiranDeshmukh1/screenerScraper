from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


def fetch_fd_data (symbols,key=None):
    
    if not isinstance(symbols, list):
        symbols = [symbols]  # Convert a single symbol to a list
   
    keys = ['quarterly_results', 'pnl_yearly','balance_sheet', 
            'cashflow', 'ratios', 'shareholding_pattern_quarterly', 
            'shareholding_pattern_yearly']
    
    all_results = {}
    
    for symbol in symbols:
        results = {}

    

        urls = [f'https://www.screener.in/company/{symbol}/',f'https://www.screener.in/company/{symbol}/consolidated/']

        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                break
            except requests.exceptions.RequestException:
                # If there's an error, proceed to the next URL
                pass


        #page = requests.get(url) 

        soup = BeautifulSoup(response.text,'html.parser')

        for i in range (7):

            table = soup.find_all('table',class_ = 'data-table')[i]

            column_header_raw = table.find_all('th')

            column_header = [headers.text.strip() for headers in column_header_raw]

            df = pd.DataFrame(columns= column_header)

            column_data = table.find_all('tr')

            for row in column_data[1:]:
                row_data = row.find_all('td')
                individual_row_data = [data.text.strip() for data in row_data]
                lenght = len(df)
                df.loc[lenght]=individual_row_data
                
                
                
            df.insert(0, 'Symbol', symbol)
            df = df.rename(columns={df.columns[1]: 'Particulars'})
            results[keys[i]] = df
        
        all_results[symbol] = results
            
            
            
    if key is not None:
        selected_results = {symbol: results[key] for symbol, results in all_results.items() if key in results}
        return selected_results
        
    else:
        return None


