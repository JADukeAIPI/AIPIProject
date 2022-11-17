from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import requests
import datetime
from datetime import datetime, timedelta, date

today_date = datetime.today().strftime('%Y-%m-%d')

def get_date(number_days_from_today):

  end_date = datetime.today() + timedelta(days=number_days_from_today)
  end_date=end_date.strftime('%Y-%m-%d')
  return end_date

def get_booking_data(start_date, end_date):
	url = "https://booking-com.p.rapidapi.com/v1/car-rental/search"
	querystring = {"drop_off_longitude":"-84.419853","currency":"USD","sort_by":"recommended","drop_off_datetime":end_date + ' 15:00:00',"drop_off_latitude":"33.640411","from_country":"it","pick_up_longitude":"-84.419853","locale":"en-gb","pick_up_datetime":start_date + " 15:00:00","pick_up_latitude":"33.640411"}

	headers = {
		"X-RapidAPI-Key": "3662501eefmsh25ecd880f1ff146p15a604jsn7f50708cd702",
		"X-RapidAPI-Host": "booking-com.p.rapidapi.com"}

	response = requests.request("GET", url, headers=headers, params=querystring)
	results = response.json()
	df = pd.json_normalize(results, record_path =['search_results'])

	return df

def clean_api_df(data_df):
  df_cleaned = data_df.copy()
  
  #filter to the columns we want to keep
  columns_to_keep = ['vehicle_info.v_id', 'vehicle_info.v_name', 'vehicle_info.group', 'vehicle_info.transmission', 'pricing_info.base_price', 'pricing_info.price']
  #filter to the types of vehicles in vehicle.group
  vehicle_groups_to_keep = ['Luxury']
  df_cleaned=df_cleaned[columns_to_keep]
  df_cleaned=df_cleaned[df_cleaned['vehicle_info.group'].isin(vehicle_groups_to_keep)]
  df_cleaned.rename(columns={'vehicle_info.v_id':'Vehicle_id', 'vehicle_info.v_name': 'Vehicle Name', 'vehicle_info.group': 'Category', 'pricing_info.base_price': 'Base Price', 'pricing_info.price': 'Price', 'vehicle_info.transmission': 'Transmission'}, inplace=True)
  df_cleaned.sort_values(by='Base Price', ascending=False, inplace=True)
  return df_cleaned

def get_bookings_multiple_dates(start_date = get_date(1), end_date = get_date(30)):
  dfs = []
  

  day = datetime.strptime(start_date, '%Y-%m-%d')
  last_day = datetime.strptime(end_date, '%Y-%m-%d')
  iterator=0
  while day<last_day:
    date_tuple = (day.strftime('%Y-%m-%d'), (day+timedelta(days=1)).strftime('%Y-%m-%d'))

    df_partial = clean_api_df(get_booking_data(*date_tuple))
    df_partial['Date Pickup']=date_tuple[0]
    df_partial['Date Dropoff'] = date_tuple[1]
    dfs.append(df_partial)
    day=day+timedelta(days=1)


  df = pd.concat([dfs[i] for i in range(len(dfs))], axis=0) 

  return df

df_next_60_days = get_bookings_multiple_dates(get_date(1), get_date(60))

cars_available = df_next_60_days.groupby('Date Pickup')['Vehicle Name'].count()

cars_prices = df_next_60_days.groupby(['Vehicle_id', 'Date Pickup'])['Price'].mean()

price_each_day = df_next_60_days.groupby('Date Pickup')['Price'].mean()

def create_df_for_model(df):
  df1=df.copy()
  df1['cars_available'] = df1.groupby('Date Pickup')['Vehicle Name'].transform('count')
  fleet_size = df1['cars_available'].max()
  df1['Reservations'] = df1['cars_available'].apply(lambda x: fleet_size-x)
  df1['Individual_car_prices'] = df1.groupby(['Vehicle_id', 'Date Pickup'])['Price'].transform('mean')
  df1['Avg_type_car_prices'] = df1.groupby(['Vehicle Name', 'Date Pickup'])['Price'].transform('mean')
  df1['Date Pickup'] = pd.to_datetime(df1['Date Pickup'])

  return df1

data = create_df_for_model(df_next_60_days)