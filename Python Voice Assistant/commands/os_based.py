import os

#Date
from time import localtime
def Date():
    theTime = localtime()
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthDay = theTime[2]
    if monthDay == 1:
        date = "first"
    elif monthDay == 2:
        date = "second"
    elif monthDay == 3:
        date = "third"
    else:
        if monthDay > 20:
            if str(monthDay)[-1] == "1":
                date = str(round(monthDay, -1)) + " first"
            elif str(monthDay)[-1] == "2":
                date = str(round(monthDay, -1)) + " second"
            elif str(monthDay)[-1] == "3":
                date = str(round(monthDay, -1)) + " third"
            else:
                date = str(monthDay) + "th"
        else:
            date = str(monthDay) + "th"
    return("Today is, " + day_list[theTime[6]] + ", the " + date + " of " + month_list[theTime[1] - 1])

#Time
def Time():
    theTime = localtime()
    if theTime[3] > 12:
        hour = str(theTime[3] - 12)
    else:
        hour = str(theTime[3])
    minute = theTime[4]
    if minute > 30:
        hour = str(int(hour) + 1)
        if minute == 45:
            arguments = "quarter to " + hour
        else:
            arguments = str(60 - minute) + " minutes to " + hour
    else:
        if minute == 0:
            arguments = hour + " o'clock"
        elif minute == 15:
            arguments = "quarter past " + hour
        elif minute == 30:
            arguments = "half past " + hour
        else:
            arguments = str(minute) + " minutes past " + hour
    return("The time is " + arguments)

#Take a screenshot
from PIL import Image
import pyautogui
def Screenshot():
    year = str(localtime().tm_year)
    month = str(localtime().tm_mon)
    day = str(localtime().tm_mday)
    hour = str(localtime().tm_hour)
    minute = str(localtime().tm_min)
    second = str(localtime().tm_sec)
    Date = "{}{}{}{}{}{}.png".format(year, month, day, hour, minute, second)
    User = os.getlogin()
    SavePath = r"C:\Users\{}\Pictures".format(User)
    pyautogui.screenshot(os.path.join(SavePath, Date))
    im = Image.open(os.path.join(SavePath, Date))
    im.show()
