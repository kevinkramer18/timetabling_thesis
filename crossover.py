import random


def crossover_process(topParent, bottomParent, child):


    for i in range(0, len(topParent.offerings)-1):
        rand = random.randint(1, 100)

        #Gives the sched of the class from the topparent
        tpt1 = topParent.offerings[i].timeslot1_id
        tpt2 = topParent.offerings[i].timeslot2_id
        print(tpt1, tpt2)

        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id))
        print(str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].begin_time))
        tpt1begin_time = str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].begin_time)
        print(tpt1begin_time)

        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id))
        print(str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].begin_time))
        tpt2begin_time = str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].begin_time)
        print(tpt2begin_time)

        if rand <= 60:
            child.offerings[i].professor_id = topParent.offerings[i].professor_id
            child.offerings[i].room_id = topParent.offerings[i].room_id

            child.offerings[i].timeslot1_id = topParent.offerings[i].timeslot1_id
            child.offerings[i].timeslot2_id = topParent.offerings[i].timeslot2_id
            child.offerings[i].college_id = topParent.offerings[i].college_id





    return child