import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.metrics import classification_report, confusion_matrix, matthews_corrcoef, plot_confusion_matrix

#Load data
data = pd.read_csv('data.csv')
data = pd.DataFrame(data)

data.columns = ['body_acc_mean_X', 'body_acc_std_X', 'body_acc_skewness_X', 'body_acc_kurtosis_X', 'body_acc_mean_Y', 'body_acc_std_Y','body_acc_skewness_Y', 'body_acc_kurtosis_Y', 'body_acc_mean_Z', 'body_acc_std_Z', 'body_acc_skewness_Z', 'body_acc_kurtosis_Z', 'total_acc_mean_X', 'total_acc_std_X', 'total_acc_skewness_X', 'total_acc_kurtosis_X', 'total_acc_mean_Y', 'total_acc_std_Y', 'total_acc_skewness_Y', 'total_acc_kurtosis_Y', 'total_acc_mean_Z', 'total_acc_std_Z', 'total_acc_skewness_Z', 'total_acc_kurtosis_Z', 'activity']
activity_names = ['subway', 'driving', 'walking', 'standing']

#Add activity numbers and activity labels
data.loc[data['activity'] == 5, 'activity_name'] = 'subway'
data.loc[data['activity'] == 3, 'activity_name'] = 'driving'
data.loc[data['activity'] == 2, 'activity_name'] = 'walking'
data.loc[data['activity'] == 1, 'activity_name'] = 'standing'
class_names = ['subway', 'driving', 'walking', 'standing']

#Delete all NA values
data = data.dropna()

X = data.drop(columns=['activity', 'activity_name'])
y = data['activity_name']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

#Create support vector classifier
model = SVC()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds))

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(model, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)
plt.show()

matthews_corrcoef(y_test, preds)