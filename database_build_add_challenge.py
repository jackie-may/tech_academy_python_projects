

import sqlite3
#importing sqlite3 gives us access to
#all the functions that sqlite offers


conn = sqlite3.connect('database1.db')
#the variable 'conn'
#'conn' is going to hold the connection to the database
#this action creates the file which will be empty
#until we add the contents further down in the code
#creates a db file in 'C:\python_projects' folder
cur = conn.cursor()
#accessing the cursor object and giving it the name 'c'
#c = cursor
#cursor operates the database when commands are given


def create_table():
#making create_table a function
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file_name TEXT \
            )")
        #execute is a built in command
        #common to use all caps for SQL commands
        #() = sqlite statement that we are passing in
        #'IF NOT EXISTS' = saying if it doesn't exist, create it


def data_entry():
#making data_entry a function so that it can be reused
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['information.docx'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['Hello.txt'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['myImage.png'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['myMovie.mpg'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['World.txt'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['data.pdf'])
        cur.execute("INSERT INTO tbl_files(col_file_name) VALUES (?)", \
                    ['myPhoto.jpg'])
        text = conn.cursor()
        text.execute("SELECT * FROM tbl_files WHERE SUBSTR (col_file_name, LENGTH(col_file_name) - 3,4) = '.txt'")
        result = text.fetchall()
        for x in result:
            print(x)


#runs the functions
create_table()
#creates the table
data_entry()
#adds the data





    














    
