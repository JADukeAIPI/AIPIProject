# AIPIProject
 Title:
 Code project to predict luxury car rental demand. 

 Description:
 This project seeks to provide boutique rental car companies that specialize in luxury/exotic vehciles with an accurate demand forcast so they can better prepare their fleets. This is intended to be accomplished in a couple of ways. First, we compare current demand against against major social events that would promote high luxury car demand (e.g. major concerts, conventionss, and sporting events). Ideally, we would also utilize historic rental car demand to model the yearly seasonality, although our API sources do not provide past demand only information regarding future inventory. Historic data could be obtained through continued data collection over the next several months. Additionally, we model prices based on perceived demand related to holidays and major events. 

 How to Install:
 This repository is broken up into a number of files. There are jupyter notebooks. .py modules, a database, a streamlit webapp, and one included dataset. Catagorically, they are broken up as the following:

    Exploratory Files (internal data exploration):
    API Call.ipynb
    LuxuryCarAPIMultipleDates.ipynb
    WebScrapingAtlantaEvents.ipynb
    readcsv.ipynb
    EDA_and_modelling.ipynb

    Deployment Files (actuall files to run):
    db.ipynb
    APICall.py
    LuxuryCarAPIMultipleDates.py
    WebScrapingAtlantaEvents.py
    readcsv.py

    Streamlit HTML App:
    ???.io

    Database (don't touch this):
    rentaldb

    Included Dataset (don't touch this):
    CarRentalDataV1.csv

In order to install the project correctly, you will only need to interact with 1 file, db.ipynb and the html web application. First, run the db.ipynb notebook. There are specific instructions at the top of the notebook. Follow those and then open the streamlit html web application. 

How to Use the Project:

After you've successfully run the db.ipynmb notebook and opened the web app, it's a very straight forward process. Select your desired date range within the streamlite application to see our estimate of demand needs in terms of car rentals.

Credits:

This project would not be possible if not for the following people:

Cindy Chang - Project conception, APIs, and data cleaning
Chad Miller - Webscraping, modeling, and data cleaning
Christian Hollar - Streamlit app, APIs, and data cleaning
Justin Abernathy - DB, APIs, and data cleaning
 

