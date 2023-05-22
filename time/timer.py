import time
from datetime import datetime
import datetime
import argparse
import re

parser = argparse.ArgumentParser(description='Python Countdown Timer')
parser.add_argument('-t', '--time', help='Countdown Time with unit [s|m|h|d]', required=True)
args = parser.parse_args()

# user input time
countdown_string = args.time

# search for numerical value in input
number = re.search("[0-9]{1,}", countdown_string)

# search for unit in input
unit = re.search("[a-zA-Z]{1,}", countdown_string)


# check if all needed is given
if number == None or unit == None:
    print("missing data")
else:
    number = number[0]
    unit = unit[0]

# convert unit to lower letter
unit = unit.lower()

# calculate time in seconds
match unit:
    case "s":
        runtime = int(number)
    case "m":
        runtime = int(number) * 60
    case "h":
        runtime = int(number) * 60 * 60
    case "d":
        runtime = int(number) * 60 * 60 * 24

dt1 = datetime.datetime.now()
dt2 = dt1 + datetime.timedelta(seconds=runtime)
max_dif = dt2 - dt1
seconds_to_end_max = int(round(max_dif.total_seconds(),0))

run = True
i = 5
balken_max = 40
leer = 0
while run == True:
    # time now
    dt = datetime.datetime.now()
    # dif between now and goal time
    timedif = dt2 - dt
    seconds_to_end = int(round(timedif.total_seconds(),0)) + 1

    # calculate bars
    balken = int(round(balken_max - timedif/max_dif*balken_max,0))
    leer = balken_max - balken

    # print Time
    if i > 5:
        print(str(dt) + " [" + str(timedif) + "] [" +  "=" * balken + ">" + " " * leer + "] " + str(dt2), end="\r")
        i = 0

    i += 1

    # end time reched?
    if dt2 <= dt:
        run = False


    time.sleep(0.1)
print("")