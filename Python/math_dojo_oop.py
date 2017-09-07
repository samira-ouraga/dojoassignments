class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k                      
            else:
                self.result += i 
                 
        print self.result                
        return self

    def subtract(self,*args):
        self.result -=arg2
        print self.result
        return self

    def final_result(self):
        return self.result

md = MathDojo()
md.add(1,[1,1]).final_result()

