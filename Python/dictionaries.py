#create a dictionnary
# def about_me():
#     bio = {}
#     bio["name"] = "Samira"
#     bio["age"] = 26
#     bio["country of birth"] = "Ivory Coast"
#     bio["language"] = "French"

#     print bio
#     print "My name is {}".format(bio["name"])
#     print "I am {}".format(bio["age"])
#     print "I wam born in {}".format(bio["country of birth"])
#     print "My favorite language  is {}".format(bio["language"])
# about_me()

def user_dicto(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + str(some_key) + " " + "is" + " " + str(some_value)
print user_dicto({"name":"samira", "age": 26})