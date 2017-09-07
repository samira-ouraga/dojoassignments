class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, arg1,*args):
        for i in args:
            for j in i:
                self.result += arg1 + j
        print self.result
        return self

    def subtract(self,arg2):
        self.result -=arg2
        print self.result
        return self

    def final_result(self):
        return self.result

md = MathDojo()
md.add(1,[1]).final_result()

