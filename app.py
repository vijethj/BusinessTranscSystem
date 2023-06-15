import streamlit as st
import mysql.connector

from create import *
from database import *
from delete import *
from read import *
from update import *
from Custom_Query import *

def main():
    st.title("Business Transaction Processing & DBMS")
    table_menu = ["Business", "Associate Business", "Subsidaries", "Stock Options", "Bill", "Transaction Details"]
    table_choice = st.sidebar.selectbox("View Tables", table_menu)
    menu = ["Add Records", "View Table Records", "Edit Table Records", "Remove Records", "Execute Query"]
    choice = st.sidebar.selectbox("Menu", menu)
# create_table()
#Business Table 
    if table_choice == "Business":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            b_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            b_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            b_delete()

        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")

#Associate Business Table
    elif table_choice == "Associate Business":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            ab_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            ab_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            ab_delete()
        
        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")
    
#Subsidary Table    
    elif table_choice == "Subsidaries":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            s_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            s_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            s_delete()
        
        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")

#Stock Options Table
    elif table_choice == "Stock Options":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            so_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            so_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            so_delete()
        
        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")
            
#Bill Table    
    elif table_choice == "Bill":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            bi_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            bi_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            bi_delete()
        
        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")
            
#Transaction Details    
    elif table_choice == "Transaction Details":
        if choice == "Add Records":
            st.subheader("Enter Record Details:")
            td_create()

        elif choice == "View Table Records":
            st.subheader("View Record Details:")
            read()

        elif choice == "Edit Table Records":
            st.subheader("Edited Record Details:")
            td_update()

        elif choice == "Remove Records":
            st.subheader("Delete Record:")
            td_delete()
        
        elif choice == "Execute Query":
            query()
            
        else:
            st.subheader("404 Not Found...")
    
if __name__ == '__main__':
    main()