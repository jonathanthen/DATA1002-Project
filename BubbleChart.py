import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("PISA2015-cleaned.csv")

x = df["Student-Teacher Ratio"]
y = df["Science Score"]
z = df["Proportion of ISCED Level 5a Teachers"]
plt.title("Factors that influence student scores")
plt.xlabel("Student-Teacher Ratio (Classroom size:1)")
plt.ylabel("Student Scores")
plt.xlim(0,30)
plt.ylim(300,600)
plt.scatter(x,y,s=z*1000, alpha=0.5)
plt.show()

