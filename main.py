import numpy as np
import streamlit as st
import base64


st.set_page_config(page_title='Price on Ozon')

def set_css(main_bg):
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         @font-face {{
            font-family: "IBM Plex Sans", sans-serif;              
        }}
        .st-ae, .css-81oif8 {{
            font-size: 30px;
        }}
            .css-u3o8cc{{
                height: 72px;
            }}
        strong {{
            font-family: "IBM Plex Sans", sans-serif !important;
            font-weight: 500;               
        }}
         .egzxvld3, .e8zbici2 {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
         }}
         .egzxvld3, .e8zbici2, .e1fqkh3o3 {{
             background-size: cover;
             background-repeat: no-repeat;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_css('bg.jpg')


def price(selfprice, package, coef, amount_in_package, percent, comission):
    price = selfprice * coef * amount_in_package + package + comission
    price_with_tax = price + (price * percent)
    previos_price = price_with_tax + (price_with_tax * 0.7)
    return np.around(price_with_tax), np.around(previos_price)


selfprice = st.number_input('Введите себестоимость: ')
package = st.number_input('Введите стоимость упаковки: ')
coef = st.number_input('Введите коэфициент: ')
amount_in_package = st.number_input('Введите количество товаров в упаковке: ')
percent = st.number_input('Введите процент за налоги: ')
comission = st.number_input('Введите комиссию озона: ')

lst_if_prices =  price(selfprice, package, coef, amount_in_package, percent / 100, comission)

st.write(f'**Текущая стоимость: {lst_if_prices[0]}**')
st.write(f'**Предыдущая стоимость(зачеркнутая): {lst_if_prices[1]}**')