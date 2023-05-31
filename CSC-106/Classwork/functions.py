class functions:
    

    def overtime(hours, rate):
        if hours <= 40:
            total_wage = hours * float(rate) 
        else:
            hours_above = float(hours) - 40
            overtime_wage = float(rate*1.5) * hours_above
            total_wage = float(40*rate) + overtime_wage
        return(total_wage)

    print(overtime(50, 10))


    def even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    print(even(8))



    def leap_year(year):

        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True
        else:
            return False

    print(leap_year(2016)) 



    