#https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python
#server name: tappedin.database.windows.net
#databaase: TappedIn
#server admin login name: cfrench23
#password: Sh33pG1rl!0987

import pyodbc
from BeerClass import Beers

# connecting to the database
server = 'tappedin.database.windows.net'
database = 'TappedIn'
username = 'cfrench23'
password = 'Sh33pG1rl!0987'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

#The statements below query the Azure database, retrieving the desired info
cursor = cnxn.cursor()

# SQL query 
cursor.execute("SELECT * FROM dbo.Beer ")
row = cursor.fetchone()

while row:
    # str(row[X]) there needs to be one of these for each SELECT 
    # item in the query, with X being the unique value called
    #print (str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]) )
    row = cursor.fetchone()

def insert_drink(BeerType, BeerName, Brewery, IBU, ABV, BeerDesc):
    query = "INSERT INTO dbo.Beer(BeerType, BeerName, Brewery, IBU, ABV, BeerDesc) VALUES(?, ?, ?, ?, ?, ?)"
  
    #args info comes from crawler
    args = (BeerType, BeerName, Brewery, IBU, ABV, BeerDesc)
       
    try:
        # connecting to the database
        server = 'tappedin.database.windows.net'
        database = 'TappedIn'
        username = 'cfrench23'
        password = 'Sh33pG1rl!0987'
        driver= '{ODBC Driver 17 for SQL Server}'
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

        cursor = cnxn.cursor()

        print(query)
        cursor.execute(query, args)

        cnxn.commit()
 
    finally:
        cursor.close()
        cnxn.close()
 
def main(beer):
                #(      BeerType,             BeerName,             Brewery,               IBU,              ABV,                  BeerDesc)
   insert_drink(beer.__getBeerType__(),beer.__getName__(), beer.__getBrewery__(), beer.__getIBU__(), beer.__getABV__(), beer.__getBeerDescription__())
 
#if __name__ == '__main__':
 #   main(beer)