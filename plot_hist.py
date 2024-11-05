import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('Data.csv')
ages=df['Age']
bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(ages, bins=bins, edgecolor='black', label='Ages into bins')

median_age = 29
color = '#fc4f30'


plt.axvline(median_age, color=color, label='Median Age', linewidth=2)
plt.title('Ages in Data')
plt.legend()
plt.tight_layout()
plt.show()
