principal = float(input("enter the principal amount:")) # take input of principal from user.
rate = float(input("enter the rate of interest:")) # take input of rate from user.
time = float(input("enter the time in a year:"))  # take input of time from user.

simple_interest = float((principal*rate*time)/100) # for calculating the simple interest.

print("The simple interest is:", simple_interest)  # printing the simple interest as a output
