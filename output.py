import csv

def output_faculty_csv(timetable):
    with open('C:\\Users\\Kevin James T Kramer\\Documents\\School\\My Thesis\\Output CSVs\\faculty_schedule.csv', mode='w') as faculty_file:
        faculty_writer = csv.writer(faculty_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for x in timetable.faculty:
            faculty_writer.writerow([x.professor_id, x.first_name, x.last_name, x.schedule])



def output_timetable_csv(timetable):
    with open('C:\\Users\\Kevin James T Kramer\\Documents\\School\\My Thesis\\Output CSVs\\timetable.csv', mode='w') as timetable_file:
        timetable_writer = csv.writer(timetable_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        timetable_writer.writerow([timetable.fitness1, timetable.fitness2, timetable.fitness3])

        for x in timetable.offerings:
            timetable_writer.writer([x.offering_id, x.course_id, x.course_code, x.professor_id, x.room_id, x.timeslot1_id, x.timeslot2_id])





