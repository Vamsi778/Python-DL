import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('foodsales.csv')

train.sales.describe()
print ("The skew :", train.sales.skew())
plt.hist(train.sales, color='green')
plt.show()

numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['sales'].sort_values(ascending=False)[:5], '\n')

nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:27])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'

data = train.select_dtypes(include=[np.number]).interpolate().dropna()

y = np.log(train.sales)
X = data.drop(['sales'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
predictions = model.predict(X_test)
print ("Evaluation using R^2 \n", model.score(X_test, y_test))
from sklearn.metrics import mean_squared_error
print ('Evaluation using RMSE \n', mean_squared_error(y_test, predictions))

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b')
plt.xlabel('Predicted Sales')
plt.ylabel('Actual Food Sales')
plt.title('Regression Model for Food Sales')
plt.show()

corr=train.corr()
sns.heatmap(corr)
plt.show()



