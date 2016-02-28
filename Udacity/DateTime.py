import datetime

today = datetime.datetime.today()

print "Today's date is:", str(today)
print "As a full date and timestamp"

print "Today's date is {:%m-%d-%y}".format(today)
print "As a month, day and 2 digit year layout"

print "Today's date is {:%Y-%m-%d}".format(today)
print "As a 4 digit year, month, then day layout, hyphen seperated, 10 char spaces"
