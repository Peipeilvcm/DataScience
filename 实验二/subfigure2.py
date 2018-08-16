# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 02:37:35 2018

@author: Administrator
"""
import matplotlib.pyplot as plt
from subfigure import get_one_csv

if __name__ == '__main__':
    plt.figure(num=60, figsize=(80,60))
    plt.ylabel('electric')
    for i in range(131,191):
        Data = get_one_csv(i, '兔子数据')
        plt.plot(Data[:,0],Data[:,1],label=str(i))
    plt.ylim((-45, 45))
    plt.legend() 
    plt.show()