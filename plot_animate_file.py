import csv
import random
import time

xvalue=1
field1=1000
field2=1000
fieldnames=['XValues','Field1','Field2']
with open('Temp_file.csv','w') as file1:
    csv_writer=csv.DictWriter(file1,fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('Temp_file.csv','a') as file2:
        csv_writer=csv.DictWriter(file2,fieldnames=fieldnames)
        info={'XValues': xvalue, 'Field1':field1, 'Field2':field2}
        csv_writer.writerow(info)
        print(xvalue,field1,field2)
        xvalue+=1
        field1=field1+random.randint(-6,8)
        field2=field2+random.randint(-6,5)

    time.sleep(1)


