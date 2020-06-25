# ## Example: Face Recognition
#
# As an example of support vector machines in action, let's take a look at the facial recognition problem.
# We will use the Labeled Faces in the Wild dataset, which consists of several thousand collated photos of various public figures.
#读取数据集
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person=60)
#看一下数据的规模
print(faces.target_names)
print(faces.images.shape)
# Let's plot a few of these faces to see what we're working with:
# * 每个图的大小是 [62×47]
# * 在这里我们就把每一个像素点当成了一个特征，但是这样特征太多了，用PCA降维一下吧！
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
#降维到150维
pca = PCA(n_components=150, whiten=True, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
#先降维然后再SVM
model = make_pipeline(pca, svc)
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(faces.data, faces.target,
                                                random_state=40)
# 使用grid search cross-validation来选择我们的参数
from sklearn.model_selection import GridSearchCV
param_grid = {'svc__C': [1, 5, 10],
              'svc__gamma': [0.0001, 0.0005, 0.001]}
grid = GridSearchCV(model, param_grid)
# get_ipython().run_line_magic('time', 'grid.fit(Xtrain, ytrain)')
# print(grid.best_params_)
model = grid.best_estimator_
yfit = model.predict(Xtest)
yfit.shape
from sklearn.metrics import classification_report
print(classification_report(ytest, yfit,
                            target_names=faces.target_names))
# * 精度(precision) = 正确预测的个数(TP)/被预测正确的个数(TP+FP)
# * 召回率(recall)=正确预测的个数(TP)/预测个数(TP+FN)
# * F1 = 完整例子*精度*召回率/(精度+召回率)
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(ytest, yfit)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=faces.target_names,
            yticklabels=faces.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
# * 这样显示出来能帮助我们查看哪些人更容易弄混