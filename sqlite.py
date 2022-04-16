import sqlite3
from django.db import DatabaseError
from tabulate import tabulate

class Dtabase():
    def __init__(self , name , price , count , more):
        self.name = name
        self.price = price
        self.count = count
        self.more = more
        global conn 
        conn = sqlite3.connect("protect.db")
    @property
    def create(self):
        global c
        c = conn.cursor()
        with conn:
            c.execute('''CREATE TABLE IF NOT EXISTS protect(
                name text,
                price integer,
                count integer,
                more text
                )''')
    @property
    def add(self):
        with conn:
            c.execute("INSERT INTO protect VALUES(:name , :price , :count , :more)",{"name":self.name , "price":self.price , "count":self.count , "more":self.more})

    @property
    def print(self):
        c = conn.cursor()
        with conn:
            c.execute("SELECT * FROM protect")
            row = c.fetchall()

            return row
            
                
            
            
           
            


if __name__ == "__main__":
    
    #d1 = Dtabase("iphone14" , 1400 , 4 , "this is the next ihpone that will be available on app steore")
    #d1.create
    #d1.print
    pass
    
    
    
    