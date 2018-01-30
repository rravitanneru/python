# loops are used a execute a block a code for number of times
# while loop is used when we dont know how many times we have to execute
# for loop is for if we know how many times to execute

# nested loop means loop in loop
# now writing a program to print prime numbers
i = 2
while(i<=100):
    j =2
    while( j <= (i/j) ):
      if not (i%j): break
      j= j+1
    if (j > (i/j)): print(i,'is prime')

    i = i+1

