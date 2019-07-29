import csv

def output_faculty_csv(timetable):
    with open('C:\\Users\\Kevin James T Kramer\\Documents\\School\\My Thesis\\Output CSVs\\faculty_schedule.csv', mode='w') as faculty_file:
        faculty_writer = csv.writer(faculty_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for x in timetable.faculty:
            faculty_writer.writerow([x.professor_id, x.first_name, x.last_name, x.schedule])



def output_timetable_csv(timetable):
    with open('C:\\Users\\Kevin James T Kramer\\Documents\\School\\My Thesis\\Output CSVs\\timetable.csv', mode='w') as timetable_file:
        timetable_writer = csv.writer(timetable_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        timetable_writer.writerow(['Fitness1: ',timetable.fitness1,'Fitness2: ', timetable.fitness2])
        for x in timetable.offerings:
            timetable_writer.writerow([x.offering_id, x.course_id, x.course_code, x.professor_id, x.room_id, x.timeslot1_id, x.timeslot2_id])


def output_timeslots_csv(timetable):
    with open('C:\\Users\\Kevin James T Kramer\\Documents\\School\\My Thesis\\Output CSVs\\timeslots.csv', mode='w') as timeslots_file:
       timeslots_writer = csv.writer(timeslots_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

       for x in timetable.timeslots:
           if x.offering_id != "":
               timeslots_writer.writerow([x.timeslot_id, x.room_id, x.room_code, x.class_day, x.begin_time, x.end_time, x.offering_id])



