

def getInfo(): #use this to get information from the our user
    var1 = input("\nPlease provide the first numeric value: ")
    #to get information you have to use 'input'
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2 #instead of calling the function it is going to return these variables and return it back to where we called it
    


#TRY AND EXCEPT BLOCK
def compute(): #compute calls 'getInfo' and gets it's information this way
    go = True # while go = true everthing under 'while' will continue to loop
    while go: # the while is calling the getInfo function
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2) #converts to an integer / numeric value
            """we are asking for an input
            and even if the user inputs a number
            python recognizes it as a string
            and this converts it to an integer"""
            go = False
        except ValueError as e:
            """ this is what happens if an error is produced
            by the above code and it is a value error (wrong value type)
            adding the 'as e' includes the computers error message in the output"""
            print("{}: \n\nYou did not provide a numeric value!".format(e)) #{}: is a wildcard
        except: #all other errors
            print("\n\nOops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3)) #once the while loop is resolved we print out to the users screen


if __name__ == "__main__":
    compute() #this is what will actually be 'run'
