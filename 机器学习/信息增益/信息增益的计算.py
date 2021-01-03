import numpy as np
import math
def createData():
    datasets = [[0,0,0,0,'no'],
                [0,0,0,1,'no'],
                [0,1,0,1,'yes'],
                [0,1,1,0,'yes'],
                [0,0,0,0,'no'],
                [1,0,0,0,'no'],
                [1,0,0,1,'no'],
                [1,1,1,1,'yes'],
                [1,0,1,2,'yes'],
                [1,0,1,2,'yes'],
                [2,0,1,2,'yes'],
                [2,0,1,1,'yes'],
                [2,1,0,1,'yes'],
                [2,1,0,2,'yes'],
                [2,0,0,0,'no']]
    lables = ['age','work','hourse','credit','apply']
    return datasets,lables

def shannoEnt(datasets):
    lableCount = {}
    for dataset in datasets:
        lable = dataset[-1]
        if lable not in lableCount.keys():
            lableCount[lable] =0
        lableCount[lable]+=1
    shanoEnt = 0
    l = len(datasets)
    for key in lableCount.keys():
        tmp = float(lableCount[key])/l
        shanoEnt -= tmp*math.log2(tmp)
    return shanoEnt
datasets,lables = createData()
shanoEnt = shannoEnt(datasets)
print("shanoEnt",shanoEnt)

# 计算每个特征的信息增益

def splitdatasets(datasets,axis,value):
    retDataset = []
    for featVec in datasets:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataset.append(reducedFeatVec)
    return retDataset
# 计算axis为列的信息增益
def infoGain(datasets,axis):
    baseEnt = shannoEnt(datasets)
    newEnt = 0.0
    featlist = [example[axis] for example in datasets]
    uniqueVals = set(featlist)
    for value in uniqueVals:
        subDataSet = splitdatasets(datasets,axis,value)
        prob = len(subDataSet)/float(len(datasets))
        newEnt +=prob*shannoEnt(subDataSet)
    infoGain = baseEnt -newEnt
    return infoGain

print(infoGain(datasets,0))
print(infoGain(datasets,1))
print(infoGain(datasets,2))
print(infoGain(datasets,3))


