# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:22:33 2018

@author: Administrator
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

def get_one_csv(cvs_id, filepath):
    file_path = os.getcwd()+'\\'+filepath+'\\'+str(cvs_id)+'.csv'
    csv_data = pd.read_csv(open(file_path), usecols=[0,5],encoding='utf-8')
    csv_data = np.array(csv_data)
    return csv_data

def get_valid_data(csv_id, filepath):
    #找触电点步长
    point_find_step = 1
    threshold = 1.0
    #for i in range(csv_id1,csv_id2):
    Data = []
    file_path = os.getcwd()+'\\'+filepath+'\\'+str(csv_id)+'.csv'
    csv_data = pd.read_csv(open(file_path), usecols=[0,5],encoding='utf-8') 
    csv_data = np.array(csv_data)
    left, right = 0, len(csv_data) - 1
    while left < right:
        if abs(csv_data[left,1]) > threshold:
            break
        left = left + point_find_step
    while right > left:
        if abs(csv_data[right,1]) > threshold:
            break
        right = right - point_find_step
    Data.extend(csv_data[left:right+1])
    Data = np.array(Data)
    Data = Data.reshape(-1,2)
    return Data


fig, ax = plt.subplots(figsize=(30,25))

print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

plt.ylim((-45, 45))
plt.ylabel('electric')

x = np.arange(1,3001,1)
Data = get_one_csv(131, '兔子数据')
line, = ax.plot(x, Data[:,1], linewidth=2)
# FuncAnimation 会在每一帧都调用“update” 函数。
# 在这里设置一个60帧的动画，每帧之间间隔200毫秒
def update(i):
    label = 'csv {0}'.format(i+131)
    Data = get_one_csv(i+131, '兔子数据')
    #line = ax.plot(x, Data[:,1], linewidth=2,label=str(i))
    line.set_ydata(Data[:,1])
    ax.set_xlabel(label)
    return line, ax

if __name__ == '__main__':
    anim = FuncAnimation(fig, update, frames=np.arange(0, 61), interval=200)
    plt.show()
