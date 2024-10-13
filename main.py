#importing sqlite3
import sqlite3
#importing pandas
import pandas as pd
connection=sqlite3.connect("database.sqlite")
print("lucky you connection is established and at the end get out here!!!!!!!!!!!!!!!")
# moving on to reading the file and some other stuff
tables=pd.read_sql("SELECT * FROM Match",connection)
print(tables)
tablescd=pd.read_sql("SELECT FROM Match AVG(Win_Margin);",connection)
print(tables.info())
