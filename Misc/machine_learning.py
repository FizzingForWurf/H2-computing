#from sklearn import tree

'''
features = [[140, 1], [130, 1], [150, 0], [170, 0]] #* weight followed by bumpy
labels = [0, 0, 1, 1] #* 1 is orange and 0 is apple

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

from sklearn.datasets import load_iris  

iris = load_iris()

print(iris.feature_names)