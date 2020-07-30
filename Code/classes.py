import sys

c195 = list()
c197 = list()
both = dict()

def fillBoth(comm1, techReporting):
    for name in comm1:
        if name in techReporting:
            if name in both:
                continue
            else:
                try:
                    raise NotImplementedError('Name ')
                except Exception as e:
                    print(e.__class__.__name__, e)
def getName():
    name = ""
    try:
        raise NotImplementedError('Name ')
    except Exception as e:
        print(e.__class__.__name__, e)
    return name

def getNames(cName):
    done = False
    while done == False:
        name = getName()
        if cName in both.keys():
            continue
        else:
            both.update({cName,name})

def getCourse(cName):
    
    res = input('Would you like to add another class? (\'ClassName\', \'n\')')
    if res.lower() == 'done':
            done = True
        elif res.lower() == '195':
            getNames(res)
        elif res.lower() == '197':
            getNames(res)
        else : print('Invalid course selection! Please try again!')

def runProgram():
    done = False
    res = input('Would you like to add another class?  \n\t<course name> -or- done: ')
    while done == False:
        # SET Class
        course = getCourse()
        # GET Instructors for Class
        getNames(course)
        else : print('Invalid course selection! Please try again!')

runProgram()