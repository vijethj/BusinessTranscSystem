SRN: PES1UG20CS499
Name: Vijeth APJ
Section: 5 I
Topic: Business Transaction Processing and DBMS

Frontend:
	Streamlit was used to code the frontend on VS Code
	Method used in coding is, .py files have been created for each CRUD operation like create.py, read.py, delete.py etc. including other necessary files such as
	app.py, database.py.
	The frontend consists of 6 different tables upon which CRUD operations can be performed.
	Each CRUD operation can be performed on a page of its own which can be selected in the side menu where one can first select the table name they would like to edit
	and then select the corresponding operation.
	There's another page in which the user can perform SQL queries and view the corresponding outputs.
	SQL Connector has been used to make the connection between frontend and backend possible.

Backend:
	MySQL Workbench has been used to monitor and keep track of the database in use which is 'pes1ug20cs499_project'
	Here various parameters for each table were constructed and defined. Population of the mentioned database was performed here as well.
	Functions, procedures, triggers were implemented in Workbench. 
	The tables created are: business, associate_businesses, subsidary, stock_options, bill, transaction_details.
	
Platform:
	Streamlit used for frontend
	MySQL Workbench used for backend
	MySQL Connector used
	