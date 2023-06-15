import streamlit as st
import pandas as pd
from database import *

def b_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        Dept_No = st.number_input("Department Number:")
        Dept_Name = st.text_input("Department Name:")
        No_of_Staff = st.number_input("Number Of Staff:")
    with col2:
        Address_Street = st.text_input("Address Street:")
        Address_City = st.text_input("Address City:")
        Address_State = st.text_input("Address State:")
        Address_Country = st.text_input("Address Country:")
        Address_PIN = st.text_input("Address PIN:")
    with col3:
        Contact_TelNo = st.text_input("Contact Telephone No:")
        Contact_Fax = st.text_input("Contact Fax:")
        Contact_Email = st.text_input("Contact E-Mail:")
    if st.button("Add Record"):
        b_add_data(Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
        st.success("Successfully added Record: {}".format(Dept_Name))


def ab_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        Reg_No = st.number_input("Registration Number:")
        Dept_No = st.number_input("Department Number:")
        B_Name = st.text_input("Business Name:")
        Services_Offered = st.text_input("Services Offered:")
    with col2:
        Address_Street = st.text_input("Address Street:")
        Address_City = st.text_input("Address City:")
        Address_State = st.text_input("Address State")
        Address_Country = st.text_input("Address_Country:")
        Address_PIN = st.text_input("Address_PIN:")
    with col3:
        Contact_TelNo = st.text_input("Contact Telephone No:")
        Contact_Fax = st.text_input("Contact Fax:")
        Contact_Email = st.text_input("Contact E-Mail:")
    if st.button("Add Record"):
        ab_add_data(Reg_No, Dept_No, B_Name, Services_Offered, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
        st.success("Successfully added Record: {}".format(Reg_No))
        ab_proc = ab_func_view()
        ab = pd.DataFrame(ab_proc, columns=['B_Name', 'Dept_No', 'Affiliated_Dept'])
        with st.expander("Executed Function"):
            st.dataframe(ab)
        
def s_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        Reg_No = st.number_input("Registration Number:")
        Dept_No = st.number_input("Department Number:")
        S_Name = st.text_input("Subsidary Name:")
        Incorp_Date = st.date_input("Date of Incorporation:")
        No_of_Staff = st.number_input("Number of Staff:")
        B_Type = st.text_input("Business Type:")
    with col2:
        Address_Street = st.text_input("Address Street:")
        Address_City = st.text_input("Address City:")
        Address_State = st.text_input("Address State")
        Address_Country = st.text_input("Address Country:")
        Address_PIN = st.text_input("Address PIN:")
    with col3:
        Contact_TelNo = st.text_input("Contact Telephone No:")
        Contact_Fax = st.text_input("Contact Fax:")
        Contact_Email = st.text_input("Contact E-Mail:")
    if st.button("Add Record"):
        Period_of_Operation= 0
        s_add_data(Reg_No, Dept_No, S_Name, Incorp_Date, Period_of_Operation, No_of_Staff, B_Type, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email)
        st.success("Successfully added Record: {}".format(Reg_No))
        

def so_create():
    col1, col2 = st.columns(2)
    with col1:
        Stock_ID = st.number_input("Stock ID:")
        Stock_Purchaser = st.text_input("Stock Purchaser:")
        Dept_No = st.number_input("Department Number:")
    with col2:
        Stock_Type = st.selectbox("Type of Stocks:", ["Emp Stock Purchase Plan", "Phantom Stock", "Restricted Stock Grant", "SARs"])
        Stock_Units = st.number_input("Amount of Stock Units:")
    if st.button("Add Record"):
        Stock_Value= 0
        so_add_data(Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value)
        st.success("Successfully added Record: {}".format(Stock_ID))
        so_proc = so_proc_view()
        so = pd.DataFrame(so_proc, columns=['Stock_ID', 'Stock_Purchaser', 'Stock_Value'])
        with st.expander("Executed Procedure"):
            st.dataframe(so)
        


        
def bi_create():
    col1, col2 = st.columns(2)
    with col1:
        Bill_ID = st.number_input("Bill ID:")
        Stock_ID = st.number_input("Stock ID:")
    with col2:
        Bill_Recipient = st.text_input("Bill Recipient Name:")
        Bill_Date = st.date_input("Date of Bill:")
        Bill_Value = st.number_input("Value of Bill:")
    if st.button("Add Record"):
        bi_add_data(Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value)
        st.success("Successfully added Record: {}".format(Bill_ID))
       
        
def td_create():
    col1, col2 = st.columns(2)
    with col1:
        Transc_ID = st.number_input("Transaction ID:")
        Dept_No = st.number_input("Department Number (If Applicable):")
        Reg_No = st.number_input("Registration Number (If Applicable):")
        Bill_ID = st.number_input("Bill ID (If Applicable):")
    with col2:
        Transc_Type = st.selectbox("Type of Transaction:", ["Business Transaction", "Subsidary Transaction", "Stock Transaction"])
        Transc_Date = st.date_input("Date of Transaction:")
        Transc_Val = st.text_input("Value of Transaction:")
    if st.button("Add Record"):
        if Dept_No > 0:
            Reg_No= None
            Bill_ID= None
        elif Reg_No > 0:
            Dept_No= None
            Bill_ID= None
        elif Bill_ID > 0:
            Dept_No = None
            Reg_No = None
        td_add_data(Transc_ID, Dept_No, Reg_No, Bill_ID, Transc_Type, Transc_Date, Transc_Val)
        st.success("Successfully added Record: {}".format(Transc_ID))
