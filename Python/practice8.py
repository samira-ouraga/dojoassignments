#create a function that prints odd/even numbers
# def odd_even():
#     for i in range(2000):
#         if i%2 == 0:
#             print ("Number is " + str(i) +". "+  "this is an even number")
#         else:
#             print ("Number is " + str(i) + ". "+ "this is an odd number")
# print odd_even()

#create a function that multiplies
def multiply(mylist,num):
    for x in range(len(mylist)):
        mylist[x] *= num
    return mylist
a = [2,4,10,16]
b = multiply(a,5)
#print b

#write a function that multiply function callas argument
def layered_multiples(mylist):
    new_list = []
    for x in mylist:
        inner_list = []      
        for z in range(0,x):
            inner_list.append(1)
        new_list.append(inner_list)
    return new_list
x = layered_multiples(multiply([2,3,4],3))
print x
