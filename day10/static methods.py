#static method
#there are two variables in class (class variable / instance variable )





class car(ABC):
    def moveforward(self):
        pass
    def movebackward(self):
        pass
    def fm(self):
        pass


class swift(car):
    @staticmethod             #we can call moveforward method without creating a object using the decorator@staticmethod
    
    def moveforward(self):
        print("swift")
    def movebackward(self):
        print("swift1")
        
    def fm(self):
        print("swift3")



class inova(car):
    def moveforward(self):
        print('inovo')
    def movebackward(self):
        print('inovo1')
    def fm(self):
        print('inovo2')
