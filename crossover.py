import random


def crossover_process(topParent, bottomParent, child):


    for i in range(0, len(topParent.offerings)-1):
        rand = random.randint(1, 100)

        t1 = topParent.offerings[i].timeslot1_id
        t2 = topParent.offerings[i].timeslot2_id
        print(t1, t2)
        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id))
        print(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].begin_time)
        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id))




        if rand <= 60:
            child.offerings[i].professor_id = topParent.offerings[i].professor_id
            child.offerings[i].room_id = topParent.offerings[i].room_id

            child.offerings[i].timeslot1_id = topParent.offerings[i].timeslot1_id
            child.offerings[i].timeslot2_id = topParent.offerings[i].timeslot2_id
            child.offerings[i].college_id = topParent.offerings[i].college_id





    return child