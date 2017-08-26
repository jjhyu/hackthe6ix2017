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

# class step():
#     def __init__(self, givenTime, text):
#         self.givenTime = givenTime
#         self.text = text
#
#     def isTimed(self):
#         return self.givenTime == -1
processed_steps = []
stepNumber = 1
for line in raw_steps:
    step = {}
    step["stepNumber"] = stepNumber
    stepNumber = stepNumber + 1
    step["text"] = line
    words = line.split(' ')
    step["isTimed"] = ("minutes" in words)
    if "minutes" in words:
        minutesIndex = words.index("minutes")
        lengthMinutes = int(words[minutesIndex - 1])
        step["lengthMins"] = lengthMinutes
    else:
        step["lengthMins"] = ""

    processed_steps.append(step)



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


