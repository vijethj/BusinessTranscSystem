import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vijeth1728",
    database="pes1ug20cs499_project"
)
c = mydb.cursor()


#def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS Train (Train_No int, Name varchar(30), Train_Type varchar(20), Source varchar(20), Destination varchar(20), Availability varchar(5));')


def b_add_data(Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email):
    c.execute('INSERT INTO business VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email))
    mydb.commit()

def ab_add_data(Reg_No, Dept_No, B_Name, Services_Offered, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email):
    c.execute('INSERT INTO associate_businesses VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (Reg_No, Dept_No, B_Name, Services_Offered, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email))
    mydb.commit()

def s_add_data(Reg_No, Dept_No, S_Name, Incorp_Date, Period_of_Operation, No_of_Staff, B_Type, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email):
    c.execute('INSERT INTO subsidary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (Reg_No, Dept_No, S_Name, Incorp_Date, Period_of_Operation, No_of_Staff, B_Type, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email))
    c.execute('CALL PeriodOfOp()')
    mydb.commit()
    
def so_add_data(Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value):
    c.execute('INSERT INTO stock_options VALUES (%s,%s,%s,%s,%s,%s)',
              (Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value))
    c.execute('CALL stocks_value()')
    mydb.commit()
    
def bi_add_data(Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value):
    c.execute('INSERT INTO bill VALUES (%s,%s,%s,%s,%s)',
              (Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value))
    mydb.commit()
    
def td_add_data(Transc_ID, Dept_No, Reg_No, Bill_ID, Transc_Type, Transc_Date, Transc_Val):
    c.execute('INSERT INTO transaction_details VALUES (%s,%s,%s,%s,%s,%s,%s)',
              (Transc_ID, Dept_No, Reg_No, Bill_ID, Transc_Type, Transc_Date, Transc_Val))
    mydb.commit()
    
  
def ab_func_view():
    c.execute('SELECT B_Name, Dept_No, affiliated_dept(Dept_No) FROM associate_businesses ORDER BY Dept_No')
    data = c.fetchall()
    return data 

def so_proc_view():
    global c 
    c.execute('CALL stocksval()')
    data = c.fetchall()
    return data
    c.close()  
    c = mydb.cursor()

def b_view_all_data():
    c.execute('SELECT * FROM business')
    data = c.fetchall()
    return data
def ab_view_all_data():
    c.execute('SELECT * FROM associate_businesses')
    data = c.fetchall()
    return data
def s_view_all_data():
    c.execute('SELECT * FROM subsidary')
    data = c.fetchall()
    return data
def so_view_all_data():
    c.execute('SELECT * FROM stock_options')
    data = c.fetchall()
    return data
def bi_view_all_data():
    c.execute('SELECT * FROM bill')
    data = c.fetchall()
    return data
def td_view_all_data():
    c.execute('SELECT * FROM transaction_details')
    data = c.fetchall()
    return data


def view_only_b_names():
    c.execute('SELECT Dept_Name FROM business')
    data = c.fetchall()
    return data
def view_only_ab_names():
    c.execute('SELECT B_Name FROM associate_businesses')
    data = c.fetchall()
    return data
def view_only_s_names():
    c.execute('SELECT S_Name FROM subsidary')
    data = c.fetchall()
    return data
def view_only_so_names():
    c.execute('SELECT Stock_Purchaser FROM stock_options')
    data = c.fetchall()
    return data
def view_only_bi_names():
    c.execute('SELECT Bill_Recipient FROM bill')
    data = c.fetchall()
    return data
def view_only_td_names():
    c.execute('SELECT Transc_ID FROM transaction_details')
    data = c.fetchall()
    return data


def b_get_details(Dept_Name):
    c.execute('SELECT * FROM business WHERE Dept_Name="{}"'.format(Dept_Name))
    data = c.fetchall()
    return data
def ab_get_details(B_Name):
    c.execute('SELECT * FROM associate_businesses WHERE B_Name="{}"'.format(B_Name))
    data = c.fetchall()
    return data
def s_get_details(S_Name):
    c.execute('SELECT * FROM subsidary WHERE S_Name="{}"'.format(S_Name))
    data = c.fetchall()
    return data
def so_get_details(Stock_Purchaser):
    c.execute('SELECT * FROM stock_options WHERE Stock_Purchaser="{}"'.format(Stock_Purchaser))
    data = c.fetchall()
    return data
def bi_get_details(Bill_Recipient):
    c.execute('SELECT * FROM bill WHERE Bill_Recipient="{}"'.format(Bill_Recipient))
    data = c.fetchall()
    return data
def td_get_details(Transc_ID):
    c.execute('SELECT * FROM transaction_details WHERE Transc_ID="{}"'.format(Transc_ID))
    data = c.fetchall()
    return data


def b_edit_details(new_Dept_No, new_Dept_Name, new_No_of_Staff, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email ):
    c.execute("UPDATE business SET Dept_No=%s, Dept_Name=%s, No_of_Staff=%s, Address_Street=%s, Address_City=%s, Address_State=%s, Address_Country=%s, Address_PIN=%s, Contact_TelNo=%s, Contact_Fax=%s, Contact_Email=%s WHERE " 
              "Dept_No=%s and Dept_Name=%s and No_of_Staff=%s and Address_Street=%s and Address_City=%s and Address_State=%s and Address_Country=%s and Address_PIN=%s and Contact_TelNo=%s and Contact_Fax=%s and Contact_Email=%s", (new_Dept_No, new_Dept_Name, new_No_of_Staff, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Dept_No, Dept_Name, No_of_Staff, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email))
    mydb.commit()
    data = c.fetchall()
    return data
def ab_edit_details(new_Reg_No, new_Dept_No, new_B_Name, new_Services_Offered, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No, Dept_No, B_Name, Services_Offered, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email):
    c.execute("UPDATE associate_businesses SET Reg_No=%s, Dept_No=%s, B_Name=%s, Services_Offered=%s, Address_Street=%s, Address_City=%s, Address_State=%s, Address_Country=%s, Address_PIN=%s, Contact_TelNo=%s, Contact_Fax=%s, Contact_Email=%s WHERE " 
              "Reg_No=%s", (new_Reg_No, new_Dept_No, new_B_Name, new_Services_Offered, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No))
    mydb.commit()
    data = c.fetchall()
    return data
def s_edit_details(new_Reg_No, new_Dept_No, new_S_Name, new_Incorp_Date, new_Period_of_Operation, new_No_of_Staff, new_B_Type, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No, Dept_No, S_Name, Incorp_Date, Period_of_Operation, No_of_Staff, B_Type, Address_Street, Address_City, Address_State, Address_Country, Address_PIN, Contact_TelNo, Contact_Fax, Contact_Email):
    c.execute("UPDATE subsidary SET Reg_No=%s, Dept_No=%s, S_Name=%s, Incorp_Date=%s, Period_of_Operation=%s, No_of_Staff=%s, B_Type=%s, Address_Street=%s, Address_City=%s, Address_State=%s, Address_Country=%s, Address_PIN=%s, Contact_TelNo=%s, Contact_Fax=%s, Contact_Email=%s WHERE " 
              "Reg_No=%s", (new_Reg_No, new_Dept_No, new_S_Name, new_Incorp_Date, new_Period_of_Operation, new_No_of_Staff, new_B_Type, new_Address_Street, new_Address_City, new_Address_State, new_Address_Country, new_Address_PIN, new_Contact_TelNo, new_Contact_Fax, new_Contact_Email, Reg_No))
    c.execute('CALL PeriodOfOp()')
    mydb.commit()
    data = c.fetchall()
    return data
def so_edit_details(new_Stock_ID, new_Stock_Purchaser, new_Dept_No, new_Stock_Type, new_Stock_Units, new_Stock_Value, Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value):
    c.execute("UPDATE stock_options SET Stock_ID=%s, Stock_Purchaser=%s, Dept_No=%s, Stock_Type=%s, Stock_Units=%s, Stock_Value=%s WHERE " 
              "Stock_ID=%s and Stock_Purchaser=%s and Dept_No=%s and Stock_Type=%s and Stock_Units=%s and Stock_Value=%s", (new_Stock_ID, new_Stock_Purchaser, new_Dept_No, new_Stock_Type, new_Stock_Units, new_Stock_Value, Stock_ID, Stock_Purchaser, Dept_No, Stock_Type, Stock_Units, Stock_Value))
    c.execute('CALL stocks_value()')
    mydb.commit()
    data = c.fetchall()
    return data 
def bi_edit_details(new_Bill_ID, new_Stock_ID, new_Bill_Recipient, new_Bill_Date, new_Bill_Value, Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value):
    c.execute("UPDATE bill SET Bill_ID=%s, Stock_ID=%s, Bill_Recipient=%s, Bill_Date=%s, Bill_Value=%s WHERE " 
              "Bill_ID=%s and Stock_ID=%s and Bill_Recipient=%s and Bill_Date=%s and Bill_Value=%s", (new_Bill_ID, new_Stock_ID, new_Bill_Recipient, new_Bill_Date, new_Bill_Value, Bill_ID, Stock_ID, Bill_Recipient, Bill_Date, Bill_Value))
    mydb.commit()
    data = c.fetchall()
    return data
def td_edit_details(new_Transc_ID, new_Dept_No, new_Reg_No, new_Bill_ID, new_Transc_Type, new_Transc_Date, new_Transc_Val, Transc_ID, Dept_No, Reg_No, Bill_ID, Transc_Type, Transc_Date, Transc_Val):
    c.execute("UPDATE transaction_details SET Transc_ID=%s, Dept_No=%s, Reg_No=%s, Bill_ID=%s, Transc_Type=%s, Transc_Date=%s, Transc_Val=%s WHERE " 
              "Transc_ID=%s", (new_Transc_ID, new_Dept_No, new_Reg_No, new_Bill_ID, new_Transc_Type, new_Transc_Date, new_Transc_Val, Transc_ID))
    mydb.commit()
    data = c.fetchall()
    return data


def b_delete_data(Dept_Name):
    c.execute('DELETE FROM business WHERE Dept_Name="{}"'.format(Dept_Name))
    mydb.commit()
def ab_delete_data(B_Name):
    c.execute('DELETE FROM associate_businesses WHERE B_Name="{}"'.format(B_Name))
    mydb.commit()
def s_delete_data(S_Name):
    c.execute('DELETE FROM subsidary WHERE S_Name="{}"'.format(S_Name))
    mydb.commit()
def so_delete_data(Stock_Purchaser):
    c.execute('DELETE FROM stock_options WHERE Stock_Purchaser="{}"'.format(Stock_Purchaser))
    mydb.commit()
def bi_delete_data(Bill_Recipient):
    c.execute('DELETE FROM bill WHERE Bill_Recipient="{}"'.format(Bill_Recipient))
    mydb.commit()
def td_delete_data(Transc_ID):
    c.execute('DELETE FROM transaction_details WHERE Transc_ID="{}"'.format(Transc_ID))
    mydb.commit()