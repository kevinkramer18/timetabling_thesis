import random


def crossover_process(topParent, bottomParent, child):

    for i in range(0, len(child.offerings)-1):


        randParent = random.randint(1, 100)


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
        print("****************** Bottom Parent**********************")
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

        # btm2begin_time gives the begin_time from the second parent timeslot
        print(next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id))
        # print(str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id)].class_day) + '-' + str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id)].begin_time))
        btmt2begin_time = str(bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[ i].timeslot2_id)].class_day) + '-' + str( bottomParent.timeslots[next(j for j, x in enumerate(bottomParent.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id)].begin_time)
        print(btmt2begin_time)

        # Returns whether the timeslot1 in child is occupied or not from topParent
        print("*******************************")
        cbtmtimeslot1 = child.timeslots[next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id)].offering_id
        cbtmtimeslot2 = child.timeslots[next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id)].offering_id
        print(next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id))
        cbtmtimeslot1index = next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot1_id)
        print(next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id))
        cbtmtimeslot2index = next(j for j, x in enumerate(child.timeslots) if x.timeslot_id == bottomParent.offerings[i].timeslot2_id)



        if randParent <= 60  and (child.faculty[tpProfessorIndex].units + topParent.offerings[i].units) <= child.faculty[tpProfessorIndex].load :
            print("Top Parent Chosen")
            if tpt1begin_time not in child.faculty[tpProfessorIndex].schedule and tpt2begin_time not in child.faculty[tpProfessorIndex].schedule and ctimeslot1 == ""  and ctimeslot2 == "":
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

            else:


                while True:
                    rand = random.randint(0, len(child.timeslots) - 2)

                    if child.timeslots[rand].class_day == 'M' or child.timeslots[rand].class_day == 'T' and child.timeslots[rand].offering_id == '' and child.timeslots[rand +1 ].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[tpProfessorIndex].schedule:
                        child.offerings[i].professor_id = topParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand+1].timeslot_id
                        child.offerings[i].college_id = topParent.offerings[i].college_id

                        child.faculty[tpProfessorIndex].assigned_offerings.append(topParent.offerings[i].offering_id)
                        child.faculty[tpProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[tpProfessorIndex].schedule.append(child.timeslots[rand+1].class_day + '-' + str(child.timeslots[rand+1].begin_time))
                        child.faculty[tpProfessorIndex].units += topParent.offerings[i].units

                        child.timeslots[rand].offering_id = topParent.offerings[i].offering_id
                        child.timeslots[rand+1].offering_id = topParent.offerings[i].offering_id

                        break




                    elif child.timeslots[rand].class_day == 'W' or child.timeslots[rand].class_day == 'H' and child.timeslots[rand].offering_id == '' and child.timeslots[rand - 1].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[tpProfessorIndex].schedule:
                        child.offerings[i].professor_id = topParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand - 1].timeslot_id
                        child.offerings[i].college_id = topParent.offerings[i].college_id

                        child.faculty[tpProfessorIndex].assigned_offerings.append(topParent.offerings[i].offering_id)
                        child.faculty[tpProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[tpProfessorIndex].schedule.append(child.timeslots[rand -1].class_day + '-' + str(child.timeslots[rand - 1].begin_time))
                        child.faculty[tpProfessorIndex].units += topParent.offerings[i].units

                        child.timeslots[rand].offering_id = topParent.offerings[i].offering_id
                        child.timeslots[rand - 1].offering_id = topParent.offerings[i].offering_id

                        break

                    elif child.timeslots[rand].class_day == 'F' and child.timeslots[rand].offering_id == '' and child.timeslots[rand + 1].offering_id == '' and child.timeslots[rand].begin_time != 1245 and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[tpProfessorIndex].schedule:
                        child.offerings[i].professor_id = topParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand + 1].timeslot_id
                        child.offerings[i].college_id = topParent.offerings[i].college_id

                        child.faculty[tpProfessorIndex].assigned_offerings.append(topParent.offerings[i].offering_id)
                        child.faculty[tpProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[tpProfessorIndex].schedule.append( child.timeslots[rand + 1].class_day + '-' + str(child.timeslots[rand + 1].begin_time))
                        child.faculty[tpProfessorIndex].units += topParent.offerings[i].units

                        child.timeslots[rand].offering_id = topParent.offerings[i].offering_id
                        child.timeslots[rand + 1].offering_id = topParent.offerings[i].offering_id

                        break



        elif randParent >= 60 and (child.faculty[btmProfessorIndex].units + bottomParent.offerings[i].units) <= child.faculty[btmProfessorIndex].load:
            print("Bottom Parent Chosen")
            if btmt1begin_time not in child.faculty[btmProfessorIndex].schedule and btmt2begin_time not in child.faculty[btmProfessorIndex].schedule and cbtmtimeslot1 == "" and cbtmtimeslot2 == "":
                child.offerings[i].professor_id = bottomParent.offerings[i].professor_id
                child.offerings[i].room_id = bottomParent.offerings[i].room_id
                child.offerings[i].timeslot1_id = bottomParent.offerings[i].timeslot1_id
                child.offerings[i].timeslot2_id = bottomParent.offerings[i].timeslot2_id
                child.offerings[i].college_id = bottomParent.offerings[i].college_id

                child.faculty[btmProfessorIndex].assigned_offerings.append(bottomParent.offerings[i].offering_id)
                child.faculty[btmProfessorIndex].schedule.append(btmt1begin_time)
                child.faculty[btmProfessorIndex].schedule.append(btmt2begin_time)
                child.faculty[btmProfessorIndex].units += bottomParent.offerings[i].units

                child.timeslots[cbtmtimeslot1index].offering_id = bottomParent.offerings[i].offering_id
                child.timeslots[cbtmtimeslot2index].offering_id = bottomParent.offerings[i].offering_id
            else:
                while True:
                    rand = random.randint(0, len(child.timeslots) - 2)

                    if child.timeslots[rand].class_day == 'M' or child.timeslots[rand].class_day == 'T' and child.timeslots[rand].offering_id == '' and child.timeslots[rand +1 ].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[btmProfessorIndex].schedule:
                        child.offerings[i].professor_id = bottomParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand+1].timeslot_id
                        child.offerings[i].college_id =  bottomParent.offerings[i].college_id

                        child.faculty[btmProfessorIndex].assigned_offerings.append(bottomParent.offerings[i].offering_id)
                        child.faculty[btmProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[btmProfessorIndex].schedule.append(child.timeslots[rand+1].class_day + '-' + str(child.timeslots[rand+1].begin_time))
                        child.faculty[btmProfessorIndex].units +=  bottomParent.offerings[i].units

                        child.timeslots[rand].offering_id =  bottomParent.offerings[i].offering_id
                        child.timeslots[rand+1].offering_id =  bottomParent.offerings[i].offering_id

                        break




                    elif child.timeslots[rand].class_day == 'W' or child.timeslots[rand].class_day == 'H' and child.timeslots[rand].offering_id == '' and child.timeslots[rand - 1].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[btmProfessorIndex].schedule:
                        child.offerings[i].professor_id =  bottomParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand - 1].timeslot_id
                        child.offerings[i].college_id =  bottomParent.offerings[i].college_id

                        child.faculty[btmProfessorIndex].assigned_offerings.append( bottomParent.offerings[i].offering_id)
                        child.faculty[btmProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[btmProfessorIndex].schedule.append(child.timeslots[rand -1].class_day + '-' + str(child.timeslots[rand - 1].begin_time))
                        child.faculty[btmProfessorIndex].units +=  bottomParent.offerings[i].units

                        child.timeslots[rand].offering_id =  bottomParent.offerings[i].offering_id
                        child.timeslots[rand - 1].offering_id =  bottomParent.offerings[i].offering_id

                        break

                    elif child.timeslots[rand].class_day == 'F' and child.timeslots[rand].offering_id == '' and child.timeslots[rand + 1].offering_id == '' and child.timeslots[rand].begin_time != 1245 and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[btmProfessorIndex].schedule:
                        child.offerings[i].professor_id =  bottomParent.offerings[i].professor_id
                        child.offerings[i].room_id = child.timeslots[rand].room_code
                        child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                        child.offerings[i].timeslot2_id = child.timeslots[rand + 1].timeslot_id
                        child.offerings[i].college_id =  bottomParent.offerings[i].college_id

                        child.faculty[btmProfessorIndex].assigned_offerings.append( bottomParent.offerings[i].offering_id)
                        child.faculty[btmProfessorIndex].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                        child.faculty[btmProfessorIndex].schedule.append( child.timeslots[rand + 1].class_day + '-' + str(child.timeslots[rand + 1].begin_time))
                        child.faculty[btmProfessorIndex].units +=  bottomParent.offerings[i].units

                        child.timeslots[rand].offering_id =  bottomParent.offerings[i].offering_id
                        child.timeslots[rand + 1].offering_id =  bottomParent.offerings[i].offering_id

                        break

        else:
            print("*************************")
            print("Mutation")
            while True:
                rand_faculty = random.randint(0, len(child.faculty)-1)
                if (child.faculty[rand_faculty].units + bottomParent.offerings[i].units) <= child.faculty[rand_faculty].load :

                    while True:
                        rand = random.randint(0, len(child.timeslots) - 2)

                        if child.timeslots[rand].class_day == 'M' or child.timeslots[rand].class_day == 'T' and child.timeslots[rand].offering_id == '' and child.timeslots[rand + 1].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[rand_faculty].schedule:
                            child.offerings[i].professor_id = child.faculty[rand_faculty].professor_id
                            child.offerings[i].room_id = child.timeslots[rand].room_code
                            child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                            child.offerings[i].timeslot2_id = child.timeslots[rand + 1].timeslot_id


                            child.faculty[rand_faculty].assigned_offerings.append(child.offerings[i].offering_id)
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand + 1].class_day + '-' + str(child.timeslots[rand + 1].begin_time))
                            child.faculty[rand_faculty].units += child.offerings[i].units

                            child.timeslots[rand].offering_id = child.offerings[i].offering_id
                            child.timeslots[rand + 1].offering_id = child.offerings[i].offering_id

                        elif  child.timeslots[rand].class_day == 'W' or child.timeslots[rand].class_day == 'H' and child.timeslots[rand].offering_id == '' and child.timeslots[rand - 1].offering_id == '' and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time) not in child.faculty[rand_faculty].schedule:
                            child.offerings[i].professor_id = child.faculty[rand_faculty].professor_id
                            child.offerings[i].room_id = child.timeslots[rand].room_code
                            child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                            child.offerings[i].timeslot2_id = child.timeslots[rand - 1].timeslot_id


                            child.faculty[rand_faculty].assigned_offerings.append(child.offerings[i].offering_id)
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand - 1].class_day + '-' + str(child.timeslots[rand - 1].begin_time))
                            child.faculty[rand_faculty].units += child.offerings[i].units

                            child.timeslots[rand].offering_id = child.offerings[i].offering_id
                            child.timeslots[rand - 1].offering_id = child.offerings[i].offering_id

                            break

                        elif   child.timeslots[rand].class_day == 'F'  and child.timeslots[rand].offering_id == '' and child.timeslots[rand + 1].offering_id == '' and child.timeslots[rand].begin_time != 1245 and child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time)  not in child.faculty[rand_faculty].schedule:
                            child.offerings[i].professor_id = child.faculty[rand_faculty].professor_id
                            child.offerings[i].room_id = child.timeslots[rand].room_code
                            child.offerings[i].timeslot1_id = child.timeslots[rand].timeslot_id
                            child.offerings[i].timeslot2_id = child.timeslots[rand + 1].timeslot_id


                            child.faculty[rand_faculty].assigned_offerings.append(child.offerings[i].offering_id)
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand].class_day + '-' + str(child.timeslots[rand].begin_time))
                            child.faculty[rand_faculty].schedule.append(child.timeslots[rand + 1].class_day + '-' + str(child.timeslots[rand + 1].begin_time))
                            child.faculty[rand_faculty].units += child.offerings[i].units

                            child.timeslots[rand].offering_id = child.offerings[i].offering_id
                            child.timeslots[rand + 1].offering_id = child.offerings[i].offering_id


                    break




    return child