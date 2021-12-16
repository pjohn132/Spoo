class Print:
    def __init__(self):
        # Create $$$ rectangle
        self.x = int (input("ENTER NO. OF VERTICAL COLUMNS:"))
        self.y = int (input("ENTER NO. OF HORIZONTAL ROWS:"))
        print("$"*self.x)                                   # $$$$$
        for i in range(0,self.y-2):                         # $   $ 
            print("$"*1," "*(self.x-4),"$"*1)               # $   $
        if self.y!=1:                                       # $$$$$
            print("$"*self.x)
        joke = 1
        # Duplicate $$$ rectangle
        self.z = int (input("ENTER NO. OF DUPLICATES:"))
        while self.z <= 1:
            self.z = int (input("ENTER NO. OF DUPLICATES:"))
            if joke == 5:
                print("PLLLEAAASEEE")
            if joke == 7:
                print("this is a friendly reminder. DO THE $$$$$ING THING...")
            if joke == 9:
                print("...Plea$e?")
            if joke == 13:
                print("FINE! Here's your credit sequence: ENTER NO. OF ( you know what to do ;) ) ")
            if joke == 16:
                print("uhhhh")
            if joke == 17:
                print("hhhhhhhhhhhhhhhhhhhhhh")
            if joke == 18:
                print("h")
            if joke == 19:
                print("a")
            if joke == 20:
                print("h")
            if joke == 21:
                print("a")
            if joke==22:
                print("h")
            if joke==23:
                print("a")
            if joke ==24:
                print("h")
            if joke ==25:
                print("a")
            if joke ==26:
                print("h")
            if joke ==27:
                print("h")
            if joke==28:
                print("h")
            if joke==29:
                print("h") 
            if joke == 30:
                print("Y"," ","O"," ","U"," "*5,"A"," ","R"," ","E"," "*5,"D"," ","E"," ","A"," ","D")
                break   
            joke = joke + 1
            
            if self.z > 1:
                break
        if self.z > 1:
            for i in range(0,self.z): 
                if i == 0:
                    print(" "*3,end="")                          # $$$$$ $$$$$ $$$$$ $$$$$
                print("$"*self.x," "*1,end="")                   # $   $ $   $ $   $ $   $
                if i == self.z - 1:                              # $   $ $   $ $   $ $   $
                    print(" ")                                   # $   $ $   $ $   $ $   $ 
            for i in range(0,self.y-2):                          # $$$$$ $$$$$ $$$$$ $$$$$
                if i <=self.y-2:
                    print(" "*3,end="")                           
                for i in range(0,self.z):                              
                    print("$"*1," "*(self.x-4),"$"*1," ",end="") 
                    if i == self.z - 1:
                        print(" ")
            if self.y!=1:            
                for i in range(0,self.z):
                    if i == 0:
                        print("SP","",end="")
                    print("$"*self.x," ",end="")
                    if i == self.z-1:
                        print("KY")
        print(" ")
        if joke < 10:
            print("")
        if joke > 10:
            print("addddd up those zeros, turkey:  0+0+0+000000000 >>>>>>>>>>>wow>>>>>>>>>>>>>>>>>>suchgreater>>>>>>>>>>>>> than your brain cells. edit: :) ")
            

        
            
        
class Rectangle(Print):
    def __init__(self):
        super().__init__()
        
                         
    
            
d = Print()

