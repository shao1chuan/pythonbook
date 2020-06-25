import numpy as np
import pandas as pd
from PIL import Image
import os
train_path = './data/train/'
vaild_path = './data/vaild/'
data_path = '../fer2013.csv'
def make_dir():
    for i in range(0,7):
        p1 = os.path.join(train_path,str(i))
        p2 = os.path.join(vaild_path,str(i))
        if not os.path.exists(p1):
            os.makedirs(p1)
        if not os.path.exists(p2):
            os.makedirs(p2)
def save_images():
    df = pd.read_csv(data_path)
    t_i = [1 for i in range(0,7)]
    v_i = [1 for i in range(0,7)]
    for index in range(len(df)):
        emotion = df.loc[index][0]
        usage = df.loc[index][2]
        image = df.loc[index][1]
        data_array = list(map(float, image.split()))
        data_array = np.asarray(data_array)
        image = data_array.reshape(48, 48)
        im = Image.fromarray(image).convert('L')#8位黑白图片
        if(usage=='Training'):
            t_p = os.path.join(train_path,str(emotion),'{}.jpg'.format(t_i[emotion]))
            im.save(t_p)
            t_i[emotion] += 1
            #print(t_p)
        else:
            v_p = os.path.join(vaild_path,str(emotion),'{}.jpg'.format(v_i[emotion]))
            im.save(v_p)
            v_i[emotion] += 1
            #print(v_p)
make_dir()
save_images()