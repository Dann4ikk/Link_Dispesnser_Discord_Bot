import json
from datetime import datetime, timedelta         #our dependencies
from calendar import day_name
from pytz import timezone

Moldova = timezone("Europe/Chisinau")
def getOrar(day = None):
    orar = []
    today = day_name[datetime.now(Moldova).weekday()]
    if day:
        if day == "tomorrow":
            today = datetime.now(Moldova) + timedelta(days=1)
            today = day_name[today.weekday()]

    with open("lessons.json") as json_file: 
        timedata = json.load(open("time.json"))
        data = json.load(json_file)
        try:
            for i in data[today]:
                lectie = []
                lesson_name = data[today][i]["object"]
                start_time = timedata[i]["start-time"]
                finish_time = timedata[i]["finish-time"]
                lectie.append(lesson_name)
                lectie.append(start_time)
                lectie.append(finish_time)
                orar.append(lectie)
        except:
            pass

    return orar
        

