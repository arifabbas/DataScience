from matplotlib import pyplot as plt
import csv
from collections import Counter

# reading csv
with open('sample_data.csv') as file1:
    csv_reader= csv.DictReader(file1) 
    # first=next(csv_reader)
    language_reader= Counter()
    for row in csv_reader:
        language_reader.update(row['LanguageHaveWorkedWith'].split(';'))

    # print(language_reader)
lang=[]
value=[]
for l,c in language_reader.most_common(15):
    lang.append(l)
    value.append(c)

print(lang, value)


# plotting
lang.reverse()
value.reverse()
plt.barh(lang,value)
plt.legend()
plt.xlabel("Language")
plt.ylabel("Count")
plt.title('StackOverflow most common Languages')
plt.show()

