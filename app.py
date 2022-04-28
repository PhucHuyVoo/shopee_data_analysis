import queue
from turtle import color
import streamlit as st
import pandas as pd
import base64   
import matplotlib.pyplot as plt
import numpy as np
import os
from func.load_data import load_data
from func.plot import sale_plot
#Sales of Online Well-known Shoes Store on Shopee VietNam

st.title("Shopee Shoes Store Sales Apps")

st.markdown("""
This app show the sales of some well-know shore store on an online shopping
flatform in Viet Nam called Shopee.
* **Python libraries:** streamlit, pandas, matplotlib, numpy, selenium, bs4
This small project crawl data on Shopee.vn from a list of shop:
* Bitis (bitisvn)
* Bitas (bitas_store)
* ADDA (depthailannam)
* Vans, Converse (Drake Dang Khoa)
* Puma (puma.officialstore)
* Cox (cox_shoes_viet_nam)
* Timberland (timberlandvietnam)
* Dincox (dincox_shoes)
* DongHai (donghai.official)
* Deci (decivietnam)
* Vento (vento.official.store)
The data that I prepresent here is scraped from Shopee by myself. The code is
show in this [link](https://github.com/PhucHuyVoo). This is my attempt to crawl
data from shopee so it appear to have a considerable null value in column (solds).
""")

#Load a shop list to 'shops' varible
shop_lst = load_data()

#Load csv file
sales = pd.read_csv('D:\\Python\\shopee\\shopee_total_clean.csv')
shop = sales.groupby('shop')
# st.dataframe(sales)

#Sidebar - Shop selection
sorted_shop_unique = sorted(sales['shop'].unique())
selected_shop = st.sidebar.multiselect('Shop', sorted_shop_unique, sorted_shop_unique)

#Filtering data
sales_selected_shop = sales[ (sales['shop'].isin(selected_shop)) ]

#Display the filtering data
st.header('Display Sales Infomation in Selected Shop')
st.write('Data Dimension: ' + str(sales_selected_shop.shape[0]) + ' rows and ' + str(sales_selected_shop.shape[1]) + ' columns.')
st.dataframe(sales_selected_shop)

# Plot Closing Price of Query Symbol
num_shop = st.sidebar.slider('Number of Shops', 4, 11)

if st.button('Show Plots'):
    st.header('Sales comparison shop ')
    sale(sales,num_shop,shop_lst)
