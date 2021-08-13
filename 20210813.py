import streamlit as st
import numpy as np
import pandas as pd
import time 

# st.title('My first app')
# st.write('Hello ItoMaru!')
# st.write(pd.DataFrame({
#     'first column': [1,2,3,4],
#     'second column': [10,20,30,40]
# }))

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column':[10,20,30,40]
})

df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76,-122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c'])

    chart_data

option = st.selectbox(
    'which number do you like best?',
    df['first column'])

'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

'Starting a long computation...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'