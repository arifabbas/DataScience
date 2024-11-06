import matplotlib.pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

# print(plt.subplot())
# fig,ax =plt.subplots()
# print(ax)
# print(fig)

# ax.plot(ages_x,dev_y,label='Dev Salaries')
# ax.plot(ages_x,py_dev_y,label='Py Salaries')
# ax.plot(ages_x,js_dev_y,label='JS Salaries')

# ax.legend()



# customizations

# fig,(ax1,ax2) =plt.subplots(ncols=1,nrows=2, sharex=True)
# # print(ax)
# ax1.plot(ages_x,dev_y,label='Dev Salaries')
# ax1.plot(ages_x,py_dev_y,label='Py Salaries')
# ax2.plot(ages_x,js_dev_y,label='JS Salaries')


# ax1.set_xlabel('Ages')
# ax1.set_ylabel('Salaries')
# ax1.set_title('Salaries vs Ages')


# ax2.set_xlabel('Ages')
# ax2.set_ylabel('Salaries')
# ax2.set_title('Salaries vs Ages')
# ax1.legend()
# ax2.legend()

# multiple figs
fig1,ax1 =plt.subplots()
fig2,ax2 =plt.subplots()

ax1.plot(ages_x,dev_y,label='Dev Salaries')
ax1.plot(ages_x,py_dev_y,label='Py Salaries')
ax2.plot(ages_x,js_dev_y,label='JS Salaries')


ax1.set_xlabel('Ages')
ax1.set_ylabel('Salaries')
ax1.set_title('Salaries vs Ages')


ax2.set_xlabel('Ages')
ax2.set_ylabel('Salaries')
ax2.set_title('Salaries vs Ages')
ax1.legend()
ax2.legend()

fig1.savefig('Dev and Py Sal vs Ages')
fig2.savefig('JS Sal vs Ages')

plt.tight_layout()
plt.show()