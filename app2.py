


import app


def print_app2(): #declaring a function
    name = (__name__) #calling outside of this function to the function in app.py
    return name


if __name__ == "__main__":
    """ saying if this script is being ran do the following code underneath
    otherwise don't do anything on this page
    this is how you control the program flow"""
    #the following is calling code from within this script
    print("I am running code from {}".format(print_app2()))
    """ calling on a special built in function called format
    and the period means it's happening to this string
    it is a helper method to the string
    and formats or 'plugs in' information into where the {} are"""
    """ must have () to call a function """

    #the following is calling code from the imported app.py
    print("I am running code from {}".format(app.print_app()))
    """ can't access the app until you add 'app.' in the front
    so it knows to go to the app.py file and call on the function in that file 'print_app()' """
    """ 'app.' calls on the module
    'print_app()' calls on the modules method """
