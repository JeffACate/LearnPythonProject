import sys
import os

c195 = list()
c197 = list()
both = dict()

# import cls and clear
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    input('ClearThis')
    cls()
    name = input('Instructors Name: ')
    return name

def getNames(cName):
    done = False
    while done != True:
        getName()

def getCourse():
    try:
        raise NotImplementedError('getCourse(cName)')
    except Exception as e:
        print(e.__class__.__name__, e)

def runProgram():
    try:
        raise NotImplementedError('runProgram()')
    except Exception as e:
        print(e.__class__.__name__, e)

res = getName()
print(res)