from datetime import datetime
import webbrowser
import time

class Alarm:
    __alarmTime = None
    __youtubeLink = None

    def __init__(self,time,link):
        self.__alarmTime = time
        self.__youtubeLink = link
        print("Alarm Set")
        self.__announce_time()

    def __calculate_difference(self):
        now = datetime.now()
        currentTime = str(now.hour) + ":" + str(now.minute)
        FMT = '%H:%M'
        tdelta = datetime.strptime(self.__alarmTime, FMT) - datetime.strptime(currentTime, FMT)
        timeArray = str(tdelta).split(':')
        return {'hour': timeArray[0], 'minute': timeArray[1]}

    def __announce_time(self):
        left = self.__calculate_difference()
        print("Time Left To Wake Up:", left['hour'], "Hour", left['minute'], "Minute")
        self.__countdown()

    def __countdown(self):
        while True:
            left = self.__calculate_difference()
            if (left['hour'] == "0") and (left['minute'] == "00"):
                break
            else:
                time.sleep(60)
                self.__announce_time()
        self.__trigger_alarm()
        exit()

    def __trigger_alarm(self):
        webbrowser.open(self.__youtubeLink,new=0,autoraise=True)