import json
import pandas as pd
import requests

def load_data(store_id):
    # loading test dataset
    df_test = pd.read_csv('../../data/test.csv')
    df_store_raw = pd.read_csv('../../data/store.csv')

    # merge
    df_test = df10.merge(df_store_raw, on='Store')

    # choose store for predction
    df_test = df_test[df_test['Store'] == 22]

    return df_test


def filter_data(df):
    # remove closed days
    df = df[df['Open'] != 0]
    df = df[~df['Open'].isnull()]
    df = df.drop(columns=['Id'])

    # convert DataFrame to json
    data_j = df.to_json(orient='records')

    return data_j

def call_api(data_j):
    # API call
    url = ' https://rossman-prediction-sales.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data_j

    r = requests.post(url, data=data, headers=header)
    print(f'Status Code {r.status_code}')

    d1 = pd.DataFrame(r.json())
    d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()
    
    return d2

def return_predict_from_api(store_id):
    df_store = load_data(store_id)	
    df_store_filtered = filter_data(df_store)
    response_df = call_api(df_store_filtered)

    return d2['prediction'].values[0]
