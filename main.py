from professor import Professor
from room import Room
from course import Course
from offering import Offering

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print(mydb)