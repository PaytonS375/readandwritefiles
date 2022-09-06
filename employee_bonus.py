import csv

infile = open('Employee.csv','r')

csvfile = csv.reader(infile, delimiter='')

next(csvfile)