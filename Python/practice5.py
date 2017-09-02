#Write a program that compares two lists and prints a message depending on if the inputs are identical or not
def Comparing(list_one, list_two):    
    cmp(list_one, list_two)
    if list_one == list_two:
        print "the lists are the same "
    else:
        print "not the same"
print Comparing(['celery','carrots','bread','milk'], ['celery','carrots','bread','milk'])




