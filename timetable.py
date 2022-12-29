from model import courses
import datetime
import time

timetable ={
    "Monday" :[courses.LA_LAB,courses.LA_LAB,courses.SPM,"lunch"],
    "Tuesday":[courses.DAA,courses.SPM,courses.AOS,"lunch",courses.DAA,courses.PLSQL_LAB,courses.PLSQL_LAB],
    "Wednesday":[courses.CAN,courses.AOS,courses.LA_LAB,courses.LA_LAB,courses,"lunch"],
    "Thursday":[courses.CAN,courses.AOS,courses.ADBMS,"lunch",courses.PLSQL_LAB,courses.PLSQL_LAB,courses.ADBMS,courses.CAN],
    "Friday":[courses.DAA,courses.DAA_LAB,courses.DAA_LAB,"lunch",courses.ADBMS,courses.DAA_LAB,courses.DAA_LAB]
}



x= datetime.datetime.now()
print(x.time())
mon=x.strftime("%A")

print(type(mon))
lis= timetable.get(""+mon)
#Tue_1_Theory
if(mon==timetable["Monday"]):
    print(timetable["Monday"][1])
elif(mon==timetable["Tuesday"]):
    print(timetable["Tuesday"][1])
elif(mon==timetable["Thursday"]):
    print(timetable["Thursday"][1])


def subject():


    month=x.strftime("%a")
    print(month)
   
