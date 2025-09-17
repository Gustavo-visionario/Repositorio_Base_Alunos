import csv

examplefile = open('frutas.csv')
examplereader = csv.reader (examplefile)

for row in examplereader:
    print('row #' + str(examplereader.line_num) + '' + str(row))