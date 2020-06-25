from sklearn import svm
x = [[3, 3], [4, 3], [1, 1]]
y = [1, 1, -1]
model = svm.SVC(kernel='linear')
model.fit(x, y)
# 打印支持向量
print(f"打印支持向量 :{model.support_vectors_}")
# 第2和第0个点是支持向量
print(f"model.support_{model.support_}")
# 有几个支持向量
print(f"model.n_support_{model.n_support_}")
print(f"属于第几个分类：{model.predict([[4,3]])}")
print(f"超平面属性 {model.coef_}，截距：{model.intercept_}")



