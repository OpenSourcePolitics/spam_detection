# import pdb
import pandas as pd
import numpy as np
import os


def cleaned_df(df):
    # pdb.set_trace()
    # df['sign_in_count'] = df['sign_in_count'].astype('Int64')
    # df['sign_in_count'].astype(str).astype(int)
    
    df['url_in_contributions']=df['comments'].apply(lambda x: 1 if 'http' in str(x) else 0)
    df.drop('comments', axis=1, inplace=True)
    # df['url_in_contributions']=df['comments'].apply(lambda x: 0 if 'http' in x else 1)
    df['personal_url'] = df['personal_url'].apply(
        lambda x: 0 if pd.isnull(x) else 1)
    df['about'] = df['about'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df['admin'] = df['admin'].apply(lambda x: 0 if pd.isnull(x) else 1)
    # df['blocked'] = df['blocked'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df['avatar'] = df['avatar'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df['extended_data'] = df['extended_data'].astype(
        str).apply(lambda x: 0 if x == '{}' else 1)
    df = df.replace(np.nan, 0)

    df = df.apply(pd.to_numeric)  # convert all columns of DataFrame
    return df


def check_for_token(request):
    return request.headers.get("AUTH_TOKEN") == os.getenv("AUTH_TOKEN")
