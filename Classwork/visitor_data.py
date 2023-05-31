##Lucy Mastrianni and Neil Daterao 
## 
##Harwall University Form 



def form():
    """ The form function that collects info from users

    Returns:
    - A string that says whether the form succeeded or not
    """
    # Collect the user's street number
    street_num = input("Enter the street number of your address: ")
    street_num = test_street_num(street_num)
    if street_num == False:
        return "Form failed: Restart the form!"

    # Collect the user's age
    age = input("Enter your age: ")
    age = test_age(age) # Finish this function below!
    if age == False:
        return 


    email = input("Enter your email: " )
    email = test_email(email)
    if email == False:
        return "Form failed: Restart the form!"

    rov = input("Reason for visit?\n 1. Alumni\n 2. Perspective Student\n 3. Family of Perspective Student\n 4. Visiting Family/Friends\n 5. Job Opportunities\n 6. Other\n")
    rov = test_rov(rov)
    if rov == False:
        return "Form failed: Restart the form!"
    


    # Then, print out all our collected info in a form
    print("=====================")
    print("We've collected the following information:")
    print("- Street Number:", street_num)
    print("- Age:", age)
    print("- Email:", email)
    print("- Reason for Vist:", rov)
    print("=====================")

    return "Form complete!"


def test_street_num(street_num):
    """ EXAMPLE: Gets the user's street number.

    Arguments: 
    - street_num - the street number of the user 
    Returns: 
    - False if the input is incorrect
    - the integer street number if it is correct
    """
    # Check to see if it's empty!
    if street_num.strip() == "":
        print("SORRY! You forgot to enter your number!\n")
        return False
    # Check to see if it's a number!
    elif street_num.isdigit() == False:
        print("SORRY! Your number should be a positive number\n")
        return False
    else:
        return street_num

def test_age(age):
    """ Gets the user's age
    COMPLETE THIS FUNCTION
    """
    
    if age.strip() == "":
        print("SORRY! You forgot to enter your age!\n")
        return False

    elif age.isdigit() == False:
        print("SORRY! Your age should be a positive number\n")
        return False

    elif int(age) < 12 or int(age) > 122:
        print("SORRY! This is not a valid age\n")
        return False 

    else:
        return age

def test_email(email):

    #Various Test Cases 
    if "@" in email == False:
        print("SORRY! Not a valid email address!\n")
        return False
        
        
    
    
    elif (email.endswith(".com") == False) and (email.endswith(".org") == False) and (email.endswith(".net") == False) and (email.endswith(".edu") == False):  
        print("SORRY! Not a valid email address!\n")
        return False 

    else:
        return email


def test_rov(rov):

    #Various Test Cases
    if (rov.isdigit() == False):
        print("Sorry! Not a valid choice! \n")
        return False 

    elif (int(rov) < 1 or int(rov) > 6):
        print("Sorry! Not a valid choice! \n")
        return False

    elif (int(rov) == 1):
        rov = "Alumni"
        return rov

    elif (int(rov) == 2):
        rov = "Perspective Student"
        return rov

    elif (int(rov) == 3):
        rov = "Family of Perspective Student"
        return rov

    elif (int(rov) == 4):
        rov = "Visiting Family/Friends"
        return rov

    elif (int(rov) == 5):
        rov = "Job Opportunities"
        return rov

    elif (int(rov) == 6):
        rov = "Other"
        return rov


    
        
                                                                                                    

       
      



# Runs the main program
print( form() )
