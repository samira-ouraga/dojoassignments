#find and replace
# words = "It's thanksgiving day. It's my birthday,too!"
# result = words.find('day')
# print "substring let it:", result
# print words.replace("day", "month")

#Min and max of list
# x = [2,54,-2,7,12,98]
# print min(x)
# print max(x)

#first and last of list 
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x.index("world")
# print x[7]
# y = []
# y.append("hello")
# y.append("world")
# print y 

#new list 
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x 
a = x[:len(x)/2]
b = x[len(x)/2:]
print a 
print b
b.insert(0, a)
print b





