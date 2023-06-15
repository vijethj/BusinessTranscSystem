import streamlit as st
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='vijeth1728',
    database='pes1ug20cs499_project'
)
c = mydb.cursor()

def view_all_data():
    data = c.fetchall()
    return data

def query():
    st.subheader("Enter Custom Query:")
    cust = st.text_input("Custom Query:")
    if st.button("Execute Custom Query"):
        try:
            c.execute(cust)
            field_names = [i[0] for i in c.description]
            output = view_all_data()
            df = pd.DataFrame(output, columns=field_names)
            with st.expander("Output:"):
                st.dataframe(df)
        except Exception as e:
            st.error("Query failed. Reason: {}".format(e))

if __name__ == '__main__':
    main()