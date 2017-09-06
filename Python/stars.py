def the_stars(my_list):
    for i in range(len(my_list)):
        my_list[i] *= "*"
    return my_list       
print the_stars([1,2,3,4])


def stars_and_letters(second_list):
    for i in range(len(second_list)):
        first_letter = second_list[i][0]
        print  first_letter * len(second_list[i])
print stars_and_letters(["tina","knowles","sasha",1,2])

