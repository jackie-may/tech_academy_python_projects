#template:
#PYTHON:     3.9.1
#
#AUTHOR:     Jackie May
#
#PURPOSE:    The Tech Academy - Python Course, Creating our first program
#            together.Demonstrating how to pass variables from function
#            to function while producing a functional game.
#
#            Remember, function_name(variable) _means that we pass in
#            the variable. Return variable _means that we are returning
#            the variable back to the calling function.




def start(nice=0,mean=0,name=""):                   #nice & mean receive numeric value,
                                                    #name receives an empty string value
                                                    #going to receive this information
                                                    #throughout the game and store them
                                                    #in the variables
                                                    #most importantly can control what
                                                    #the default values are
    #get user's name                             
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)




def describe_game(name):
    """
        check if this is a new gameor not.
        if it isnew, get the user's name.
        if it is not a new game, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    #if the user plays again, they will receive this message
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        #stop asking for their name
        stop = True 
        while stop:
            if name == "":
                #going to capitalize the information we get from the user here (a raw string from the input)
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome,{}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou cna choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    #returning the users name to the 'get user's name above' so that we can address them by their name from now on
    return name




def nice_mean(nice,mean,name):
    stop = True
    #while stop is true do the following loop
    while stop:
        show_score(nice,mean,name)
        #new variable 'pick'
        #user will respond n or m
        #'\n>>>' new line for user to enter info
        #.lower so it doesn't matter if user uses upper or lower case
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            #either way if they are nice or mean we will stop asking
            stop = False 
    score(nice,mean,name) #pass the 3 variables to the score()




def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))




def score(nice,mean,name):
    #score function is being passed the values stroed within the 3 variables
    if nice > 2:    #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean> 2:     #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:           #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)




#nice and mean score plus the user's name
def win(nice,mean,name):
    #substitute the {} wildcards with out variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \n made lots of friends along the way!".format(name))
    #call again function and pass in our variables
    #asking if they want to play again
    again(nice,mean,name)




def lose(nice,mean,name):
    #substitutes the {} wildcards with our variable values
    print("\nAHHH too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)




def again(nice,mean,name):
    stop = True
    while stop:
        #storing whatever value the user gives us in 'choice'
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower() 
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            #will come up on the screen in development mode asking if we want to close python
            #if we were in an executable, this would close the program
            quit()
        #this is for if they didn't answer the question at all or correctly
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")




def reset(nice,mean,name):
    #resetting nice and mean variables
    nice = 0
    mean = 0
    #we do not reset the 'name' variable as that same user has elected to play again
    #call 'start' the original function that we started with
    #this will overwrite the empty string variable and replace it with the known users name
    start(nice,mean,name)











        






if __name__ == "__main__":
    start()#this means we are going to fire the start() function to run the program
