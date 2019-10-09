import csv

input_file = csv.reader(open('dowjones.csv'))
output_file = open('dowjonescleaned.csv', 'w')
csv_writer = csv.writer(output_file)

is_first_line = True

for row in input_file:
    if is_first_line:
        is_first_line = False
        csv_writer.writerow(['Date','Open', 'Close'])
    else:
        Date = row[0]
        Date = Date.split("/")
        Date = Date[2]
        Open = row[1]
        Close = row[4]
        if Date == '2011' or Date == '2012' or Date == '2013' or Date == '2014' or Date == '2015':
            csv_writer.writerow([Date,Open,Close]).rstrip('\n')
