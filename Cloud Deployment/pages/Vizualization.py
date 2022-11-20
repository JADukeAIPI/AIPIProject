import streamlit as st
import pandas as pd
import altair as alt

st.markdown('Data Vizualization')
st.sidebar.markdown("Vizualization")
df = pd.read_csv('./pages/Data/LuxuryAPI.csv')

df['date'] = pd.to_datetime(df.Date_Pickup).dt.strftime('%Y-%m')

line_chart = alt.Chart(df).mark_line().encode(
    x= 'date',
    y='Price',
)

st.altair_chart(line_chart, use_container_width=True)

# df.groupby('Vehicle_Name')['Price'].plot(legend=True)
# plt.xlabel('Pick Up Date (YYYY-MM)')
# plt.ylabel('Price ($)')
# # plt.gca().xaxis.set_major_locator(mdate.MonthLocator())

# pd.pivot_table(df.reset_index(),
#                index='date', columns='Vehicle_Name', values='Price'
#               ).plot(subplots=True)