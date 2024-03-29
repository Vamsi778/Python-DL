import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('./glass.csv')
y = df["Type"]
df1 = df.drop("Type",axis=1).copy()
# create training and testing
X_train, X_test, Y_train, Y_test = train_test_split(df1, y,test_size=0.15)
##SVM
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
#acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
acc_svc1 = round(svc.score(X_test, Y_test) * 100, 2)
print("Accuracy is",acc_svc1)