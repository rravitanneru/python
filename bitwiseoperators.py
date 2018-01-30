
# bit wise operators perform actions on every bit by converting them into binary
# bit wise operators are
# 1.&(and),|(or),^ (Xor),<< bit wise left shfit,>> bitwise right shift,~ (not)

## bitwise and
a = 3                    # 3 in binary form  11
b = 2                    # 2 in binary form  10
c = a & b                #------------------------
print(c)                 #                   10  that is 2 in binary
 # bitwise or

d = a|b                  # 11
print(d)                 # 10
                         #-----
                         # 11
# bitwise XOR
e = a^b
print(e)

# bitwise leftshift
f = a<<1              # bitwsie leftshit shifts digits to leftside to right 11-->110(last an addtional bit 0 is addeed)
print(f)

# bitwise rightshift

g = a>>1 #    shifts digits to right side by one digit 11-->01 (0 is added instead of right shifted 
print(g)