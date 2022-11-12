import pandas as pd

def read_df(rental_file):
    '''
    Rreads a car rental CSV from Kaggle

    Inputs:
        CSV file with location, vehicle make, model, and daily rate information

    Returns:
        df(DataFrame): DataFrame containing the full CSV file
    '''
    
    # CSV to read into a DF
    df = pd.read_csv(rental_file)
    return df

df = read_df("CarRentalDataV1.csv")

def clean_and_sort_df(df):
    '''
    Sorts and cleans the CSV we just read into a DF

    Inputs:
        DataFrame of Car Rental Data

    Returns:
        df_ATL(DataFrame): DataFrame containing only vehciles rented in the Atlanta market. Also cleans up the naming conventions of the columns we
        need to interact with such as vehicle.type and vehicle.year
    '''
    df_ATL = df[df.airportcity == 'Atlanta']
    df_ATL = df_ATL.rename(columns = {'location.city': 'city', 'location.country' : 'country', 'location.latitude' : 'latitude',  'vehicle.make' : 'make', 'vehicle.model' : 'model', 'vehicle.type' : 'type', 'vehicle.year' : 'year', 'rate.daily' : 'daily_rate'})
    return df_ATL

df_ATL = clean_and_sort_df(df)

def sort_lux_df():
    '''
    Sorts the new Atlanta focused DF to only show vehicles considered luxury based on daily rate

    Inputs:
        Atlanta DataFrame

    Returns:
        df_ATL_lux(DataFrame): DataFrame containing only the luxury vehciles for rent in Atlanta
    '''
    df_ATL_lux = df_ATL[df_ATL.daily_rate > 150]
    return df_ATL_lux

df_ATL_lux = sort_lux_df()