import schedule
import main
import timetable

schedule.every().day.at("22.38").do(main.py)
schedule.every().day.at("10.30").do(main.py)
schedule.every().day.at("11.20").do(main.py)
schedule.every().day.at("13.00").do(main.py)

