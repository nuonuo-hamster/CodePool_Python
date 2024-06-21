class user():

    def __init__(self, name):
        self.id = name
        self.resource = 1

    def dispatchResource(self):
        
        if (self.resource > 0):
            self.resource -= 1
            return 0
        else:
            print("not enough resource")
            return 1

    def relocateResource(self):

        self.resource += 1

class applies():

    def __init__(self, name):
        self.id = name
    
    def getResource(self):
        print("getResource!")

    def returnResource(self):
        pass

class user_nuonuo():

    def __init__(self):
        self.user = user("nuonuo")
        self.applies = applies("genshin")
    
    def launchApply(self):
        err = self.user.dispatchResource()
        if(not err): self.applies.getResource()

    def terminateApply(self):
        self.applies.returnResource()
        self.user.relocateResource()