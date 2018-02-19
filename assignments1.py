import numpy as np
import random
import csv
from math import ceil

# get variables from stdin
number_assignments = input('How many assignements do you want to burden your students with:\n')
students_per_group = int(input('How many students shall work on an assignment max?:\n'))
name_csv_inp = input('The name of the csv-file?:\n')
name_csv_output = input('What shall be the name of the output file?:\n')

#variables

student_lst = np.genfromtxt(name_csv_inp, delimiter=("\n"))
#create list of students: [fn, ln, email]
for i in range(student_lst):g
    student_lst[i] = student_lst[i].split(",")

nmbr_students = len(student_lst)
nmbr_groups = ceil(nmbr_students/students_per_group)
odd_students = nmbr_students % students_per_group
c = csv.writer(open(name_csv_output, "wb"))
#shuffle the student list for each assignment
for j in range(number_assignments):
    rng = random.Random()
    rng.shuffle(student_lst)
    c.writerow('Assignment {}\n'.format(j))

    # case 1: there are a few odd students but not enough groups to distribute them on without departing more than 1
    # from given group size.
    # to do: keep group number but determine new group size. We favour many groups departing little from initial
    # group size over few groups departing more to a greater extend
    if odd_students < students_per_group - odd_students and odd_students >= nmbr_groups:
        students_per_group = ceil(nmbr_students / nmbr_groups)
        odd_students = nmbr_students % students_per_group
    # case 2: many odd students but not enough groups to fill them up to a new group without departing more than 1 from
    # given group size
    # check if this is even possible!!!
    elif odd_students >= students_per_group - odd_students and students_per_group -1 - odd_students > nmbr_groups:
        pass
    # case 3: groups fit perfectly
    elif odd_students == 0:
        for k in range(nmbr_groups):
            c.writerow(''.join(student_lst[k*students_per_group:(k+1)*students_per_group - 1,0]))
    # case 4: there are a few odd students and enough groups to distribute them on
    elif odd_students < students_per_group - odd_students and odd_students < nmbr_groups:
        for k in range(nmbr_groups-1):
            #assign more students to the first groups
            if not k > odd_students:
                c.writerow(''.join(student_lst[k*students_per_group:(k+1 * students_per_group), 0]))
            #assign normal number of students to the last groups
            else:
                c.writerow(''.join(student_lst[k*students_per_group:(k+1) * students_per_group-1, 0]))
    # case 5: there are enough odd students to fill them up from other groups to a new group
    else:
        for k in range(nmbr_groups):
            # make first groups one smaller to fill up last one
            if k <= students_per_group - odd_students:
                c.writerow(''.join(student_lst[k * students_per_group:(k + 1) * students_per_group - 2, 0]))
            # make last groups of normal size
            else:
                c.writerow(''.join(student_lst[k * students_per_group:(k + 1) * students_per_group - 1, 0]))
    c.writerow('\n')


















