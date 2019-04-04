#Usage
#python "C:\Users\Hans Jin\Desktop\PaperProject\DataSeparation.py"

import numpy as np
from sklearn.model_selection import train_test_split

datapath = r'C:\Users\Hans Jin\Desktop\PaperProject\origindata.csv'
trainpath = r'C:\Users\Hans Jin\Desktop\train_usual.csv'
testpath = r'C:\Users\Hans Jin\Desktop\test_usual.csv'

#Load data into a matrix. CSV file uses comma as delimiter. Skip the first row.
my_matrix = np.loadtxt(open(datapath),delimiter=",",skiprows=1)
X, y = my_matrix[:,:-1],my_matrix[:,-1]
#700 training data and 300 testing data. Random_state determines where the data should go to.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)
#Write numbers to new files in their original format
train= np.column_stack((X_train,y_train))
np.savetxt(trainpath,train,fmt="%9.8f",delimiter=",")
test = np.column_stack((X_test, y_test))
np.savetxt(testpath,test,fmt="%9.8f",delimiter=",")
