class student:

    def __init__(self,first,last,marks):
         self.first = first
         self.last = last
         self.marks = marks
         self.email = first + '.' + last + '@omniwyse.com'
    def fullname (self):
        return '{} {}'.format(self.first, self.last)

#ravi = student('ravi','kumar',75)
#print(ravi.marks)
#print(ravi.email)
#print(ravi.fullname())
kumar = student('kumar','ravi',90)
print(kumar.marks)
print(kumar.fullname())

# inheritenace
class st1(student):
    def __init__(self,first,last,marks,pro_lan): # we are using inheritance and adding a extra parameter to method which is present in super class
        super().__init__(first,last,marks)
        self.pro_lan = pro_lan

ravi = st1('ravi','kumar',75,'python')
print(ravi.pro_lan)
print(ravi.first)