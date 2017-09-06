#Create a function that takes in two lists and creates a single dictionary
#  where the first list contains keys and the second values
def switch_dict_to_lists():
    name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
    favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
    new_dict = {}
    new_dict = zip(name,favorite_animal)
    return new_dict
    
print switch_dict_to_lists()