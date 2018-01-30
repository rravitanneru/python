# there are two identical operators
# is, is not
# is by default evalutes to true if vars on both sides of operator pointing to same memory location, object,value
# is not by default evalutes to true if vars on both sides of operator pointing to same memory location, object,value
a =  10
b =  10
if(a is b):
    print('a is present in b')
p = 12
q = 11
if(p is not q):
     print('a is not in b')