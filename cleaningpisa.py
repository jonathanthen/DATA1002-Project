import csv

csv_reader = csv.reader(open('PISA2015-clean.csv'))
output_file = open('PISA2015-cleaned.csv', 'w', newline='')
csv_writer = csv.writer(output_file)

is_first_line = True
is_sec_line = True
is_third_line = True

for row in csv_reader:
    if is_first_line:
        is_first_line = False
        csv_writer.writerow(['Country', 'Math Score', 'Reading Score', 'Science Score', 'Index Mother Occupation Status', 'Index Father Occupation Status', 'Student-Teacher Ratio', 'Proportion of ISCED Level 5a Teachers'])
        continue
    if is_sec_line:
        is_sec_line = False
        continue
    if is_third_line:
        is_third_line = False
        continue
    else:
        country = row[0]
        math = row[1]
        reading = row[2]
        science = row[3]
        mother = row[4]
        father = row[5]
        stratio = row[6]
        teacher = row[7]
        csv_writer.writerow([country, math, reading, science, mother, father, stratio, teacher])