#from sklearn import tree

'''
features = [[140, 1], [130, 1], [150, 0], [170, 0]]     #* weight followed by bumpy
labels = [0, 0, 1, 1]                                   #* 1 is orange and 0 is apple

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

weight = int(input("Enter the mass of the fruit: "))
bumpy = int(input("Is the fruit bumpy? "))

output = clf.predict([[weight, bumpy]])

if output == 1:
    print("Orange")
else:
    print("Apple")
'''

'''
import numpy as np
from sklearn.datasets import load_iris  
from sklearn import tree
import pydot

iris = load_iris()
test_idx = [0, 50, 100]

train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

'''
'''
#? Visualisation code
from sklearn.externals.six import StringIO

dot_data = StringIO()
tree.export_graphviz(clf, 
out_file=dot_data, 
feature_names=iris.feature_names, 
class_names=iris.target_names, 
filled=True, rounded=True, impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
'''

'''
import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height =  28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()
'''

from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)

from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)

class KClassifier():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def closest(self, row):
        shortest_dist = euc(row, self.x_train[0])
        shortest_index = 0

        for i in range(1, len(self.x_train)):
            distance = euc(row, self.x_train[i])
            if distance < shortest_dist:
                shortest_dist = distance
                shortest_index = i
        
        return self.y_train[shortest_index]

    def predict(self, x_test):
        predictions = []

        for row in x_test:
            label = self.closest(row)
            predictions.append(label)

        return predictions

#from sklearn.neighbors import KNeighborsClassifier
my_classifier = KClassifier()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))