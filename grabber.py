import json
from datetime import datetime         #our dependencies
from pytz import timezone
from calendar import day_name
import os

cursedLessons = ("Germana", "Informatica", "Engleza")

def get_all():

    Moldova = timezone("Europe/Chisinau")


    now = datetime.now(Moldova).strftime("%H:%M")     # we find the time and transform it to a H:M format
    today = datetime.now(Moldova)
    today = day_name[today.weekday()] 
    #today = "Friday"
    #now = datetime.strptime("09:30", "%H:%M").strftime("%H:%M")

    currentLesson = ""
    nextLesson = ""

    currentLessonName = ""
    nextLessonName = ""                         #varibles

    currentLessonLink = ""
    nextLessonLink = ""



    with open("time.json") as json_file:        #with is used so that the file is closed after is has been used
        data = json.load(json_file)             # we load the json into the data variable as a dict
        for i in data:                          #loop through the elements


            lesson = data[i]                    #lesson will be equal to "lesson1, lesson2.."

            #we take the string(ex: "13:25") from the the objects start_time and finish-time that are a part of the lesson dict(ex: "lesson3") and turn it into a time object of the format H:M
            start = datetime.strptime(lesson["start-time"], "%H:%M").strftime("%H:%M")
            finish = datetime.strptime(lesson["finish-time"], "%H:%M").strftime("%H:%M")

            if now < start:
                nextLesson = data[i]["order-nr"]
                currentLesson = 0
                break
            elif start <= now and finish >= now:
                currentLesson = data[i]["order-nr"]
                if data[i]["order-nr"] <= 6:
                    nextLesson = data[i]["order-nr"] + 1
                else:
                    nextLesson = 0
                break
            else:
                currentLesson = 0
                nextLesson = 0


    
    with open("lessons.json") as json_file: 
        data = json.load(json_file)
        try:
            if currentLesson != 0:
                currentLessonName = data[today][f"lesson{currentLesson}"]["object"]
            elif currentLesson == 0:
                    currentLessonName = "Free Time"
        except:
            currentLessonName = "Free Time"
        try:
            if nextLesson != 0:
                nextLessonName = data[today][f"lesson{nextLesson}"]["object"]
            elif nextLesson == 0:
                nextLessonName = "Free Time"
        except:
            nextLessonName = "Free Time"


    try:
        if currentLessonName in cursedLessons:
            currentLessonLink = (f"<{os.getenv(currentLessonName + '1')}>", f"<{os.getenv(currentLessonName + '2')}>")
        elif currentLesson != 0:
            currentLessonLink = f"<{os.getenv(currentLessonName)}>"
        else:
            currentLessonLink = "There is no limk for now, be back later :)"
        if currentLessonLink == "<None>":
            currentLessonLink = "There seems to be no link for this lesson. Check studii.md or viber group"
    except:
        currentLessonLink = "There is no limk for now, be back later :)"
    try:
        if nextLessonName in cursedLessons:
            nextLessonLink = (f"<{os.getenv(nextLessonName + '1')}>", f"<{os.getenv(nextLessonName + '2')}>")
        elif nextLesson != 0:
            nextLessonLink = f"<{os.getenv(nextLessonName)}>"
        else:
            nextLessonLink = "There is no limk for now, be back later :)"
        if nextLessonLink == "<None>":
            nextLessonLink = "There seems to be no link for this lesson. Check studii.md or viber group"    
    except:
        nextLessonLink = "There is no limk for now, be back later :)"



    #print(currentLesson)
    #print(currentLessonName)
    #print(currentLessonLink)
    #print(nextLesson)    
    #print(nextLessonName)
    #print(nextLessonLink)

    return currentLessonName, currentLessonLink, nextLessonName, nextLessonLink,

       
    




