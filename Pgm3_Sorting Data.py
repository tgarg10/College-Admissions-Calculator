f = open('profiles_additional_2.csv',newline='')
o = open('profiles_additional_3.csv','w',newline='')
import csv

r = csv.reader(f)
w = csv.writer(o)
l = []
for j in r:
    a = j
    print(a[6])
    if a[6] == '':
        a[6] = 'No'
    if a[7] == '':
        a[7] = 'Regular Decision'
    l += [a]
w.writerows(l)
o.close()
f.close()
