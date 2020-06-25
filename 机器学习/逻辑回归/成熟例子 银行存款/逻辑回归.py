import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data=pd.read_csv('bank.csv',delimiter=';')
data=data.dropna()
print(data.shape)
print(list(data.columns))
print(data.head())
# 把y变为数值型，并进行简单的统计。
data.loc[data['y']=='yes','y']=1
data.loc[data['y']=='no','y']=0
data['y'].value_counts()
sns.countplot(x='y',data=data,palette='hls')
plt.show()
# 工作和y的关系
pd.crosstab(data.job,data.y).plot(kind='bar')
plt.title('Purchase Frequency for Job Title')
plt.xlabel('Job')
plt.ylabel('Frequency of Purchase')
plt.show()
#plt.savefig('purchase_fre_job')
# 购买存款的频率在很大程度上取决于职位。 因此，职称可以是结果变量的良好预测因子。
# 婚姻状况与y的关系：
table=pd.crosstab(data.marital,data.y)
table.div(table.sum(axis=1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Marital Status vs Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Proportion of Customers')
# 婚姻状况似乎不是结果变量的强预测因子。
# 教育情况与y的关系
table=pd.crosstab(data.education,data.y)
table.div(table.sum(axis=1).astype(float),axis=0).plot(kind='bar')
plt.title('Stacked Bar Chart of Education Status vs Purchase')
plt.xlabel('Education Status')
plt.ylabel('Proportion of Customers')

# 创建虚拟变量:　　这是只有两个值的变量，0和1。
# 回顾我们数据集的信息，有11个object，其中y已经转化过来，另外有10个类别需要转化。
cat_vars = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
for var in cat_vars:
    cat_list = 'var' + '_' + var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1 = data.join(cat_list)
    data = data1
data_vars = data.columns.values.tolist()
to_keep = [i for i in data_vars if i not in cat_vars]
data_final = data[to_keep]
data_final.columns.values
# 分离特征与目标变量
data_final_vars=data_final.columns.values.tolist()
y=['y']
X=[i for i in data_final_vars if i not in y]
# 特征选择
# 递归特征消除（Recursive Feature Elimination，RFE）基于以下思想： 首先，在初始特征集上训练估计器，并且通过coef_属性或通过feature_importances_属性获得每个特征的重要性。 然后，从当前的一组特征中删除最不重要的特征。 在修剪的集合上递归地重复该过程，直到最终到达所需数量的要选择的特征。
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
rfe = RFE(logreg, 18)
rfe = rfe.fit(data_final[X], data_final[y] )
print(rfe.support_)
print(rfe.ranking_)
# 根据布尔值筛选我们想要的特征(参考）：
from itertools import compress
cols=list(compress(X,rfe.support_))
# 或者：
cols= [i for index,i in list(enumerate(X)) if rfe.support_[index] == True]
# 执行模型
import statsmodels.api as sm
X=data_final[cols]
y=data_final['y']
logit_model=sm.Logit(y,X)
logit_model.raise_on_perfect_prediction = False
result=logit_model.fit()
print(result.summary().as_text)
# 大多数变量的p值小于0.05，因此，大多数变量对模型都很重要。

# 逻辑回归模型的拟合
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
# 可以看到，准确率达到了0.9.

# 交叉验证
# 　　交叉验证尝试避免过度拟合，同时仍然为每个观察数据集生成预测。 我们使用10折交叉验证来训练我们的Logistic回归模型。
from sklearn import model_selection
from sklearn.model_selection import cross_val_score

kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))
# 平均精度仍然非常接近Logistic回归模型的准确度; 因此，我们可以得出结论，我们的模型很好拟合了数据。
# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
# 结果告诉我们，我们有10848 + 2564个正确预测和1124 + 121个错误预测。

# 计算精度（precision）召回(recall)F测量(F-measure)和支持(support)
# 精度是比率tp /（tp + fp），其中tp是真阳性的数量，fp是假阳性的数量。 精确度直观地是分类器如果是负的则不将样品标记为阳性的能力。
# 召回是比率tp /（tp + fn）其中tp是真阳性的数量，fn是假阴性的数量。 召回直观地是分类器找到所有阳性样本的能力。
# F-beta分数可以解释为精确度和召回率的加权调和平均值，其中F-β分数在1处达到其最佳值，在0处达到最差分数。
# F-beta评分对召回的重量超过精确度β因子。 beta = 1.0意味着召回和精确度同样重要。
# 支持是y_test中每个类的出现次数。
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
# 可以看出：在整个测试集中，88％的促销定期存款是客户喜欢的定期存款。 在整个测试集中，90％的客户首选定期存款。
# Macro F1 Score
from sklearn.metrics import f1_score
print(f1_score(y_test, y_pred, average = 'macro'))

# ROC曲线
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
#plt.savefig('Log_ROC')
plt.show()

# ROC曲线是与二元分类器一起使用的另一种常用工具。 虚线表示纯随机分类器的ROC曲线; 一个好的分类器尽可能远离该线（朝左上角）。