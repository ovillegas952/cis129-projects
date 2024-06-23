"""
Author:Omar Villegas

Professor:Troy Adams

Date:6/19/2024

Course:CIS129

Description: This program uses a condition-controlled loop,counter controlled loop,
and accumulator for a grocery store to keep track of total number of bottles collected for seven days.
"""
#Lab 5 The Bottle Return Program

#Declared Variables
todayBottles = 0
totalBottles = 0
totalPayout = 0
counter = 1
keepGoing = 'y'

#Program Loop
while keepGoing == 'y':
    #getBottles code
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <= 7:
        todayBottles = input("Enter number of bottles returned for day #" + str(counter) + ": ")
        totalBottles = int(totalBottles) + int(todayBottles)
        counter += 1
    else:
    #calcPayout code
        PAYOUT_PER_BOTTLE = .10
        totalpayout = 0
        totalpayout = totalBottles * PAYOUT_PER_BOTTLE

    #printInfo code
    print("\nNumber of bottles for week:", totalBottles)
    print("The total paid out is $ %.1f" % totalpayout)
    
    #EndWhile Statement
    keepGoing = input("\nDo you want to enter another week's worth of data?\n(Enter y or n): ")
