import csv
#import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn import linear_model
import scipy.stats import linregress

csv_reader = csv.reader(open('PISA2015-cleaned.csv'))
is_first_line = True

country_data = []
math_data = []
science_data = []
stratio_data = []
teacher_data = []

for row in csv_reader:
    if is_first_line:
        is_first_line = False
        continue

    else:
        country = row[0]
        math = int(row[1])
        science = int(row[3])
        stratio = float(row[6])
        teacher = float(row[7])

        country_data.append(country)
        math_data.append(math)
        science_data.append(science)
        stratio_data.append(stratio)
        teacher_data.append(teacher)

x = math_data
y = stratio_data

plt.title(" Graph of Mathematics PISA Score vs Student Teacher Ratio")
plt.scatter(y, x)
plt.ylim(300, 600)
plt.xlim(0, 30)
plt.xlabel('Student Teacher Ratio')
plt.ylabel('Mathematics PISA Score')
linear_model.LinearRegression()
plt.show()

