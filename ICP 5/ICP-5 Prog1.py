import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

dataset = pd.read_csv('train.csv')


plt.scatter(x=dataset['GarageArea'], y=dataset['SalePrice'])
plt.ylabel('SalePrice')
plt.xlabel('GarageArea')
plt.show()

dataset = dataset[dataset['GarageArea'] < 1000].where(dataset['GarageArea'] != 0)
dataset = dataset[dataset['SalePrice'] < 500000].where(dataset['SalePrice'] != 0)

plt.scatter(x=dataset['GarageArea'], y=dataset['SalePrice'])
plt.xlim(-75, 1600)
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.show()