from person2 import Person #from person2 imports details of person
import pickle


def print_people():
    '''Iterates through the people list and prints out details'''

    for person in people:
        print('{0} {1} is {2} years old'.format(person.firstname,person.surname,person.age))# displays options
              

        
def add_person():
    '''creates a new user''' # creates 'a new user
    
    Firstname = input("what is your firstname") #asks firstname and stores input in p1
    Lastname = input("what is your lastname") #asks lastname and stores input in p1
    DOB = input("what is your date of birth") # asks date of birth and stores in p1
    p1 = Person(Firstname, Lastname , DOB ) 
    people.append(p1) # creates a new person


def save(file, date):
    '''pickles file'''
    
    with open(file, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCAL)


def load(file):
    '''un-pickle'''
    try:
        with open(file, 'rb') as f:
            people = pickle.load(f)
    except FileNotFoundError:
        print('No File Found')
        people = []
    return people
 


 

