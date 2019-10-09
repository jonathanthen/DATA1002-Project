import csv

csv_reader = csv.reader(open('DP_LIVE_09102019024123039.csv'))
output_file = open('housecleaned.csv', 'w')
csv_writer = csv.writer(output_file)

is_first_line = True

for row in csv_reader:
    if is_first_line:
        is_first_line = False
        csv_writer.writerow(['Location','Time', 'Value'])
    else:
        freq = row[4]
        time = row[5]
        time = time.split("-")
        time = time[0]
        if freq == "Q":
            if time == '2011' or time == '2012' or time == '2013' or time == '2014' or time == '2015':
                location = row[0]
                value = row[6]
                csv_writer.writerow([location,time,value])