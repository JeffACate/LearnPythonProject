import sys
import os

class InsturctorComparer:

    c195 = list()
    c197 = list()
    both = list()

    # import cls and clear
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    #SINGLE RESPONSIBILITY: gets a NAME for a specified COURSE
    def GetName(self,cName):
        name = input('Instructors Name for {0}: '.format(cName))
        return name

    #SINGLE RESPONSIBILITY: makes a LIST of instructors for a specific COURSE
    def GetNames(self,cName):
        done = False
        name = ''
        while done != True:
            # self.cls()
            if cName == 'c195':
                print(self.c195)
            else:
                print(self.c197)
            if name.lower() == 'done':
                done = True
            else:
                name = self.GetName(cName)
                if name != 'done':
                    if cName == 'c195':
                        if name not in self.c195:
                            self.c195.append(name)
                    elif cName == 'c197':
                        if name not in self.c197:
                            self.c197.append(name)
                else:
                    print('Invalid response. Try again.')

    def GetCourse(self):
        invalid = False
        while invalid != True:
            # self.cls()
            done = input('\n(0) exit\n(1) 195\n(2) 197\nWhat class would you like to select? ')
            if done == '0':
                invalid = True
            elif done == '1':
                self.GetNames('c195')
            elif done == '2':
                self.GetNames('c197')
            else:
                print('Invalid response. Try again.')
    
    def CompareCourses(self,course1,course2):
        newList = list()
        for instructor in course1:
            if instructor in course2:
                if instructor in newList:
                    continue
                else:
                    print(instructor)
                    newList.append(instructor)
        for instructor in course2:
            if instructor in course1:
                if instructor in newList:
                    continue
                else:
                    print(instructor)
                    newList.append(instructor)
        return newList

    def RunProgram(self):
        self.GetCourse()
        self.both = self.CompareCourses(self.c195,self.c197)
        return self.both

c = InsturctorComparer()
c.RunProgram()
print('\n195:',c.c195, '\n197:', c.c197,'\nboth:', c.both)