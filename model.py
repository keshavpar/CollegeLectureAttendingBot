import enum;
import datetime
class courses(enum.Enum):
    AIP='ADVANCED INTERNET PROGRAMMING'
    AIP_LAB='ADVANCED INTERNET PROGRAMMING LAB'
    AP='APTITUDE-1'
    CP='COMPUTING APTITUDE'
    PP='PYTHON PROGRAMMING'
    SK='SOFT SKILLS -1'


x = datetime.datetime.now()
month=x.strftime("%a")
print(month)    
