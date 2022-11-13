
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json

today_date = datetime.today().strftime('%Y-%m-%d')

def get_end_date(number_days):

  end_date = datetime.today() + timedelta(days=number_days)
  end_date=end_date.strftime('%Y-%m-%d')
  return end_date

end_date = get_end_date(90)

def get_events(start_date = today_date, end_date = get_end_date(90), query_string = None):
    '''
    Scrapes data from Creative Loafing, Google events, and Discover Atlanta for the next time period and organizes the data in a DataFrame

    Inputs:
        Date range in terms of strings of YYYY-MM-DD for today and future date; default is today to today + 90 days
        Query string (default None) which will perform .query(query_string) on the dataframe

    Returns:
        events_df(DataFrame): DataFrame containing the scraped data for all upcoming events
    '''
    
    # URLS to search  
    #url = 'https://creativeloafing.com/atlanta-events/this-month' 
    #url2 ='https://www.google.com/search?q=atlanta+convention+center+events&oq=atlanta+convention+center+events&aqs=chrome..69i57j0i512j0i22i30l6.4881j0j7&sourceid=chrome&ie=UTF-8&ibp=htl;events&rciv=evn&sa=X&ved=2ahUKEwjIsY_c4J_7AhX-lWoFHWBFBBcQ66QDKAZ6BAgIEAw#htichips=date:month&htischips=date;month&htidocid=L2F1dGhvcml0eS9ob3Jpem9uL2NsdXN0ZXJlZF9ldmVudC8yMDIyLTExLTExfDI1MTcwNDI2NDQ0NjM3MjA4ODg%3D&htivrt=events&fpstate=tldetail'
    url3 = 'https://discoveratlanta.com/events/all/?startdate='+today_date+'&enddate='+(end_date)+'&date_sort=this-month'
    #url4 = 'https://www.google.com/search?lei=3P9qY9XjLZGvqtsPpuOckAE&q=atlanta+convention+calendar+2022&biw=1440&bih=764&dpr=2&ibp=htl;events&rciv=evn&sa=X&ved=2ahUKEwil94el95_7AhUZibAFHSDpDQkQ8eoFKAJ6BAgJEA8#htivrt=events&htidocid=L2F1dGhvcml0eS9ob3Jpem9uL2NsdXN0ZXJlZF9ldmVudC8yMDIyLTExLTExfDI1MTcwNDI2NDQ0NjM3MjA4ODg%3D&fpstate=tldetail'

    # Request the page and use BeautifulSoup to extract the contents
    #page = requests.get(url)
    #page2 = requests.get(url2)
    page3 = requests.get(url3)
    #page4 = requests.get(url4)
    
    #soup = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(page2.content, 'html.parser')
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    #soup4 = BeautifulSoup(page4.content, 'html.parser')

    #for now, just using url3
    events = soup3.find_all('article', class_='listing')
    
    event_dict={} #to store event info
    for event in events:
      title = event.find(attrs={'class':'listing-title'}).text
      dates = json.loads(event['data-eventdates'])
      location = event.find(attrs={'class':'subtitle location'}).text
      description = event.find(attrs={'class':"listing-copy detail"}).text     
      event_dict[title]={'Dates': dates, 'Location': location, 'Description': description}
 
    #create dataframe
    event_df = pd.DataFrame.from_dict(event_dict).T
    event_df.reset_index(inplace=True)
    event_df = event_df.rename(columns = {'index':'Event'})
    event_df = event_df.explode('Dates', ignore_index=True)
    event_df['Dates'] = pd.to_datetime(event_df['Dates'])
    event_df = event_df.sort_values(by='Dates', ascending=True).reset_index(drop=True)
    event_df = event_df[(event_df['Dates'] > start_date) & (event_df['Dates'] <= end_date)]
    #filter by query string if provided
    if query_string is not None:
      event_df = event_df.query(query_string, engine='python')
    
    return event_df

