import csv

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile)
writer = csv.writer(outfile)

next(csvfile)

running_month = 0

monthlist = ['January','February','March','April','May','June','July','August','September','October','November','December']
total_steps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for record in csvfile:
    month = int(record[0])
    steps = int(record[1])

    if month == 1:
        total_steps[0] += steps

    elif month == 2:
        total_steps[1] += steps

    elif month == 3:
        total_steps[2] += steps

    elif month == 4:
        total_steps[3] += steps

    elif month == 5:
        total_steps[4] += steps

    elif month == 6:
        total_steps[5] += steps

    elif month == 7:
        total_steps[6] += steps

    elif month == 8:
        total_steps[7] += steps

    elif month == 9:
        total_steps[8] += steps

    elif month == 10:
        total_steps[9] += steps

    elif month == 11:
        total_steps[10] += steps

    elif month == 12:
        total_steps[11] += steps

average_steps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

average_steps[0] = total_steps[0] / 31
average_steps[1] = total_steps[1] / 28
average_steps[2] = total_steps[2] / 31
average_steps[3] = total_steps[3] / 30
average_steps[4] = total_steps[4] / 31
average_steps[5] = total_steps[5] / 30
average_steps[6] = total_steps[6] / 31
average_steps[7] = total_steps[7] / 31
average_steps[8] = total_steps[8] / 30
average_steps[9] = total_steps[9] / 31
average_steps[10] = total_steps[10] / 30
average_steps[11] = total_steps[11] / 31

writer.writerow([monthlist[0], average_steps[0]])
writer.writerow([monthlist[1], average_steps[1]])
writer.writerow([monthlist[2], average_steps[2]])
writer.writerow([monthlist[3], average_steps[3]])
writer.writerow([monthlist[4], average_steps[4]])
writer.writerow([monthlist[5], average_steps[5]])
writer.writerow([monthlist[6], average_steps[6]])
writer.writerow([monthlist[7], average_steps[7]])
writer.writerow([monthlist[8], average_steps[8]])
writer.writerow([monthlist[9], average_steps[9]])
writer.writerow([monthlist[10], average_steps[10]])
writer.writerow([monthlist[11], average_steps[11]])