
#import sqlite3 
import sqlite3 as sql
#use conn instead of typing all of that
conn = sql.connect('db_strings.db')

#create the database if it doesn't exist already
with conn:
    #use cur instead of conn.cursor()
    cur = conn.cursor()
    #create table if it doesnt exist
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_string( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_strings TEXT \
        )")
    # == db.savechanges()
    conn.commit()



#filelist from assignment
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#iterate through filelist
for x in fileList:
    #grab all files that end with .txt 
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #insert files ending with .txt to db
            cur.execute("INSERT INTO tbl_string (col_strings) VALUES (?)", (x,))
            #== db.savechanges()
            conn.commit()
        #print to console
        print(x)
#close connection
conn.close()
