# creating the lists
# lists are similar to arrays but can contain different datatypes

ravi = ['mango','apple','orange']
print(ravi)

# upadating items to the list

ravi[2] =  'grapes'
print(ravi)

# adding two lists

ravi2 = ['samsung','apple','nokia']
print (ravi2)
print(ravi+ravi2)
ravi3 = ravi+ravi2
print(ravi3)
# printint part of the list
print(ravi3[0:4])
# printintg the list multipe times
print(ravi3[0:2]*2)

# printing the list length

print(len(ravi3))