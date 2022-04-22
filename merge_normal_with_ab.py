import pandas as pd
import os

os.remove(r'E:\Course Assessment\机电\dataset\test_data.csv')

# merge the abnormal and normal file
f1 = r'E:\Course Assessment\机电\dataset\normal_data\result_normal.csv'
f2 = r'E:\Course Assessment\机电\dataset\abnormal_data\result_abnormal.csv'
file = [f1, f2]
for i in file:  # 循环读取同文件夹下的csv文件
    fr = open(i, 'rb').read()
    with open('test_data.csv', 'ab') as f:  # 将结果保存为result.csv
        f.write(fr)

# correct the sample number of the second file(the abnormal one)
