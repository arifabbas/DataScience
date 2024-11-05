import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA
from itertools import count
import csv
import random
import pandas as pd


# index=count()
# x=[]
# y=[]
# def animate(i):
#     x.append(next(index))
#     y.append(random.randint(0,5))
#     plt.cla()
#     plt.plot(x,y)

# ani=FA(plt.gcf(),animate,interval=1000)


# animate file
xvals=[]
field1=[]
field2=[]



def animate(i):
    with open('Temp_file.csv','r') as file1:
        csv_reader=csv.DictReader(file1)
        for row in csv_reader:
            xvals.append(row['XValues'])
            field1.append(row['Field1'])
            field2.append(row['Field2'])


    # df=pd.read_csv('Temp_file.csv')
    # xvals=df['XValues']
    # field1=df['Field1']
    # field2=df['Field2']

    plt.cla()
    plt.plot(xvals,field1, label='Channel1')
    plt.plot(xvals,field2, label='Channel2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani=FA(plt.gcf(),animate,interval=1000,cache_frame_data=False)

plt.show()
