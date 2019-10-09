import csv

csv_reader = csv.reader(open('historicalincomebystate.csv'))
output_file = open('incomecleaned.csv', 'w')
csv_writer = csv.writer(output_file)

is_first_line = True
is_sec_line = True
is_third_line = True
is_fourth_line = True
count = 0

for row in csv_reader:
    if is_first_line:
        is_first_line = False
        continue
    if is_sec_line:
        is_sec_line = False
        continue
    if is_third_line:
        is_third_line = False
        continue
    if is_fourth_line:
        is_fourth_line = False
        csv_writer.writerow(['State','Year 2015 Median Income', 'Year 2014 Median Income','Year 2013 Median Income','Year 2012 Median Income','Year 2011 Median Income'])
    else:
        year2011 = row[19]
        year2012 = row[17]
        year2013 = row[15]
        year2014 = row[11]
        year2015 = row[9]
        state = row[0]

        if count == 0 or count == 1:
            count += 1
            continue
        if count == 54:
            break
        else:
            csv_writer.writerow([state,year2015,year2014,year2013,year2012,year2011])
            count += 1

