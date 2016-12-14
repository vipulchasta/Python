class MyClass:
    def myIntrest( self , p , t , r = 10 ):
        self.intrest = p * t * r / 100
        #return self.interest
    def printIntrest( self ):
        print("Intrest Value is: ", self.intrest )

p = int( input("Enter Principal Amount: ") )
t = int ( input("Enter the Time: ") )

classVariable = MyClass()
classVariable.myIntrest(p,t)
classVariable.printIntrest()
