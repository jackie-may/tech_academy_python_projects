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






def start():                            # start() contains the variables
    f_name = "Sarah"                    # use names that describe what the variable is
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)
    

def get_info(f_name,l_name,age,gender):
    print("My name is {0} {1}. I am a {2} year old {3}.".format(f_name,l_name,age,gender))




if __name__ == "__main__":
    start()
