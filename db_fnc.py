import config
import MySQLdb

# Open database connection
#db = MySQLdb.connect(config.db_host,config.db_username,config.db_password,config.database )


def update_record():


    # Open database connection
    db = MySQLdb.connect(config.db_host,config.db_username,config.db_password,config.database )
    
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

def insert_record(table_name,fields,values):


    # Open database connection
    db = MySQLdb.connect(config.db_host,config.db_username,config.db_password,config.database )
        
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO {} ({}) values ({});".format(table_name,fields,values)
    #print sql
    try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
    except:
        print "failed"
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def read_record():


    # Open database connection
    db = MySQLdb.connect(config.db_host,config.db_username,config.db_password,config.database )
        

    # Open database connection
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # Now print fetched result
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                (fname, lname, age, sex, income )
    except:
           print "Error: unable to fecth data"

           # disconnect from server
           db.close()

def delete_record():

    
    # Open database connection
    db = MySQLdb.connect(config.db_host,config.db_username,config.db_password,config.database )
        
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        
    # disconnect from server
    db.close()
