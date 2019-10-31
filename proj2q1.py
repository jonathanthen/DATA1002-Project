import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("PISA2015-cleaned.csv")
#print(df)

# plt.scatter("Proportion of ISCED Level 5a Teachers","Math Score",data=df)
# plt.scatter("Proportion of ISCED Level 5a Teachers","Reading Score",data=df)
# plt.scatter("Proportion of ISCED Level 5a Teachers","Science Score",data=df)
# # #plt.scatter("Math Score","Index Mother Occupation Status",data=df)
# # #plt.plot("Country","Index Father Occupation Status",data=df)
#
# plt.xticks(rotation=90)
#
# plt.legend()
# plt.show()

X = df["Student-Teacher Ratio"].values.reshape(-1, 1)
Y = df["Math Score"].values.reshape(-1, 1)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.ylim(300, 600)
plt.xlim(0, 30)
plt.title("Graph of Mathematics PISA Score vs Student Teacher Ratio")
plt.xlabel("Student Teacher Ratio (Students per Teacher)")
plt.ylabel("Mathematics PISA Score (Score)")
plt.show()
# plt.matshow(df.corr())
# plt.xticks(range(len(df.columns)), df.columns)
# plt.yticks(range(len(df.columns)), df.columns)
# plt.xticks(rotation=90)
# plt.colorbar()
# plt.show()
