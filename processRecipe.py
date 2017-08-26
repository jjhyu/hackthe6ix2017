import json
FILENAME = 'recipe1.txt'
lines = []

with open(FILENAME, 'r') as text:
    for line in text:
        try:
            lines.append(line)
        except ValueError:
            print("Error, unread line")

for line in lines:
    print(line)
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


