import os
import glob
import pandas as pd

input_file = r'E:\Course Assessment\机电\dataset\abnormal_data\result_abnormal.csv'
os.remove(input_file)

# merge all csv
csv_list = glob.glob('*.csv')  # 查看与该py文件同文件夹下的csv文件数
print('共发现%s个CSV文件' % len(csv_list))
for i in csv_list:  # 循环读取同文件夹下的csv文件
    fr = open(i, 'rb').read()
    with open('result_abnormal.csv', 'ab') as f:  # 将结果保存为result.csv
        f.write(fr)

# set the sample quantity
data_frame = pd.read_csv(input_file)
sam_list = data_frame.iloc[:, 0].copy()
# print(sam_list)
sam_quantity = 2000
sam_num = int(len(sam_list) / sam_quantity)
for i in range(sam_num):
    sam_list[sam_quantity*i: sam_quantity*(i+1)] = i+23 # should be "+1", the normal has 22 samples

# data_frame.replace(data_frame.iloc[:, 0], sam_list)
data_frame[''] = sam_list
data_frame = data_frame.drop(data_frame.index[sam_num*sam_quantity:len(sam_list)])
data_frame.to_csv(input_file, sep=',', header=None, index=None)