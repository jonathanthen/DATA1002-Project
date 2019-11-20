import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('PISA2015-clean.csv')
math = df['Averages for PISA mathematics scale: overall mathematics, age 15 years']
#stratio = df['Averages for student-teacher ratio, age 15 years']
mathstratio = math['Averages for student-teacher ratio, age 15 years']
print(mathstratio)