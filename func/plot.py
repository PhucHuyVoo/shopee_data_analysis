import matplotlib.pyplot as plt
import streamlit as st

def sale_plot(df,nos,shop_lst):
    names = []
    price = []
    for idx in range(nos):
        df2 = df[df['shop'] == shop_lst[idx]]
        df2 = df2['current_price'].astype(int)
        total_price = df2.sum()
        names.append(shop_lst[idx])
        price.append(total_price)
    plt.figure(facecolor='grey')
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])    
    plt.barh(names, price, color='red', edgecolor='black', align='center')
    ax.invert_yaxis() 
    ax.set_xlabel('Sales', fontweight='bold')
    ax.set_title('Sales comparison of {} shops on Shopee flatform'.format(nos))
    ax.set_facecolor(color='grey')
    return st.pyplot(fig)   