#############################################################
#  Computer project 11
#
# Algortithm
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
            #check to see if the entered time is int         
        if type (hour)==int and type (minu)== int\
        and type(sec)==int and type(uct)==int:
            if 0<= hour<=23 and 0<= minu<=59 and \
            0<=sec<=59 and -12<=uct<=12:
                self.hour=hour
                self.minu=minu
                self.sec=sec
                self.uct=uct
            else:
                print("wrong time format")
                raise ValueError
        else:
            print("wrong time format")
            raise ValueError
               
    def __repr__(self):
        """the method returns an object which can be viewed in a shell"""
            #apply the formating style
        return  "{:02}:{:02}:{:02}{:+03}".format(self.hour, self.minu, self.sec,\
            self.uct)
                
    def __str__(self):
        """return a str object which is a printable representation of a
        Time object."""    
        return self.__repr__()
            
    def __add__(self, seconds):
        """the module lets the user do some arithmetics to the Time"""
        if type(seconds) != int:
            print("the object you are trying to add not an int")
            raise TypeError
            # get the total seconds and then find the modular and remainder
        total_sec=(self.hour * 3600 + self.minu* 60 + self.sec) + (seconds)
        final_hr = total_sec // 3600
            #if hour is 24, assign it to 0 for 24 hour system
        if final_hr==24:
            final_hr=0
            #if hour is less than 0, add 24 it to make it valid in 24hour system
        elif final_hr < 0:
            final_hr=24+ final_hr
        remaining_secs = total_sec % 3600
        final_min = remaining_secs // 60
        new_secs = remaining_secs % 60
        return "{:02}:{:02}:{:02}{:+03}".format(final_hr, final_min, new_secs, self.uct)
        
    def __sub__( self, other):
        """the module lets the user do some subtractions to the Time""" 
        if type(other) != Time:
            print("wrong time format")
            raise TypeError
            #find the difference in the UCT Time (other.uct and self.uct)
            #find the difference of the hours (self.hour and other.hour)
            #find the difference of the minute (self.minu and other.minu) 
            #convert the differences of each element to seconds
            #add the conversions togther
            #add the conversion to the difference of (self.sec-other.sec)
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
        return total_sec

    def from_str(self, time_str):
        """changes the value of the Time object to the UCT Time Format"""
            #check to see if the second parameter is Time object
        if len(time_str) != 11 or time_str [2] != ":" or time_str [5] != ":" \
         or time_str [8] not in  '+-':         
            print("wrong Time format")
            raise ValueError
        self.hour=int(time_str[0:2])
        self.minu=int(time_str[3:5])
        self.sec=int(time_str[6:8])
        self.uct=int(time_str[9:])
        if 0<= self.hour<=23 and 0<= self.minu<=59 and \
            0<=self.sec<=59 and -12<=self.uct<=12:        
            return "{:02}:{:02}:{:02}{:+03}".format(self.hour, self.minu, self.sec, self.uct)
        else:
            raise ValueError
        
    def get_as_local (self):
        """accepts an int object (the number of seconds from the start of a
        day) and changes the value of a Time object"""
            #set conditions when it is Am or PM or "Midnight" or "Noon"
        if 0 < self.hour <=11:
            return '"{:02}:{:02}:{:02} {}"'.format(self.hour, self.minu, self.sec,"AM")
        elif self.hour == 12:
            return '"Noon"'
        elif 12<self.hour<=23:
            hour=self.hour-12
            return '"{:02}:{:02}:{:02} {}"'.format(hour, self.minu, self.sec, "PM")
        elif self.hour == 0:
            return '"Midnight"'
        else:
            return "Wrong Time Entry"            

    def __gt__(self,other):
        """the module lets the user compare the variables to se which one is
        is greater. Returns a Boolean""" 
            #check to see if the second parameter is Time Object
        if type (other) != Time:
            print("wrong time format")
            raise TypeError 
            #find the difference in the UCT Time (other.uct and self.uct)
            #find the difference of the hours (self.hour and other.hour)
            #find the difference of the minute (self.minu and other.minu) 
            #convert the differences of each element to seconds
            #add the conversions togther
            #add the conversion to the difference of (self.sec-other.sec)
            #if the total_sec is greater than 0, then "first parameter" is greater
            
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
        if total_sec > 0:
            return True            
        else:
            return False    
    def __lt__(self,other):
        
        """the module lets the user compare the variables and see if
        one is less than the other, returns False if otherwise"""
        if type (other) != Time:
            print("wrong time format")
            raise TypeError 
            #find the difference in the UCT Time (other.uct and self.uct)
            #find the difference of the hours (self.hour and other.hour)
            #find the difference of the minute (self.minu and other.minu) 
            #convert the differences of each element to seconds
            #add the conversions togther
            #add the conversion to the difference of (self.sec-other.sec)
            #if the total_sec is less than 0, then "first parameter" is lesser              
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
        if total_sec < 0:
            return True
        else:
            return False
        
    def __eq__(self,other):
        """the module lets the user compare the variable and see if they
        are equal to each other, else, return False"""
        if type (other) != Time:
            print("wrong time format")
            raise TypeError
            #find the difference in the UCT Time (other.uct and self.uct)
            #find the difference of the hours (self.hour and other.hour)
            #find the difference of the minute (self.minu and other.minu) 
            #convert the differences of each element to seconds
            #add the conversions togther
            #add the conversion to the difference of (self.sec-other.sec)
            #if the total_sec is equal 0, then two parameters are equal
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
        if total_sec == 0:
            return True
        else:
            return False
            
    def __ne__(self, other):
        """the module lets the user compare the variable and see if they
        are not equal to each other, else, return False"""
        if type (other) != Time:
            print("wrong time format")
            raise TypeError         
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
            #if the total_sec is  not equal to 0, then two parameters arent equal
        if total_sec != 0:
            return True
        else:
            return False
            
    def __le__(self,other):
        """the module lets the user compare the variables and see
        if one is less than or eaqual to the other. Return False if wrong"""
        if type (other) != Time:
            print("wrong time format")
            raise TypeError
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
            #if the total_sec is "le" 0, then two parameters arent "le"
        if total_sec <= 0:
            return True
        else:
            return False
    def __ge__(self,other):
        """the module lets the user compare the variables and see
        if one is greater than or equal to the other, returns False if otherwise"""
        if type (other) != Time:
            print("wrong time format")
            raise TypeError        
        sec_in_local_hr=(other.uct - self.uct) * 3600
        sec_in_hr=(self.hour - other.hour) *3600
        sec_in_min =(self.minu - other.minu) *60
        secs=(self.sec - other.sec)  
        total_sec=sec_in_local_hr + sec_in_hr +sec_in_min + secs
        if total_sec >= 0:
            return True
        else:
            return False
        