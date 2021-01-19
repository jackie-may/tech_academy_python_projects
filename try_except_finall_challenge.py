x = 5

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("nothing went wrong")
finally:
    print("the try except challenge is over")
