#I read about the Gale-Shapley Algorithm in Algorithm Design by Jon Kleinberg and decided to attempt to code it.
#I can't really check a setup or a solution anywhere to see if either is right.
#Given a list of students and a list of hospitals with their own preferences, find a stable match.
#Each hospital may have multiple positions and there are more students than open positions
#input: preferences for a set of n m
#output: hospital student pairings with no instabilities

class Hospital:
    def __init__(self, id, num_pos):
        self.filled = False #all internships filled
        self.positions = num_pos
        self.tracker = 0 #pointer to track where the hospital is on its list to send an offer to the next student
        self.id = id
    
    def preference(self, pref):
        self.pref = pref #each hospital has a preferred list of students
    
    def position_check(self, increment):
        self.positions += increment
        if self.positions > 0:
            self.filled = False
        else:
            self.filled = True


class Student:
    def __init__(self, pref, id):
        self.found_internship = False #not engaged initially
        self.ranking_dict = {} #create a dictionary that stores the hospital's ID as a key and includes rank as a value
        self.id = id
        self.accepted = None
        for rank in range(len(pref)):
            self.ranking_dict[pref[rank]] = rank

    def ranking_check(self, first_hospital, second_hospital): #return the preferred hospital in the student's preference list
        if self.ranking_dict.get(first_hospital) < self.ranking_dict.get(second_hospital):
            return first_hospital
        return second_hospital
    
    def accept_internship(self, hospital):
        self.found_internship = True
        self.accepted = hospital

class Hospital_List:
    def __init__(self):
        self.hospitals = []
        self.length = 0
    
    def add(self, id):
        self.hospitals.append(id) #doesn't matter where man is added so lets go with O(1) time complexity choice
        self.length += 1
    
    def find(self):
        self.length -= 1
        return self.hospitals.pop() #doesn't matter which man is taken first so lets go with O(1) time complexity choice

class Prospective_Students:
    def __init__(self):
        self.students = []
        self.length = 0
    
    def add(self, id):
        self.students.append(id)
        self.length += 1

def stable_match(hospitals, students):
    while hospitals.length > 0: #while there is an available internship, keep going
        current_hospital = hospitals.find()
        while current_hospital.filled is not True:
            prospective_student = current_hospital.pref[current_hospital.tracker]
            if prospective_student.found_internship == False: #if student is available
                current_hospital.position_check(-1) #hospital position decreases by one
                prospective_student.accept_internship(current_hospital) #student accepts internship
            else:
                if prospective_student.ranking_check(current_hospital, prospective_student.accepted) == current_hospital:
                    prospective_student.accepted.position_check(1) #previous hospital loses the intern and now has an open spot
                    hospitals.add(prospective_student.accepted) #previous hospital is added to hospitals looking for intern list
                    current_hospital.position_check(-1) #current hospital gains an intern
                    prospective_student.accept_internship(current_hospital) #student accepts inernship
            current_hospital.tracker += 1 #move to next student on hospital's preference list
    final_match = []
    for current_student in students.students:
        if current_student.accepted is not None:
            final_match.append((current_student.id, current_student.accepted.id))
        else:
            final_match.append((current_student.id, current_student.accepted))
    return final_match


h1 = Hospital("h1", 1)
h2 = Hospital("h2", 1)
h3 = Hospital("h3", 4)
s1 = Student([h3, h2, h1], "s1")
s2 = Student([h1, h3, h2], "s2")
s3 = Student([h2, h1, h3], "s3")
s4 = Student([h2, h1, h3], "s4")
s5 = Student([h2, h1, h3], "s5")
s6 = Student([h2, h1, h3], "s6")
s7 = Student([h2, h1, h3], "s7")
h1.preference([s1, s2, s3, s4, s5, s6, s7])
h2.preference([s1, s3, s2, s4, s5, s6, s7])
h3.preference([s2, s1, s3, s4, s5, s7, s6])

hospitals = Hospital_List()
hospitals.add(h3)
hospitals.add(h2)
hospitals.add(h1)
students = Prospective_Students()
students.add(s1)
students.add(s2)
students.add(s3)
students.add(s4)
students.add(s5)
students.add(s6)
students.add(s7)

print(stable_match(hospitals, students))

