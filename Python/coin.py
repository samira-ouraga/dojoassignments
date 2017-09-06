#Write a function that simulates tossing a coin 5,000 times.
#  Your function should print how many times the head/tail appears.


import random 
def coin_tosses(num):
    count = 0
    head = 0
    tail = 0
    sentence = ""

    for x in range(1, num):
        flip = random.randint(0,1)
        count += 1
        if flip == 1:
            head += 1
            side = "head"
            print "Attempt #", count, ": Throwing a coin... It's a ", side, "! Got ", head, "head(s) so far and", tail, "tail(s) so far"
        else:
            tail += 1
            side = "tail"
            print "Attempt #", count, ": Throwing a coin... It's a ", side, "! Got ", head, "head(s) so far and", tail, "tail(s) so far"
    

      
print coin_tosses(6)

