#!/usr/bin/python3
import csv
from matplotlib import pyplot as plt
filename='medname.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
#    print(header_row)
#    for index,column_header in enumerate(header_row):
#        print(index,column_header)
    highs=[]
    for row in reader:
        high=int(row[0])
        highs.append(high)
#    print(highs)

#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
#设置图形的格式
plt.title("Daily high temperature,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
