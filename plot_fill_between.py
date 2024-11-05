import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("data.csv")
ages=df['Age']
py_salaries=df['Python']
js_salaries=df['JavaScript']
dev_salaries=df['All_Devs']


plt.plot(ages, dev_salaries, linestyle='--', color='#444444', label='All_Dev')
plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries>dev_salaries), interpolate=True, alpha=0.25, label='Above Avg', color='green')

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries<=dev_salaries), interpolate=True, alpha=0.25, label='Below Avg', color='red')


plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.grid(True)
plt.show()
