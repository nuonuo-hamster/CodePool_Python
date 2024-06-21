from initial import*

def changeData(user):
    
    user.id = "nuonuo_01"

if __name__ == '__main__':

    nuonuo = user_nuonuo()
    
    changeData(nuonuo.user)
    nuonuo.launchApply()
    nuonuo.terminateApply()
    nuonuo.launchApply()
    nuonuo.launchApply()
    nuonuo.terminateApply()
    nuonuo.launchApply()
    print(nuonuo.user.id)
    print(nuonuo.applies.id)