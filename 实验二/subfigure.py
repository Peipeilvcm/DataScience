# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 02:02:01 2018

@author: Administrator
"""
import matplotlib.pyplot as plt
from experiment2 import get_one_csv

if __name__ == '__main__':
    plt.figure(num=60, figsize=(50,40))
    plt.ylabel('electric')
    for i in range(131,191):
        Data = get_one_csv(i, '兔子数据')
        plt.subplot(15,4,i-130)
        plt.plot(Data[:,0],Data[:,1])
        plt.ylim((-45, 45))
    plt.show() 