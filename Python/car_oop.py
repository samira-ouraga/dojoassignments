class Car(object):
    def __init__(self, price,speed,fuel,mileage):
        self.price = price
        self.speed = speed 
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def display_all(self):
        print "the price is " , self.price
        print  "the speed is" , self.speed , "mph"
        print "the fuel is at" , self.fuel 
        print "the mileage is ", self.mileage , "mpg"

        if self.price > 10000:
             self.tax += 15 
        else:
            self.tax += 12
        print "tax is ", self.tax 



car1 = Car(2000,34,"Full",500)

car1.display_all()
