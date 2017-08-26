import json
import string
FILENAME = 'recipe1.txt'
lines = []

with open(FILENAME, 'r') as text:
    for line in text:
        try:
            lines.append(line)
        except ValueError:
            print("Error, unread line")

title = lines[0]
raw_steps = lines[1:]

processed_steps = []

minute_types = {"minutes", "mins", "m", "minute", "min"}
hour_types = {"hour", "hours", "hr", "h", "hrs"}
second_types = {"second", "seconds", "s", "sec"}

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

with open('recipe1.json', 'w+') as outfile:
    for data in processed_steps:
        json.dump(data,outfile)
        outfile.write(",\n")




# with open(FILENAME, 'r') as text:
#     for line in text:
#         try:
#             parsed_line = json.loads(line)
#             if "key" in parsed_line and parsed_line["key"] is not None and \
#                 parsed_line["key"] == parsed_line["key"][::-1]:
#                 words.append(parsed_line["key"])
#                 count += 1
#         except ValueError:
#             debug_print("Line is not json formatted")


