class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def walking(self):
        self.health -= 1
        return self

    def running(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.name , "did some activities "
        print self.health , "is the new health after it"

# animal1 = Animal("sam",30)
# animal1.walking().display_health()

# animal2 = Animal("tito",30)
# animal2.running().display_health()

# animal3 = Animal("ruff",70)
# animal3.walking().walking().walking().running().running().display_health()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name,150)

    def pet(self):
        self.health -= 5
        return self

# dog1 = Dog("rex")
# dog1.walking().walking().walking().running().running().pet().display_health()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name,170)

    def fly(self):
        self.health -= 10
        print "this is the new health after flying "
        return self

    def display_health(self):
        print "This is a dragon"
        super(Dragon, self).display_health()
        return self

dragon1 = Dragon("pigeon")   
dragon1.display_health() 
