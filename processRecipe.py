import json
import sys

# try:
#     FILENAME = sys.argv[1]
# except IndexError:
#     sys.exit()

def processRecipe(FILENAME):
    lines = []
    with open(FILENAME, 'r') as text:
        for line in text:
            try:
                lines.append(line)
            except ValueError:
                print("Error, unread line")

    title = lines[0]
    breakIndex = lines.index('\n')
    raw_steps = lines[(1+breakIndex):]
    finalDictionary = {"title" : title}
    processed_steps = {}
    minute_types = {"minutes", "mins", "m", "minute", "min", "minutes\n", "mins\n", "m\n", "minute\n", "min\n"}
    hour_types = {"hour", "hours", "hr", "h", "hrs","hour\n", "hours\n", "hr\n", "h\n", "hrs\n", "hours.\n"}
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

        processed_steps.update(step)

    finalDictionary.update({"steps":processed_steps})
    return json.dumps(finalDictionary)

if __name__ == "__main__":
    print(processRecipe("testing_examples/recipe1.txt"))