from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

import requests

def api_request():
    url = "https://booking-com.p.rapidapi.com/v1/car-rental/search"

    querystring = {"drop_off_longitude":"-84.419853","currency":"USD","sort_by":"recommended","drop_off_datetime":"2023-01-03 19:00:00","drop_off_latitude":"33.640411","from_country":"it","pick_up_longitude":"-84.419853","locale":"en-gb","pick_up_datetime":"2023-01-01 19:00:00","pick_up_latitude":"33.640411"}

    headers = {
	"X-RapidAPI-Key": "e2bfcb999amshb4c19de5b3c019ap1f1c11jsn1d16c1bf87d9",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    results = response.json()

    df = pd.DataFrame.from_dict(results['search_results'])

    df2 = pd.json_normalize(results, record_path =['search_results'])
    return df2

df2 = api_request()

def clean_api_df(data_df):
  df_cleaned = data_df.copy()
  
  #filter to the columns we want to keep
  columns_to_keep = ['vehicle_info.v_id', 'vehicle_info.v_name', 'vehicle_info.group', 'vehicle_info.transmission', 'route_info.dropoff.city', 'pricing_info.base_price', 'route_info.pickup.city']
  #filter to the types of vehicles in vehicle.group
  vehicle_groups_to_keep = ['Luxury']
  df_cleaned=df_cleaned[columns_to_keep]
  df_cleaned=df_cleaned[df_cleaned['vehicle_info.group'].isin(vehicle_groups_to_keep)]
  df_cleaned.rename(columns={'vehicle_info.v_id':'Vehicle_id', 'vehicle_info.v_name': 'Vehicle_Name', 'vehicle_info.group': 'Category', 'pricing_info.base_price': 'Base_Price','vehicle_info.transmission': 'Transmission', 'route_info.dropoff.city': 'Dropoff_City', 'route_info.pickup.city': 'Pickup_City'}, inplace=True)
  df_cleaned.sort_values(by='Base_Price', ascending=False, inplace=True)
  return df_cleaned

df_cleaned = clean_api_df(df2)


#querystring2 = {"drop_off_longitude":"-84.419853","currency":"USD","sort_by":"recommended","drop_off_datetime":"2022-11-20 19:00:00","drop_off_latitude":"33.640411","from_country":"it","pick_up_longitude":"-84.419853","locale":"en-gb","pick_up_datetime":"2022-11-18 19:00:00","pick_up_latitude":"33.640411"}
#response2 = requests.request("GET", url, headers=headers, params=querystring2)
#results2 = response2.json()
#df_attempt2 = pd.json_normalize(results2, record_path =['search_results'])
#df_cleaned_attempt2 = clean_api_df(df_attempt2)
#df_cleaned_attempt2
