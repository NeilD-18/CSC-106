#Neil Daterao

#Fizz Buzz Program

#Function to determine if the program will output fizz, buzz, fizzbuzz or the number 
def fizz_buzz(num):

    #first, check if the number is divisible by 3 AND 5, if not, check if divisible by 3 or 5 individually. If none, return the number as a string 
    if (num % 3 == 0) and (num % 5 == 0):
        return str("fizzbuzz")
    elif (num % 3 == 0):
        return str("fizz")
    elif (num % 5 == 0):
        return str("buzz")
    else:
        return str(num) 
        
    
    



### DO NOT DELETE THIS LINE: beg testing

# some test cases
print(9, "==>", fizz_buzz(9))  #fizz
print(5, "==>", fizz_buzz(5))  #buzz
print(11, "==>", fizz_buzz(11)) #11
print(30, "==>", fizz_buzz(30)) #fizzbuzz 
