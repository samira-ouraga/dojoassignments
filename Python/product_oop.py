class Product(object):
    def __init__(self, price,item_name,weight,brand,status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.reason = ""
        self.tax = 0
        self.newprice = 0

    def sale(self):
        print "the item is" , self.status

    def addingtax(self):
        self.tax = 0.45
        self.newprice = (self.tax * self.price) + self.price
        print "after our tax of ", self.tax , "the new price is " , self.newprice

    def returning(self,reason):
        if reason == "returned damaged good":
            self.status = "defective"

        print self.status

        
       
        
        
# product1 = Product(234,"bag",3,"dior","sold")
# product1.sale()

# product2 = Product(56,"shoes",5,"puma",0.45)
# product2.addingtax()

product3 = Product(5609,"pant",5,"sic",0.56)
product3.returning("returned damaged good")


