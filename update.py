import datetime

import pandas as pd
import streamlit as st
from database import *


def b_update():
    b_update = b_view_all_data()
    b_df = pd.DataFrame(b_update, columns=['Dept_No', 'Dept_Name','No_of_Staff', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Business Table Records"):
        st.dataframe(b_df)
    list_of_depts = [i[0] for i in view_only_b_names()]
    selected_dept = st.selectbox("Select Record to be Updated", list_of_depts)
    selected_result = b_get_details(selected_dept)
    # st.write(selected_result)
    if selected_result:
        Dept_No = selected_result[0][0]
        Dept_Name = selected_result[0][1]
        No_of_Staff = selected_result[0][2]
        Address_Street = selected_result[0][3]
        Address_City = selected_result[0][4]
        Address_State = selected_result[0][5]
        Address_Country = selected_result[0][6]
        Address_PIN = selected_result[0][7]
        Contact_TelNo = selected_result[0][8]
        Contact_Fax = selected_result[0][9]
        Contact_Email = selected_result[0][10]
        # Layout of Create

        col1, col2, col3 = st.columns(3)
        with col1:
            new_Dept_No = st.number_input("Department Number:")
            new_Dept_Name = st.text_input("Department Name:")
            new_No_of_Staff = st.number_input("Number Of Staff:")
        with col2:
            new_Address_Street = st.text_input("Address Street:")
            new_Address_City = st.text_input("Address City:")
            new_Address_State = st.text_input("Address State:")
            new_Address_Country = st.text_input("Address Country:")
            new_Address_PIN = st.text_input("Address PIN:")
        with col3:
            new_Contact_TelNo = st.text_input("Contact Telephone No:")
            new_Contact_Fax = st.text_input("Contact Fax:")
            new_Contact_Email = st.text_input("Contact E-Mail:")

        if st.button("Update Record"):
            b_edit_details(new_Dept_No, new_Dept_Name, new_No_of_Staff, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
            st.success("Successfully updated ->{} to ->{}".format(Dept_Name, new_Dept_Name))

    b_result = b_view_all_data()
    b_df2 = pd.DataFrame(b_result, columns=['Dept_No', 'Dept_Name','No_of_Staff', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("Updated data"):
        st.dataframe(b_df2)
    
def ab_update():
    ab_update = ab_view_all_data()
    ab_df = pd.DataFrame(ab_update, columns=['Reg_No', 'Dept_No', 'B_Name', 'Services_Offered', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Associate Businesses Table Records"):
        st.dataframe(ab_df)
    list_of_ab = [i[0] for i in view_only_ab_names()]
    selected_ab = st.selectbox("Select Record to be Updated", list_of_ab)
    selected_result = ab_get_details(selected_ab)
    # st.write(selected_result)
    if selected_result:
        Reg_No = selected_result[0][0]
        Dept_No = selected_result[0][1]
        B_Name = selected_result[0][2]
        Services_Offered = selected_result[0][3]
        Address_Street = selected_result[0][4]
        Address_City = selected_result[0][5]
        Address_State = selected_result[0][6]
        Address_Country = selected_result[0][7]
        Address_PIN = selected_result[0][8]
        Contact_TelNo = selected_result[0][9]
        Contact_Fax = selected_result[0][10]
        Contact_Email = selected_result[0][11]
        # Layout of Create

        col1, col2, col3 = st.columns(3)
        with col1:
            new_Reg_No = st.number_input("Registration Number:")
            new_Dept_No = st.number_input("Department Number:")
            new_B_Name = st.text_input("Business Name:")
            new_Services_Offered = st.text_input("Services Offered:")
        with col2:
            new_Address_Street = st.text_input("Address Street:")
            new_Address_City = st.text_input("Address City:")
            new_Address_State = st.text_input("Address State")
            new_Address_Country = st.text_input("Address_Country:")
            new_Address_PIN = st.text_input("Address_PIN:")
        with col3:
            new_Contact_TelNo = st.text_input("Contact Telephone No:")
            new_Contact_Fax = st.text_input("Contact Fax:")
            new_Contact_Email = st.text_input("Contact E-Mail:")

        if st.button("Update Record"):
            ab_edit_details(new_Reg_No, new_Dept_No, new_B_Name, new_Services_Offered, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No, Dept_No, B_Name, Services_Offered, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
            st.success("Successfully updated ->{} to ->{}".format(Reg_No, new_Reg_No))

    ab_result = ab_view_all_data()
    ab_df2 = pd.DataFrame(ab_result, columns=['Reg_No', 'Dept_No', 'B_Name', 'Services_Offered', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("Updated data"):
        st.dataframe(ab_df2)
        
def s_update():
    s_update = s_view_all_data()
    s_df = pd.DataFrame(s_update, columns=['Reg_No', 'Dept_No', 'S_Name', 'Incorp_Date', 'Period_of_Operation', 'No_of_Staff', 'B_Type', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("View Subsidary Table Records"):
        st.dataframe(s_df)
    list_of_s = [i[0] for i in view_only_s_names()]
    selected_s = st.selectbox("Select Record to be Updated", list_of_s)
    selected_result = s_get_details(selected_s)
    # st.write(selected_result)
    if selected_result:
        Reg_No = selected_result[0][0]
        Dept_No = selected_result[0][1]
        S_Name = selected_result[0][2]
        Incorp_Date = selected_result[0][3]
        
        No_of_Staff = selected_result[0][5]
        B_Type = selected_result[0][6]
        Address_Street = selected_result[0][7]
        Address_City = selected_result[0][8]
        Address_State = selected_result[0][9]
        Address_Country = selected_result[0][10]
        Address_PIN = selected_result[0][11]
        Contact_TelNo = selected_result[0][12]
        Contact_Fax = selected_result[0][13]
        Contact_Email = selected_result[0][14]
        # Layout of Create

        col1, col2, col3 = st.columns(3)
        with col1:
            new_Reg_No = st.number_input("Registration Number:")
            new_Dept_No = st.number_input("Department Number:")
            new_S_Name = st.text_input("Subsidary Name:")
            new_Incorp_Date = st.date_input("Date of Incorporation:")
            new_No_of_Staff = st.number_input("Number of Staff:")
            new_B_Type = st.text_input("Business Type:")
        with col2:
            new_Address_Street = st.text_input("Address Street:")
            new_Address_City = st.text_input("Address City:")
            new_Address_State = st.text_input("Address State")
            new_Address_Country = st.text_input("Address Country:")
            new_Address_PIN = st.text_input("Address PIN:")
        with col3:
            new_Contact_TelNo = st.text_input("Contact Telephone No:")
            new_Contact_Fax = st.text_input("Contact Fax:")
            new_Contact_Email = st.text_input("Contact E-Mail:")

        if st.button("Update Record"):
            new_Period_of_Operation = 0
            Period_of_Operation = 0
            s_edit_details(new_Reg_No, new_Dept_No, new_S_Name, new_Incorp_Date, new_Period_of_Operation, new_No_of_Staff, new_B_Type, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No, Dept_No, S_Name, Incorp_Date, Period_of_Operation, No_of_Staff, B_Type, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
            st.success("Successfully updated ->{} to ->{}".format(Reg_No, new_Reg_No))

    s_result = s_view_all_data()
    s_df2 = pd.DataFrame(s_result, columns=['Reg_No', 'Dept_No', 'S_Name', 'Incorp_Date', 'Period_of_Operation', 'No_of_Staff', 'B_Type', 'Address_Street', 'Address_City', 'Address_State', 'Address_Country', 'Address_PIN', 'Contact_TelNo', 'Contact_Fax', 'Contact_Email'])
    with st.expander("Updated data"):
        st.dataframe(s_df2)
        
def so_update():
    so_update = so_view_all_data()
    so_df = pd.DataFrame(so_update, columns=['Stock_ID', 'Stock_Purchaser', 'Dept_No', 'Stock_Type', 'Stock_Units', 'Stock_Value'])
    with st.expander("View Stock Options Table Records"):
        st.dataframe(so_df)
    list_of_so = [i[0] for i in view_only_so_names()]
    selected_so = st.selectbox("Select Record to be Updated", list_of_so)
    selected_result = so_get_details(selected_so)
    # st.write(selected_result)
    if selected_result:
        Stock_ID = selected_result[0][0]
        Stock_Purchaser = selected_result[0][1]
        Dept_No = selected_result[0][2]
        Stock_Type = selected_result[0][3]
        Stock_Units = selected_result[0][4]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Stock_ID = st.number_input("Stock ID:")
            new_Stock_Purchaser = st.text_input("Stock Purchaser:")
            new_Dept_No = st.number_input("Department Number:")
        with col2:
            new_Stock_Type = st.selectbox("Type of Stocks:", ["Emp Stock Purchase Plan", "Phantom Stock", "Restricted Stock Grant", "SARs"])
            new_Stock_Units = st.number_input("Amount of Stock Units:")

        if st.button("Update Record"):
            new_Stock_Value = 0
            Stock_Value = 0
            so_edit_details(new_Stock_ID, new_Stock_Purchaser, new_Dept_No, new_Stock_Type, new_Stock_Units, new_Stock_Value, Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value)
            st.success("Successfully updated ->{} to ->{}".format(Stock_ID, new_Stock_ID))

    so_result = so_view_all_data()
    so_df2 = pd.DataFrame(so_result, columns=['Stock_ID', 'Stock_Purchaser', 'Dept_No', 'Stock_Type', 'Stock_Units', 'Stock_Value'])
    with st.expander("Updated data"):
        st.dataframe(so_df2)
        
def bi_update():
    bi_update = bi_view_all_data()
    bi_df = pd.DataFrame(bi_update, columns=['Bill_ID', 'Stock_ID', 'Bill_Recipient', 'Bill_Date', 'Bill_Value'])
    with st.expander("View Bill Table Records"):
        st.dataframe(bi_df)
    list_of_bi = [i[0] for i in view_only_bi_names()]
    selected_bi = st.selectbox("Select Record to be Updated", list_of_bi)
    selected_result = bi_get_details(selected_bi)
    # st.write(selected_result)
    if selected_result:
        Bill_ID = selected_result[0][0]
        Stock_ID = selected_result[0][1]
        Bill_Recipient = selected_result[0][2]
        Bill_Date = selected_result[0][3]
        Bill_Value = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Bill_ID = st.number_input("Bill ID:")
            new_Stock_ID = st.number_input("Stock ID:")
        with col2:
            new_Bill_Recipient = st.text_input("Bill Recipient Name:")
            new_Bill_Date = st.date_input("Date of Bill:")
            new_Bill_Value = st.number_input("Value of Bill:")

        if st.button("Update Record"):
            bi_edit_details(new_Bill_ID, new_Stock_ID, new_Bill_Recipient, new_Bill_Date, new_Bill_Value, Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value)
            st.success("Successfully updated ->{} to ->{}".format(Bill_ID, new_Bill_ID))

    bi_result = bi_view_all_data()
    bi_df2 = pd.DataFrame(bi_result, columns=['Bill_ID', 'Stock_ID', 'Bill_Recipient', 'Bill_Date', 'Bill_Value'])
    with st.expander("Updated data"):
        st.dataframe(bi_df2)
        
def td_update():
    td_update = td_view_all_data()
    td_df = pd.DataFrame(td_update, columns=['Transc_ID', 'Dept_No', 'Reg_No', 'Bill_ID', 'Transc_Type', 'Transc_Date', 'Transc_Val'])
    with st.expander("View Transaction Details Table Records"):
        st.dataframe(td_df)
    list_of_td = [i[0] for i in view_only_td_names()]
    selected_td = st.selectbox("Select Record to be Updated", list_of_td)
    selected_result = td_get_details(selected_td)
    # st.write(selected_result)
    if selected_result:
        Transc_ID = selected_result[0][0]
        Dept_No = selected_result[0][1]
        Reg_No = selected_result[0][2]
        Bill_ID = selected_result[0][3]
        Transc_Type = selected_result[0][4]
        Transc_Date = selected_result[0][5]
        Transc_Val = selected_result[0][6]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Transc_ID = st.number_input("Transaction ID:")
            new_Dept_No = st.number_input("Department Number (If Applicable):")
            new_Reg_No = st.number_input("Registration Number (If Applicable):")
            new_Bill_ID = st.number_input("Bill ID (If Applicable):")
        with col2:
            new_Transc_Type = st.selectbox("Type of Transaction:", ["Business Transaction", "Subsidary Transaction", "Stock Transaction"])
            new_Transc_Date = st.date_input("Date of Transaction:")
            new_Transc_Val = st.text_input("Value of Transaction:")

        if st.button("Update Record"):
            if new_Dept_No > 0:
                new_Reg_No= None
                new_Bill_ID= None
            elif new_Reg_No > 0:
                new_Dept_No= None
                new_Bill_ID= None
            elif new_Bill_ID > 0:
                new_Dept_No = None
                new_Reg_No = None
            td_edit_details(new_Transc_ID, new_Dept_No, new_Reg_No, new_Bill_ID, new_Transc_Type, new_Transc_Date, new_Transc_Val, Transc_ID, Dept_No, Reg_No, Bill_ID, Transc_Type, Transc_Date, Transc_Val)
            st.success("Successfully updated ->{} to ->{}".format(Transc_ID, new_Transc_ID))

    td_result = td_view_all_data()
    td_df2 = pd.DataFrame(td_result, columns=['Transc_ID', 'Dept_No', 'Reg_No', 'Bill_ID', 'Transc_Type', 'Transc_Date', 'Transc_Val'])
    with st.expander("Updated data"):
        st.dataframe(td_df2)
        
