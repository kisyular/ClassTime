#############################################################
#  Computer project 10
#
#  Algortithm
# Initiate a class Time
# Define the __str__ method and return the "string" statement
# Define the __repr__ method and return the "string" statement
# Define the __add__ method and return self
# Define the __sub__ method and return 0
# Define the from_uct method and pass
# Define the from_sec method and pass
# Define the __lt__ method and return False
# Define the __gt__ method and return False
# Define the __eg__ method and return False
# Define the __le__ method and return False
# Define the __ge__ method and return False
# Define the __eq__ method and return False
# Define the __ne__ method and return False
##################################################################

class Time (object):
    def __init__ (self, hour=0, minu=0, sec=0, uct=0):
        """
        Method __init__ initializes a Time object."""        
        pass    
    def __str__(self):
        """return a str object which is a printable representation of a
        Time object."""     
        return "time string"
        
    def __repr__(self):
        """the method returns an object which can be viewed in a shell"""
        return "time string"
    
    def __add__(self, seconds):
        """the module lets the user do some arithmetics to the Time""" 
        return self
    
    def __sub__( self, other ):
        """the module lets the user do some subtractions to the Time""" 
        return 0
    def from_utc(self, time_add_str):
        """changes the value of the Time object to the UCT Time Format"""
        pass
    
    def from_seconds (self, addObj):
        """accepts an int object (the number of seconds from the start of a
        day) and changes the value of a Time object"""
        pass
    def __gt__(self,otherObj):
        """the module lets the user compare the variables to se which one is
        is greater. Returns a Boolean""" 
        return False
    
    def __lt__(self,otherObj):
        """the module lets the user compare the variables and see if
        one is less than the other, returns False if otherwise""" 
        return False
        
    def __eq__(self,otherObj):
        """the module lets the user compare the variable and see if they
        are equal to each other, else, return False""" 
        return False
    def __ne__(self, otherObj):
        """the module lets the user compare the variable and see if they
        are not equal to each other, else, return False""" 
        return False
            
    def __le__(self,otherObj):
        """the module lets the user compare the variables and see
        if one is less than or eaqual to the other. Return False if wrong""" 
        return False
        
    def __ge__(self,otherObj):
        """the module lets the user compare the variables and see
        if one is greater than or equal to the other, returns False if otherwise""" 
        return False
        