class Bike(object):
    def __init__(self, price,max_speed):
        self.price = price
        self.max_speed = max_speed 
        self.miles = 0

    def display_info(self): #here the self means for every bike ccreated above , do the code below
        print self.price
        print self.max_speed
        print self.miles
        return self 
    
    def ride(self):                 #here we will increase speed of all bikes  by 10 when called
        print "riding"
        self.miles += 10
        return self
    
    def reverse(self):
        if self.max_speed >= 5:
            print "reversing"
            self.max_speed -= 5
            return self

bike1 = Bike(300,20 )    #add details before calling so that self.price will have the number
bike2 = Bike(190,50)
bike3 = Bike(300,500)


# bike1.display_info()            #call the function but attached to the individual player to have his spec info
# bike1.ride()
# bike1.reverse() 

for i in range(3):
    bike1.ride()
bike1.reverse().display_info()

for j in range(2):
    bike2.ride().reverse()
bike2.display_info()

for k in range(3):
    bike3.reverse()
bike3.display_info()



        


# print "bike 1  price is ", bike1.price


    