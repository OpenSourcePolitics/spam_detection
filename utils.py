import pandas as pd
import numpy as np
import os

def cleaned_df(df):
    df['personal_url'] = df['personal_url'].apply(
        lambda x: 0 if pd.isnull(x) else 1)
    df['about'] = df['about'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df['avatar'] = df['avatar'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df['extended_data'] = df['extended_data'].astype(
        str).apply(lambda x: 0 if x == '{}' else 1)
    df = df.replace(np.nan, 0)
    df = df.apply(pd.to_numeric)  # convert all columns of DataFrame
    return df

def check_for_token(request):
    print(os.getenv("AUTH_TOKEN"))
    return request.headers.get("AUTH_TOKEN") == os.getenv("AUTH_TOKEN")