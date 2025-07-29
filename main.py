import streamlit as st
import langchainHelper




st.title("Restaurant Name Generator")

cuisine =st.sidebar.selectbox("Pick a Cuisine",("SriLankan","Indian","Italian","Mexican","American"))

if cuisine :
     response = langchainHelper.generate_resturant_name_and_item(cuisine)
    #  using strip to remove unncessory spaces and commas 
     st.header(response['resturant_name'].strip())
     menu_items = response['menu_items'].strip().split(",")
     st.write("Menu Items")
     for items in menu_items:
          st.write("-",items)