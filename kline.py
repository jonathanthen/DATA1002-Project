import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn import neighbors
from sklearn.model_selection import train_test_split

df = pd.read_csv('PISA2015-cleaned.csv')
X = df.values[:, 6].reshape(-1, 1)      # slice dataFrame for Student Teacher Ratio
y = df.values[:, 1].reshape(-1, 1)      # slice dataFrame for Mathematics PISA Scores

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
neigh = neighbors.KNeighborsRegressor(n_neighbors=4).fit(X_train, y_train)

# Let's create one sample and predict the Mathematics PISA Score
sample = [1]        # A sample - Student Teacher Ratio of 1 
print('----- Sample case -----')
for column, value in zip(list(df)[6], sample):
    print(column + ': ' + str(value))
sample_pred = neigh.predict([sample])
print('Predicted Mathematics Score:', int(sample_pred))
print('-----------------------')

# Use the model to predict X_test
y_pred = neigh.predict(X_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))