def getBotUsername():...
inputFile = open('RedditAPIAccess.txt')
lines = []
for line in inputFile:
lines.append(line)
return line[2]
