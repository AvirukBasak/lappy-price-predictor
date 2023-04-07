import pickle

model = None

with open('models/lappy_price_predictor.pkl', 'rb') as file:
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
    print(f"predicted price: {predict_price(features)}")
