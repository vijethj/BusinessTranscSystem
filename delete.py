import pandas as pd
import streamlit as st
from database import *


def b_delete():
    b_delete = b_view_all_data()
    b_df = pd.DataFrame(b_delete, columns=['Dept_No', 'Dept_Name','No_of_Staff', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Business Table Records"):
        st.dataframe(b_df)

    list_of_depts = [i[0] for i in view_only_b_names()]
    selected_dept = st.selectbox("Department Records to Delete", list_of_depts)
    st.warning("Do you want to delete the following record? ->{}".format(selected_dept))
    if st.button("Delete Record"):
        b_delete_data(selected_dept)
        st.success("Record has been deleted successfully")
    b_result = b_view_all_data()
    b_df2 = pd.DataFrame(b_result, columns=['Dept_No', 'Dept_Name','No_of_Staff', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("Updated Business Table Records"):
        st.dataframe(b_df2)
        
def ab_delete():     
    ab_delete = ab_view_all_data()
    ab_df = pd.DataFrame(ab_delete, columns=['Reg_No', 'Dept_No', 'B_Name', 'Services_Offered', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Associate Businesses Table Records"):
        st.dataframe(ab_df)

    list_of_b_name = [i[0] for i in view_only_ab_names()]
    selected_b_name = st.selectbox("Associate Businesses Records to Delete", list_of_b_name)
    st.warning("Do you want to delete the following record? ->{}".format(selected_b_name))
    if st.button("Delete Record"):
        ab_delete_data(selected_b_name)
        st.success("Record has been deleted successfully")
    ab_result = ab_view_all_data()
    ab_df2 = pd.DataFrame(ab_result, columns=['Reg_No', 'Dept_No', 'B_Name', 'Services_Offered', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Associate Businesses Table Records"):
        st.dataframe(ab_df2)
    
def s_delete():  
    s_delete = s_view_all_data()
    s_df = pd.DataFrame(s_delete, columns=['Reg_No', 'Dept_No', 'S_Name', 'Incorp_Date', 'Period_of_Operation', 'No_of_Staff', 'B_Type', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Subsidary Table Records"):
        st.dataframe(s_df)

    list_of_s_name = [i[0] for i in view_only_s_names()]
    selected_s_name = st.selectbox("Subsidary Records to Delete", list_of_s_name)
    st.warning("Do you want to delete the following record? ->{}".format(selected_s_name))
    if st.button("Delete Record"):
        s_delete_data(selected_s_name)
        st.success("Record has been deleted successfully")
    s_result = s_view_all_data()
    s_df2 = pd.DataFrame(s_result, columns=['Reg_No', 'Dept_No', 'S_Name', 'Incorp_Date', 'Period_of_Operation', 'No_of_Staff', 'B_Type', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("Updated Subsidary Table Records"):
        st.dataframe(s_df2)
        
def so_delete():
    so_delete = so_view_all_data()
    so_df = pd.DataFrame(so_delete, columns=['Stock_ID', 'Stock_Purchaser', 'Dept_No', 'Stock_Type', 'Stock_Units', 'Stock_Value'])
    with st.expander("View Stock Options Table Records"):
        st.dataframe(so_df)

    list_of_so = [i[0] for i in view_only_so_names()]
    selected_so = st.selectbox("Stock Options Records to Delete", list_of_so)
    st.warning("Do you want to delete the following record? ->{}".format(selected_so))
    if st.button("Delete Record"):
        so_delete_data(selected_so)
        st.success("Record has been deleted successfully")
    so_result = so_view_all_data()
    so_df2 = pd.DataFrame(so_result, columns=['Stock_ID', 'Stock_Purchaser', 'Dept_No','Stock_Type', 'Stock_Units', 'Stock_Value'])
    with st.expander("Updated Stock Options Table Records"):
        st.dataframe(so_df2)
        
def bi_delete():  
    bi_delete = bi_view_all_data()
    bi_df = pd.DataFrame(bi_delete, columns=['Bill_ID', 'Stock_ID', 'Bill_Recipient', 'Bill_Date', 'Bill_Value'])
    with st.expander("View Bill Table Records"):
        st.dataframe(bi_df)

    list_of_bi = [i[0] for i in view_only_bi_names()]
    selected_bi = st.selectbox("Bill Records to Delete", list_of_bi)
    st.warning("Do you want to delete the following record? ->{}".format(selected_bi))
    if st.button("Delete Record"):
        bi_delete_data(selected_bi)
        st.success("Record has been deleted successfully")
    bi_result = bi_view_all_data()
    bi_df2 = pd.DataFrame(bi_result, columns=['Bill_ID', 'Stock_ID', 'Bill_Recipient', 'Bill_Date', 'Bill_Value'])
    with st.expander("Updated Bill Table Records"):
        st.dataframe(bi_df2)

        
def td_delete():
    td_delete = td_view_all_data()
    td_df = pd.DataFrame(td_delete, columns=['Transc_ID', 'Dept_No', 'Reg_No', 'Bill_ID', 'Transc_Type', 'Transc_Date', 'Transc_Val'])
    with st.expander("View Transaction Details Table Records"):
        st.dataframe(td_df)

    list_of_td = [i[0] for i in view_only_td_names()]
    selected_td = st.selectbox("Transaction Details Records to Delete", list_of_td)
    st.warning("Do you want to delete the following record? ->{}".format(selected_td))
    if st.button("Delete Record"):
        td_delete_data(selected_td)
        st.success("Record has been deleted successfully")
    td_result = td_view_all_data()
    td_df2 = pd.DataFrame(td_result, columns=['Transc_ID', 'Dept_No', 'Reg_No', 'Bill_ID', 'Transc_Type', 'Transc_Date', 'Transc_Val'])
    with st.expander("Updated Transaction Details Table Records"):
        st.dataframe(td_df2)
        
    
