# Import classes
from professor import Professor
from course import Course
from offering import Offering
from timeslot import Timeslot
# Import modules
import pymysql

# Declaring variables
course_list = []
faculty_list = []
offering_list = []
timeslot_list = []

def load_course_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT c1.course_id, c1.college_id, c1.dept_id, c1.course_code, c1.units, c1.course_type FROM timetabling.course c1 INNER JOIN timetabling.offering o1 ON c1.course_id = o1.course_id WHERE  o1.start_year =2015 AND o1.term=1 AND c1.course_id != 1686 AND c1.college_id =2"
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
            units_value = float(row[4])
            course_type_value = row[5]

            course = Course(course_id_value, college_id_value, dept_id_value, course_code_value, units_value, course_type_value)
            course_list.append(course)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return course_list



def load_faculty_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT users.user_id, users.first_name, users.last_name,  loads.teaching_load, coursepreference.course_id, coursepreference.course_id2, coursepreference.course_id3 FROM timetabling.users INNER JOIN timetabling.faculty ON faculty.user_id = users.user_id INNER JOIN timetabling.loads ON loads.faculty_id = faculty.faculty_id INNER JOIN timetabling.coursepreference ON coursepreference.user_id = users.user_id WHERE loads.term = 1 AND loads.start_year = 2013  "
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            professor_id_value = row[0]
            professor_fname_value = row[1]
            professor_lname_value = row[2]
            professor_load_value = float(row[3])
            cpref = row[4]
            cpref2 = row[5]
            cpref3 = row[6]

            professor = Professor(professor_id_value,professor_fname_value, professor_lname_value, professor_load_value)
            if cpref is not None:
                professor.preferred_courses.append(cpref)
            if cpref2 is not None:
                professor.preferred_courses.append(cpref2)
            if cpref3 is not None:
                professor.preferred_courses.append(cpref3)

            faculty_list.append(professor)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return faculty_list



def load_offering_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT offering.offering_id, offering.section, offering.course_id,  course.course_code, course.units, offering.max_students_enrolled, course.course_type,flowcourses.flowchart_id FROM timetabling.offering  INNER JOIN timetabling.course ON course.course_id = offering.course_id INNER JOIN timetabling.flowcourses on flowcourses.course_id=course.course_id where offering.term = 1 and start_year = 2015 and college_id = 2 and course_code != 'LBYECON' "
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            offering_id_value = row[0]
            section_value = row[1]
            course_id_value = row[2]
            course_code_value = row[3]
            units_value = float(row[4])
            max_students_value = int(row[5])
            course_type_value = row[6]
            flowchart_id_value = row[7]
            offering = Offering(offering_id_value,section_value, course_id_value,course_code_value, units_value, max_students_value, course_type_value,flowchart_id_value)
            offering_list.append(offering)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return offering_list



def load_timeslot_list():
    # Open database connection
    db = pymysql.connect("localhost", "root", "root", "mysql")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT timeslots.timeslots_id, timeslots.room_id, timeslots.class_day, timeslots.begin_time, timeslots.end_time, room.room_type, room.room_code, room.room_capacity FROM timetabling.timeslots INNER JOIN timetabling.room ON room.room_id = timeslots.room_id"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            timeslots_id_value = row[0]
            room_id_value = row[1]
            class_day_value = row[2]
            begin_time_value = row[3]
            end_time_value = row[4]
            room_type_value = row[5]
            room_code_value = row[6]
            room_capacity_value = row[7]




            timeslot = Timeslot(timeslots_id_value,room_id_value,class_day_value, begin_time_value, end_time_value, room_type_value, room_code_value, room_capacity_value )
            timeslot_list.append(timeslot)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return timeslot_list



