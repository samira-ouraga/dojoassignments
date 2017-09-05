#Write a program that prints a 'checkerboard' pattern to the console
def my_checkerboard():
    list_one = ["*"," ","*"," ","*"," "]
    list_two = [" ","*"," ","*"," ","*"]
    for i in range(6):
        print " ".join(list_one)
        print " ".join(list_two)
print my_checkerboard()
