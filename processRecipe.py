import json
import sys

FILENAME = sys.argv[1]
lines = []
bareFILENAME = FILENAME.split(".")[0]
with open(FILENAME, 'r') as text:
    for line in text:
        try:
            lines.append(line)
        except ValueError:
            print("Error, unread line")

title = lines[0]
raw_steps = lines[1:]

processed_steps = []

minute_types = {"minutes", "mins", "m", "minute", "min", "minutes\n", "mins\n", "m\n", "minute\n", "min\n"}
hour_types = {"hour", "hours", "hr", "h", "hrs","hour\n", "hours\n", "hr\n", "h\n", "hrs\n", }
second_types = {"second", "seconds", "s", "sec", "second\n", "seconds\n", "s\n", "sec\n"}

stepNumber = 1
for line in raw_steps:
    step = {}
    step["stepNumber"] = stepNumber
    stepNumber = stepNumber + 1
    step["text"] = line
    words = line.split(' ')
    isTimed = False
    minute_type = ""
    hour_type = ""
    second_type = ""
    for word in words:
        if word in minute_types:
            minute_type = word
        elif word in hour_types:
            hour_type = word
        elif word in second_types:
            second_type = word
        if word in minute_types or word in hour_types or word in second_types:
            isTimed = True
            break

    if not minute_type == "":
        timeIndex = words.index(minute_type)
        length = int(words[timeIndex - 1])
        step["lengthMins"] = length
    else:
        step["lengthMins"] = ""

    if not hour_type == "":
        timeIndex = words.index(hour_type)
        length = int(words[timeIndex - 1])
        step["lengthHours"] = length
    else:
        step["lengthHours"] = ""

    if not second_type == "":
        timeIndex = words.index(second_type)
        length = int(words[timeIndex - 1])
        step["lengthSecs"] = length
    else:
        step["lengthSecs"] = ""

    processed_steps.append(step)

with open(bareFILENAME + '.json', 'w+') as outfile:
    json_title = json.dump({"title":title}, outfile)
    for data in processed_steps:
        json.dump(data,outfile)
        outfile.write(",\n")