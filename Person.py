from datetime import date
from datetime import datetime

class Person:
    #Defines a person

    def __init__(self, firstname, surname, DOB):
        #init assigns istance variable for later use#

        self.firstname = firstname
        self.surname = surname
        self.DOB = datetime.strptime(DOB, '%b %d %Y').date()
        self.age = self.calculate_age(self.DOB)
        # takes the details for for a person

    def calculate_age(self, born):
        #Calculates age from DOB

        today = date.today()
        years_difference = today.year - born.year
        is_before_birthday = (today.month, today.day) < (born.month, born.day) 
        elapsed_years = years_difference - int(is_before_birthday)
        return elapsed_years
    # works out age from date of birth and todays date
    
7
