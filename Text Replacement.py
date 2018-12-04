marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."
m = line.find(marker)
replaced = line[0:m] + replacement + line[m+len(marker):]

print replaced
