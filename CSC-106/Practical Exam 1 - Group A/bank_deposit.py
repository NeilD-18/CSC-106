#Neil Daterao

#Program that tells you the total amount of savings based on the quantity of coins inputed 


#Variables for the amounts of each type of coin

pennies = int(input("How many pennies (1 cent) do you have? "))
nickles = int(input("How many nickles (5 cents) do you have? "))
dimes = int(input("How many dimes (10 cents) do you have? "))
quarters = int(input("How many quarters (25 cents) do you have? ")) 

#Variable for total that adds the total amount of USD based on amount of coins inputed

total = (pennies*0.01) + (nickles*0.05) + (dimes*0.1) + (quarters*.25)


#Print out the total value of savings

print("The total value of your savings is $" + str(total) + ".") 
