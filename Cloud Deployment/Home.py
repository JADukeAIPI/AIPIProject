import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime as dt

def deploy():

    st.title('Luxury Vehicle Rental Car Forecasting')
    st.header('Justin Abernathy, Cindy Change, Christian Hollar, & Chad Miller')
    
    # Model 1 - Predict Price
    date_input = st.text_input('Enter Date:','YYYY-MM-DD Format')

    if st.button('Predict Relative Price'):
        pd_Date = pd.Timestamp(date_input)

        # Luxury Price Model Features
        pd_Date = pd.Timestamp(date_input)
        trend = pd_Date - pd.Timestamp('2022-11-18')
        trend = trend.days
        number_of_week = pd_Date.day_of_week
        day_of_week = dt.strptime(date_input,'%Y-%m-%d').strftime('%A')
        score = get_score(date_input)

        st.write(f'Selected Date: {date_input}')
        st.write(f'Trend: {str(trend)}')
        st.write(f'Day of the Week: {day_of_week}')
        st.write(f'Score: {score}')
    else:
        st.write('Waiting for input...')

    # Model 2 - Predict Relative Demand
    # date_input = st.text_input('Enter Date:','YYYY-MM-DD Format')

    if st.button('Predict Relative Demand'):
        d = dt.strptime(date_input, '%Y-%m-%d').date()
        d = d.toordinal()
        pd_Date = pd.Timestamp(date_input)

        # Luxury Demand Model Features
        price_value = get_score(date_input)
        score_value = get_avg_price()
        mbenz_value = get_mercedes_benz(date_input)
        sfarm_value = get_state_farm(date_input)

        st.write(f'Selected Date: {str(date_input)}')
        st.write(f'Average Price: {str(price_value)}')
        st.write(f'Mercedez-Benz: {str(mbenz_value)}')
        st.write(f'State Farm: {str(sfarm_value)}')
        loaded_model = pickle.load(open('Models/count_model.pkl', 'rb'))
        pred_input = np.array([price_value, score_value, d, mbenz_value,sfarm_value])
        pred_input = pred_input.reshape(1,5)
        pred = loaded_model.predict(pred_input)

        baseline_count = get_baseline_count(date_input)
        ans = (pred[0] - baseline_count) / baseline_count * 100
        

        if(ans>0):
            ans = str(round(ans,2))+'%'
            st.write(f'We predict the demand will be {ans} greater than average!')
        else:
            ans = abs(ans)
            ans = str(round(ans,2))+'%'
            st.write(f'We predict the demand will be {ans} less than average!')
    else:
        st.write('Waiting for input...')

# Model Methods
def get_score(date):
    df_scores = pd.read_csv('Data/Score.csv')
    df_output = df_scores.loc[df_scores['Date']==date]
    return df_output.Score[0]

def get_avg_price():
    df_model = pd.read_csv('Data/ModelData.csv')
    return df_model['Average Price'].mean()

def get_mercedes_benz(date):
    df_model = pd.read_csv('Data/ModelData.csv')
    df_model = df_model.loc[df_model['Date']==date]
    return df_model['Mercedes-Benz Stadium'][0]

def get_state_farm(date):
    df_model = pd.read_csv('Data/ModelData.csv')
    df_model = df_model.loc[df_model['Date']==date]
    return df_model['State Farm Arena'][0]

def get_baseline_count(date):
    df_model = pd.read_csv('Data/ModelData.csv')
    return df_model['Count'].mean()

if __name__ == "__main__":
    # load_model()
    deploy()