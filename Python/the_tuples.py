#Write a function that takes in a dictionary 
# and returns a list of tuples where the first tuple item is the key and the second is the value.

def dict_to_tuple():
    my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
    }

    the_list = []
    for key,data in my_dict.iteritems():
        my_tuple = (key,data)
        #print my_tuple
        the_list.append(my_tuple)
    print (the_list)
        
    
print dict_to_tuple()