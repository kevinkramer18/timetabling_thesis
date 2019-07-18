import random


def crossover_process(topParent, bottomParent, child):


    for i in range(0, len(child.offerings)-1):
        rand = random.randint(1, 100)
        # -----------------------------------------------------------------------TOP PARENT-----------------------------------------------------------------------------------------

        #Gives the professor's index from the topparent
        print(topParent.offerings[i].professor_id)
        #print(child.faculty[next(j for j, x in enumerate(child.faculty) if x.professor_id == topParent.offerings[i].professor_id)].professor_id)
        tpProfessorIndex = next(j for j, x in enumerate(child.faculty) if x.professor_id == topParent.offerings[i].professor_id)
        print(tpProfessorIndex)

        #Gives the sched of the class from the topparent
        tpt1 = topParent.offerings[i].timeslot1_id
        tpt2 = topParent.offerings[i].timeslot2_id
        print(tpt1, tpt2)

        #tpt1begin_time gives the begin_time from the first parent timeslot
        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id))
        #print(str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].begin_time))
        tpt1begin_time = str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].begin_time)
        print(tpt1begin_time)

        #tpt2begin_time gives the begin_time from the second parent timeslot
        print(next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id))
        #print(str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].begin_time))
        tpt2begin_time = str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].class_day) + '-' + str(topParent.timeslots[next(j for j, x in enumerate(topParent.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].begin_time)
        print(tpt2begin_time)

        #Returns whether the timeslot1 in child is occupied or not from topParent
        print("*******************************")
        ctimeslot1 = child.timeslots[next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)].offering_id
        ctimeslot2 = child.timeslots[next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)].offering_id
        print(next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id))
        ctimeslot1index = next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot1_id)
        print(next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id))
        ctimeslot2index = next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == topParent.offerings[i].timeslot2_id)


        #-----------------------------------------------------------------------BOTTOM PARENT-----------------------------------------------------------------------------------------

        # Gives the professor's index from the bottomparent
        print(bottomParent.offerings[i].professor_id)
        # print(child.faculty[next(j for j, x in enumerate(child.faculty) if x.professor_id == bottomParent.offerings[i].professor_id)].professor_id)
        btmProfessorIndex = next(j for j, x in enumerate(child.faculty) if x.professor_id == bottomParent.offerings[i].professor_id)
        print(btmProfessorIndex)

        # Gives the sched of the class from the bottomparent
        btmt1 = bottomParent.offerings[i].timeslot1_id
        btmt2 = bottomParent.offerings[i].timeslot2_id
        print(btmt1, btmt2)

        # btm1begin_time gives the begin_time from the first parent timeslot
        print(next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id))
        # print(str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id)].class_day) + '-' + str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id)].begin_time))
        btmt1begin_time = str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id)].class_day) + '-' + str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots)if x.timeslot_id == bottomParent.offerings[ i].timeslot1_id)].begin_time)
        print(btmt1begin_time)



        if rand <= 60  and (child.faculty[tpProfessorIndex].units + topParent.offerings[i].units) <= child.faculty[tpProfessorIndex].load :
            if  tpt1begin_time not in child.faculty[tpProfessorIndex].schedule and tpt2begin_time not in child.faculty[tpProfessorIndex].schedule and ctimeslot1 == ""  and ctimeslot2 == "":
                child.offerings[i].professor_id = topParent.offerings[i].professor_id
                child.offerings[i].room_id = topParent.offerings[i].room_id
                child.offerings[i].timeslot1_id = topParent.offerings[i].timeslot1_id
                child.offerings[i].timeslot2_id = topParent.offerings[i].timeslot2_id
                child.offerings[i].college_id = topParent.offerings[i].college_id

                child.faculty[tpProfessorIndex].assigned_offerings.append(topParent.offerings[i].offering_id)
                child.faculty[tpProfessorIndex].schedule.append(tpt1begin_time)
                child.faculty[tpProfessorIndex].schedule.append(tpt2begin_time)
                child.faculty[tpProfessorIndex].units += topParent.offerings[i].units

                child.timeslots[ctimeslot1index].offering_id = topParent.offerings[i].offering_id
                child.timeslots[ctimeslot2index].offering_id = topParent.offerings[i].offering_id


        elif rand >= 60 and (child.faculty[btmProfessorIndex].units + bottomParent.offerings[i].units) <= child.faculty[btmProfessorIndex].load :


    return child