from professor import Professor
from room import Room
from course import Course
from offering import Offering


#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","mysql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM timetabling.course"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[4]

      # Now print fetched result
      print ("fname = %s" % \
         (fname ))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()