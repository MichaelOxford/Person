from Person import Person
import sys
import logic
import pickle

people = []
##outfile = open('dict.pickle','wb')
##pickle.dump(pickle, outFile)
##outFile.close()
choices = ['1', '2', '3']

def Main():
    '''Create test users and add them to the people list.'''
    #creates a test user and uses them for the people list
    Menu_text()
    Menu_logic()
    

    
def Menu_text():
    # Menu options defined here. 
    
    print("1 to add name, 2 to print name, 3 to exit")
    #prints options available
      

def Menu_logic():
    #Menu logic works here. 

    choose = input("What do you want to do?")
    while choose == '1' or choose == '2' or choose == '3':
        choose = input("What do you want to do?")
        #asks for input
        if choose == '3':
            input("press any key to exit")
            sys.exit()
            #if 3 pressed then it will exit
                     
        elif choose == '2':
            logic.print_people()
            #if 2 is pressed then it will show you the names entered
        elif choose == '1':
            logic.add_person()
            choose=0
            #if 1 choosen then you are able to add a person


    

if __name__ == '__main__':
    Main()



    


    

            
        
    
