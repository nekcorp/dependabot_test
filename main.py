class cMrRobot :
    """
    Class to display name of Mr Robot
    """
    
    def __init__(self,myName):
        self.myName = myName
    
   
    def DisplayMyName(self):
        print(self.myName)



if __name__ == "__main__":
    myRobot = cMrRobot("Sam Sepiol")
    myRobot.DisplayMyName()
