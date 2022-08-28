#I read about the Gale-Shapley Algorithm in Algorithm Design by Jon Kleinberg and decided to attempt to code it.
#I can't really check a setup or a solution anywhere to see if either is right.
#I did confirm that a single test case is correct where all men are rejected by their first picks and all women ultimately end up with their first picks
#Given a list of men and a list of women with their own preferences, find a stable match.
#input: preferences for a set of n men and n women
#output: set of n marriages with no instabilities

class Man:
    def __init__(self, id):
        self.engaged = False #not engaged initially
        self.tracker = 0 #pointer to track where the man is on his list to propose to next woman
        self.id = id
    
    def preference(self, pref):
        self.pref = pref #each man has a preferred list of women

    def proposal_update(self):
        self.tracker += 1

class Woman:
    def __init__(self, pref, id):
        self.engaged = False #not engaged initially
        self.ranking_dict = {} #create a dictionary that stores the man's ID as a key and includes rank as a value
        self.id = id
        for rank in range(len(pref)):
            self.ranking_dict[pref[rank]] = rank

    def ranking_check(self, first_man, second_man): #return the preferred man in the woman's preference list
        if self.ranking_dict.get(first_man) < self.ranking_dict.get(second_man):
            return first_man
        return second_man
    
    def accept_proposal(self, man):
        self.engaged = True
        self.engaged_to = man
        print((self.engaged_to.id, self.id))

class Prospective_Men:
    def __init__(self):
        self.men = []
        self.length = 0
    
    def add(self, id):
        self.men.append(id) #doesn't matter where man is added so lets go with O(1) time complexity choice
        self.length += 1
    
    def find(self):
        self.length -= 1
        return self.men.pop() #doesn't matter which man is taken first so lets go with O(1) time complexity choice

class Prospective_Women:
    def __init__(self):
        self.women = []
        self.length = 0
    
    def add(self, id):
        self.women.append(id)
        self.length += 1
    

def stable_match(free_men, free_women):
    while free_men.length > 0: #while there is a free man, keep going
        current_man = free_men.find()
        while current_man.engaged is not True:
            prospective_woman = current_man.pref[current_man.tracker]
            if prospective_woman.engaged == False: #if woman is not engaged
                current_man.engaged = True #man is engaged
                prospective_woman.accept_proposal(current_man) #woman is engaged
            else:
                if prospective_woman.ranking_check(current_man, prospective_woman.engaged_to) == current_man:
                    prospective_woman.engaged_to.engaged = False #previous man is no longer engaged
                    free_men.add(prospective_woman.engaged_to) #previous man is added to free man
                    current_man.engaged = True #current man is engaged
                    prospective_woman.accept_proposal(current_man) #woman is engaged
                else:
                    current_man.tracker += 1 #move to next woman on man's preference list
    final_match = []
    for current_woman in free_women.women:
        final_match.append((current_woman.engaged_to.id, current_woman.id))
    return final_match


m1 = Man("m1")
m2 = Man("m2")
m3 = Man("m3")
w1 = Woman([m3, m1, m2], "w1")
w2 = Woman([m2, m1, m3], "w2")
w3 = Woman([m1, m2, m3], "w3")
m1.preference([w1, w2, w3])
m2.preference([w1, w2, w3])
m3.preference([w2, w1, w3])

free_men = Prospective_Men()
free_men.add(m3)
free_men.add(m2)
free_men.add(m1)
free_women = Prospective_Women()
free_women.add(w1)
free_women.add(w2)
free_women.add(w3)

print(stable_match(free_men, free_women))

