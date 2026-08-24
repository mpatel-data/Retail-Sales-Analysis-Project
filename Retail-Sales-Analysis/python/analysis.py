import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib as mpl

df = pd.read_csv("C:/Users/14mil/OneDrive/Documents/Projects/Data Analysis/Retail-Sales-Analysis/data/retail_sales.csv")                                                    #Load data set

df.head()
df.info()                                                                               #check for missing values

df['order_date'] = pd.to_datetime(df['order_date'], format='%d/%m/%Y')                  #convert dates to datetime format

df.info()                                                                               #check order_date is datetime

df["sales"] = df["sales"].str.replace(",", "")                                          #remove , from data values
df['sales'] = pd.to_numeric(df['sales'])

df.info()                                                                               #check sales is integer

#Feature engineering

df['year'] = df['order_date'].dt.year                                                   #year extracted from order date as integer
df['month'] = df['order_date'].dt.month                                                 #month extracted from order date as integer
df['month_name'] = pd.to_datetime(
    df['month'], format="%m"
).dt.strftime("%B")

counts = df['customer_name'].value_counts()                                             #number of orders per unique customer
df['number_of_orders'] = df['customer_name'].map(counts)
df.loc[df.duplicated('customer_name'), 'number_of_orders'] = ''

df['quarter'] = (((df['month'] - 1) // 3) + 1)                                          #defined quarter based off the month


#Exploratory Data Analysis                                               

regions = []                                                                           #list of regions
for r in df['region']:
    if r not in regions:
        regions.append(r)

region_sales = df.groupby(['region'])['sales'].sum()                                   #sales by region
plt.bar(regions, region_sales)
plt.ticklabel_format(style='plain', axis='y')
plt.show()


months = []                                                                           #list of months
for m in df['month']:
    if m not in months:
        months.append(m)

month_names = pd.to_datetime(months, format="%m").strftime("%B")                     #converts numerical month to month names

monthly_sales = df.groupby(['month'])['sales'].sum()
plt.plot(month_names, monthly_sales)
plt.title("Monthly Sales Trend")
plt.ticklabel_format(style='plain', axis='y')
plt.show()

sns.barplot(data=df, x='category', y='profit')
plt.show()

df.to_csv("C:/Users/14mil/OneDrive/Documents/Projects/Data Analysis/Retail-Sales-Analysis/data/cleaned_sales_data.csv", index=False)