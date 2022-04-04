from cmath import nan
from xgboost import XGBClassifier
import pdb
from sklearn.model_selection import train_test_split
from utils import cleaned_df
import pandas as pd
import warnings
import pickle
from sklearn.metrics import accuracy_score

warnings.filterwarnings('ignore')


complete_df = pd.read_csv(
    'OSP.csv',
    delimiter=';',
    low_memory=False
)

filtered_df = complete_df[[
                          # 'sign_in_count',
                           'personal_url',
                           'about',
                           'avatar',
                           'extended_data',
                           'admin',
                          'blocked',
                          'is_spam'
                        ]]


print(filtered_df['personal_url'])
filtered_df = cleaned_df(filtered_df)
# # creating bool series False for NaN values
# # filtered_df['personal_url'] = filtered_df['personal_url'].fillna(0)
# filtered_df['avatar'] = filtered_df['avatar'].fillna(0)
# filtered_df['about'] = filtered_df['about'].fillna(0)
# # filtered_df['personal_url'] = { 1 for personal_url in filtered_df if filtered_df[personal_url].notna() else 0 }
# filtered_df.loc[filtered_df['personal_url'].isna(), 'personal_url'] = 0
# filtered_df.loc[filtered_df['personal_url'].notna(), 'personal_url'] = 1
# print(filtered_df['personal_url'].value_counts())
#     # load data
filtered_df.loc[(filtered_df['avatar'] != 0) &  (filtered_df['personal_url'] != 0) & (filtered_df['about'] != 0), 'is_spam'] = 1
filtered_df.loc[(filtered_df['personal_url'] != 0) & (filtered_df['about'] != 0), 'is_spam'] = 1
# penser aussi a la structure json dont on dispose afin de pouvoir labelliser (structure json spam detection 0,80...)
#     #ajouter & (filtered_df['blocked'] == 'true') quand on aura ùis le bon fichier 
#     # on peut également ajouter une colonne sur le script sql alter table pour toutes les personnes qui ont des propriétés de spammers
#     # noter que dans la table commentaires agréggés à utilisateurs ne va pas monter tous les spammers car certains spammers 
#     # n'ont aucun commentaire
    

# df = cleaned_df(filtered_df)
# pdb.set_trace() 
print(filtered_df.head(10))
print(filtered_df['is_spam'].value_counts())
# filtered_df.to_csv('csv_labellise.csv')
    # split data into X and y 
X, Y = filtered_df.iloc[:, :-1], filtered_df.iloc[:, -1]
#     # split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(
X, Y, test_size=test_size, random_state=seed)
#     # fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

