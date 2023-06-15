import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


def read():
    b_read = b_view_all_data()
    ab_read = ab_view_all_data()
    s_read = s_view_all_data()
    so_read = so_view_all_data()
    bi_read = bi_view_all_data()
    td_read = td_view_all_data()
    # st.write(result)
    b_df = pd.DataFrame(b_read, columns=['Dept_No', 'Dept_Name','No_of_Staff', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Business Table Records"):
        st.dataframe(b_df)
    ab_df = pd.DataFrame(ab_read, columns=['Reg_No', 'Dept_No', 'B_Name', 'Services_Offered', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Associate Businesses Table Records"):
        st.dataframe(ab_df)
    s_df = pd.DataFrame(s_read, columns=['Reg_No', 'Dept_No', 'S_Name', 'Incorp_Date', 'Period_of_Operation', 'No_of_Staff', 'B_Type', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Subsidary Table Records"):
        st.dataframe(s_df)
    so_df = pd.DataFrame(so_read, columns=['Stock_ID', 'Stock_Purchaser', 'Dept_No', 'Stock_Units', 'Stock_Type', 'Stock_Value'])
    with st.expander("View Stock Options Table Records"):
        st.dataframe(so_df)
    bi_df = pd.DataFrame(bi_read, columns=['Bill_ID', 'Stock_ID', 'Bill_Recipient', 'Bill_Date', 'Bill_Value'])
    with st.expander("View Bill Table Records"):
        st.dataframe(bi_df)
    td_df = pd.DataFrame(td_read, columns=['Transc_ID', 'Dept_No', 'Reg_No', 'Bill_ID', 'Transc_Type', 'Transc_Date', 'Transc_Val'])
    with st.expander("View Transaction Details Table Records"):
        st.dataframe(td_df)
        
