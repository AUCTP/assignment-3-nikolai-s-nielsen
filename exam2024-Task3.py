import pandas as pd

url = 'https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv'

sales = pd.read_csv(url)

# date = pd.to_datetime(sales['Date'])

# print(date.head())

# Total sales per store per year 2014
sales['Date'] = pd.to_datetime(sales['Date'])

sales_2014 = sales[sales['Date'].dt.year == 2014]

total_sales_2014 = sales_2014.groupby('Store')['Sales'].sum()

print(total_sales_2014)

# Most consistent store
std = sales.groupby('Store')['Sales'].std()
most_consistent_store = std.idxmin()
cons = std.min()

print(f'\nMost consistent store is store nr. {most_consistent_store}')
print(f'Total sales is {round(cons)}\n')

# Total sales each month
# sales['Date'] = pd.to_datetime(sales['Date'])

# sales['Month'] = sales['Date'].dt.month

# total_sales_month = sales.groupby(['Store', 'Month'])['Sales'].sum()

# print(total_sales_month)

# sales['Date'] = pd.to_datetime(sales['Date'])


# Opret en 'Month' kolonne i formatet YYYY-MM
sales['Month'] = sales['Date'].dt.to_period('M').astype(str)

# Gruppér efter Store og Month og summer Sales
monthly_sales_trend = (
    sales.groupby(['Store', 'Month'])['Sales']
    .sum()
    .reset_index()
    .rename(columns={'Sales': 'TotalSales'})
)

# Vis resultat
print(monthly_sales_trend.head())