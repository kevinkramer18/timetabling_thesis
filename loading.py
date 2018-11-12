# Import classes
from professor import Professor
from room import Room
from course import Course
from offering import Offering

# Import modules
import pymysql

# Declaring variables
course_list = []
faculty_list = []
room_list = []


def load_course_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT c1.course_id, c1.college_id, c1.dept_id, c1.course_code, c1.units, c1.course_type FROM timetabling.course c1 INNER JOIN timetabling.offering o1 ON c1.course_id = o1.course_id WHERE  o1.start_year =2013 AND o1.term=1 AND c1.course_id != 1686"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            course_id_value = row[0]
            college_id_value = row[1]
            dept_id_value = row[2]
            course_code_value = row[3]
            units_value = row[4]
            course_type_value = row[5]

            course = Course(course_id_value, college_id_value, dept_id_value, course_code_value, units_value, course_type_value)
            course_list.append(course)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return course_list



def load_room_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM timetabling.room WHERE room_code NOT LIKE '%AG%'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            room_id_value = row[0]
            room_code_value = row[1]
            room_type_value = row[3]
            room_capacity_value = row[4]

            room = Room(room_id_value, room_code_value, room_type_value, room_capacity_value)
            room_list.append(room)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return room_list


def load_faculty_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = ""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            room_id_value = row[0]
            room_code_value = row[1]
            room_type_value = row[3]
            room_capacity_value = row[4]

            professor = Professor()
            faculty_list.append(professor)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return faculty_list

