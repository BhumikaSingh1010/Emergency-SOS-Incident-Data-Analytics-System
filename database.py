import pyodbc

# SQL Server connection
connection = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=.\SQLEXPRESS;"
    r"DATABASE=EmergencySOS;"
    r"Trusted_Connection=yes;"
)

print("Connected to SQL Server successfully!")

connection.close()