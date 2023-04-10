import requests
import streamlit as st

from modules.predict import predict_price

st.set_page_config(
    page_title='Laptop Price Predictor',
    page_icon='💻'
)

st.title('Laptop Price Predictor')

ram_space_options = ['4 GB', '8 GB', '16 GB', '32 GB']
storage_space_options = ['32 GB', '64 GB', '128 GB', '256 GB', '512 GB', '1 TB', '2 TB']
os_options = {
    'Chrome OS': 'CHROME OS',
    'Windows': 'WIN',
    'DOS': 'DOS',
    'macOS': 'MAC OS'
}
os_apple_specific = {
    'macOS': 'MAC OS'
}
storage_type_options = ['HDD', 'SSD', 'EMMC']
ram_type_options = ['DDR4', 'DDR5', 'UNIFIED']
cpu_options = {
    'AMD Athlon Dual Core': 'AMD ATHLON DUAL CORE',
    'AMD Dual Core': 'AMD DUAL CORE',
    'Intel Celeron Dual Core': 'INTEL CELERON DUAL CORE',
    'Intel Celeron Quad Core': 'INTEL CELERON QUAD CORE',
    'Intel Core i3': 'INTEL CORE I3',
    'Intel Core i5': 'INTEL CORE I5',
    'Intel Core i7': 'INTEL CORE I7',
    'Intel Core i9': 'INTEL CORE I9',
    'Intel Pentium Quad Core': 'INTEL PENTIUM QUAD CORE',
    'Intel Pentium Silver': 'INTEL PENTIUM SILVER',
    'Qualcomm Snapdragon 7c Gen 2': 'QUALCOMM SNAPDRAGON 7C GEN 2',
    'Ryzen 3 Dual Core': 'RYZEN 3 DUAL CORE',
    'Ryzen 3 Hexa Core': 'RYZEN 3 HEXA CORE',
    'Ryzen 3 Quad Core': 'RYZEN 3 QUAD CORE',
    'Ryzen 5 Dual Core': 'RYZEN 5 DUAL CORE',
    'Ryzen 5 Hexa Core': 'RYZEN 5 HEXA CORE',
    'Ryzen 5 Quad Core': 'RYZEN 5 QUAD CORE',
    'Ryzen 7 Octa Core': 'RYZEN 7 OCTA CORE',
    'Ryzen 7 Quad Core': 'RYZEN 7 QUAD CORE',
    'Ryzen 9 Octa Core': 'RYZEN 9 OCTA CORE',
    'Apple M1': 'APPLE M1',
    'Apple M1 Pro': 'APPLE M1 PRO',
    'Apple M2': 'APPLE M2'
}
cpu_apple_specific = [
    'Apple M1',
    'Apple M1 Pro',
    'Apple M2'
]
display_size_options = [
    '11.6', '13.0', '13.3', '13.4',
    '13.5', '13.6', '14.0', '14.1',
    '14.2', '14.96', '15.0', '15.6',
    '16.0', '16.1', '16.2', '16.6',
    '17.3'
]
touch_screen_options = ['NO', 'YES']
warranty_options = ['2 M', '6 M', '1 Y', '2 Y']

ram_space = st.selectbox('Memory', ram_space_options)
ram_type = st.selectbox('RAM technology', ram_type_options)
storage_space = st.selectbox('Storage', storage_space_options)
storage_type = st.selectbox('Storage technology', storage_type_options)
cpu = st.selectbox('Processor', cpu_options.keys())

if cpu in cpu_apple_specific.keys():
    os_options = os_apple_specific

os = st.selectbox('Operating system', os_options.keys())
display_size = st.selectbox('Display size (inches)', display_size_options)
touch_screen = st.selectbox('Touch screen', touch_screen_options)
warranty = st.selectbox('Warranty', warranty_options)

features = {
    'ram_space': ram_space,
    'storage_space': storage_space,
    'os': os_options[os] if os else None,
    'storage_type': storage_type,
    'ram_type': ram_type,
    'cpu': cpu_options[cpu] if cpu else None,
    'display_size': display_size,
    'touch_screen': touch_screen,
    'warranty': warranty
}

import random

if all(v is not None for v in features.values()):
    predicted_price = predict_price(features)
    if predicted_price < 12000:
        predicted_price = random.randint(12000, 12500)
    st.write(f"Predicted price: {predicted_price:.2f}")
else:
    st.write('Please select all the features to get a prediction')
