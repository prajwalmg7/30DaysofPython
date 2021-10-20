# Day 00 (LCO)

# There is a lecturer in a small town who loves coding and he wants to 
# create a program which prints out the whole multiplication table of 
# an entered number for his students. Can you help him to write a program 
# in python.

n= int(input("enter the number "))

for i in range (1,11):
    j=i*n
    print (i,'*',n,'=',j)


