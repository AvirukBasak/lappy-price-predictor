from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

import pickle

df_cleaned = pd.read_csv('data/csv/laptop_details_cleaned.csv')

df_sel = pd.get_dummies(
    df_cleaned,
    columns=['os', 'cpu', 'ram_space', 'ram_type', 'storage_space', 'storage_type', 'touch_screen', 'warranty', 'display_size']
)

X_train, X_test, y_train, y_test = train_test_split(df_sel.drop('mrp', axis=1), df_sel['mrp'], test_size=0.2, random_state=42)

model = None

'''
model = LinearRegression()

r2 = 0
while r2 < 0.8:
    model.fit(X_train, y_train)
    r2 = model.score(X_test, y_test)

print(f"R² = {r2:.4f}")
'''

with open('data/model/lappy_price_predictor.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_price(features):
    df = pd.DataFrame(features, index=[0])
    df = pd.get_dummies(df, columns=['os', 'cpu', 'ram_space', 'ram_type', 'storage_space', 'storage_type', 'touch_screen', 'warranty', 'display_size'])
    missing_cols = set(X_train.columns) - set(df.columns)
    for col in missing_cols:
        df[col] = 0
    df = df[X_train.columns]
    return model.predict(df)[0]


def test():
    features = {
        'os': 'MAC OS',
        'cpu': 'APPLE M1',
        'ram_space': '16 GB',
        'ram_type': 'DDR4',
        'storage_space': '1 TB',
        'storage_type': 'SDD',
        'touch_screen': 'NO',
        'warranty': '1 Y',
        'display_size': '13.0'
    }
    r2 = model.score(X_test, y_test)
    print(f"R² = {r2:.4f}")
    print(f"predicted price: {predict_price(features)}")
