
#class utilizing encapsulation
class Protected:
    def __init__(self):
        #private variable
        self.__privateVar = 45
        #protected variable
        self._protectVar = 10

    #private function
    def getPrivate(self):
        print(self.__privateVar)

    #private function
    def setPrivate(self, private):
        #changing the private variable value to 'private'
        self.__privateVar = private

    #protected function
    def getProtect(self):
        print(self._protectVar)
        
#instantiating objects
obj = Protected()
obj.getPrivate()
obj.setPrivate(93)
obj.getPrivate()
obj.getProtect()
