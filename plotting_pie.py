from matplotlib import pyplot as plt

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.style.use("fivethirtyeight")

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}, shadow=True, explode=explode, startangle=90, autopct='%1.1f%%', )
plt.tight_layout()
plt.legend(loc=(0.5,0.7))
plt.title("Pie chart")
plt.show()



# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f