import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

#################################################################################


########################## DECISION TREE #################################
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
#### your code goes here
from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)

print(acc)
### be sure to compute the accuracy on the test set


def submitAccuracies():
    return {"acc": round(acc, 3)}