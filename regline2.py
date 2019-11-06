import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('PISA2015-cleaned.csv')

X = df.values[:, 6:8]      # slice dataFrame for Student Teacher Ratio and Proportion of ISCED 5a Master Teachers
y = df.values[:, 3]     # slice dataFrame for Science PISA Scores

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
regr = linear_model.LinearRegression().fit(X_train, y_train)

# Let's create one sample and predict the Science Score
sample = [50, 0.1]        # A sample - Student Teacher Ratio of 50 and Proportion of ISCED 5a Master Teachers of 0.1

print('----- Sample case -----')
for column, value in zip(list(df)[6:8], sample):
    print(column + ': ' + str(value))
sample_pred = regr.predict([sample])
print('Predicted Science Scores:', int(sample_pred))
print('-----------------------')

# The coefficients
print('Coefficients:')
print(regr.coef_)
# Use the model to predict y from X_test
y_pred = regr.predict(X_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))
