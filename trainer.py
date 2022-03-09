from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from utils import cleaned_df
import pandas as pd
import warnings
import pickle
warnings.filterwarnings('ignore')


complete_df = pd.read_csv(
    'training/train.csv',
    delimiter=";",
    low_memory=False
)

filtered_df = complete_df[['sign_in_count',
                           'personal_url',
                           'about',
                           'avatar',
                           'extended_data',
                           'followers_count',
                           'following_count',
                           'invitations_count',
                           'failed_attempts',
                           'admin',
                           'is_spam']]


def train_model():
    # load data
    df = cleaned_df(filtered_df)
    # split data into X and y
    X, Y = df.iloc[:, :-1], df.iloc[:, -1]
    # split data into train and test sets
    seed = 7
    test_size = 0.33
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=test_size, random_state=seed)
    # fit model no training data
    model = XGBClassifier()
    model.fit(X_train, y_train)
    pickle.dump(model, open('training/new_model.pkl', 'wb'))


if __name__ == '__main__':
    train_model()
