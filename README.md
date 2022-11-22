# AIPIProject
 Title:
 Code project to predict luxury car rental demand. 

 Description:
 This project seeks to provide boutique rental car companies that specialize in luxury/exotic vehciles with an accurate demand forcast so they can better prepare their fleets. This is intended to be accomplished in a couple of ways. First, we compare current demand against major social events that would promote high luxury car demand (e.g. major concerts, conventionss, and sporting events). Ideally, we would also utilize historic rental car demand to model the yearly seasonality, although our API sources do not provide past demand only information regarding future inventory. Historic data could be obtained through continued data collection over the next several months. Additionally, we model prices based on perceived demand related to holidays and major events. 

 How to Install:
 This repository is broken up into a number of files. There are exploratory analysis jupyter notebooks. Also there are .py modules, a database, a streamlit webapp, and one included dataset. In order to run this project and utilize our data pipeline, you must run the following files in order. 

    First you'll need to obtain a Booking.com API key in order to run any file in our project. 
    After you have obtained a key, please create a creds.py file in the main folder. This file should have the following function: api_key where creds.api_key is the Booking.com key.

    After you've obtained a key and created creds.py. Please run dbpopulated.ipynb. This file will create a database, pull data from the API, webscrape Atlanta Events, and Kaggle, clean the data, then populate multiple tables in a SQL lite 3 DB. 

    After you have populated the database. Please run dbquery.ipynb. This file will extract data from the db and make various SQL queries. 

    Additionally, open EDA_and_modeling.ipynb and select run all. This file will create all of the modeling inputs for our web application. 

    Lastly, open a terminal and navigate to ../Cloud Deployment/home.py and run "streamlit run home.py". This will open our web app and allow you to interact with it. 

Credits:

This project would not be possible if not for the following people:

Cindy Chang - Project conception, APIs, and data cleaning
Chad Miller - Webscraping, modeling, and data cleaning
Christian Hollar - Streamlit app, APIs, and data cleaning
Justin Abernathy - DB, APIs, and data cleaning
 

