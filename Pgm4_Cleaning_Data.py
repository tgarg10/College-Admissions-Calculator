import csv

f = open('profiles_stan.csv','r', newline='')
w = open('Stanford Student Profiles/profiles___3.csv','w', newline='')
fr = csv.reader(f)
fw = csv.writer(w)
l = []
for i in fr:
    l+=[i]
for j in range(len(l)):
    if l[j][1] == '':
        l[j][1] = '1450'
    if l[j][2] == '':
        l[j][2] = '4.2'
    if l[j][3] == '':
        l[j][3] = '34'
    l[j][4] = l[j][4].replace('<span itemprop="title">','').replace('B.B.A., ','').replace('B.A., ','').replace('B.A.,','').replace('B.S.,','').replace('B.B.A.,','').replace('B.S., ','')
    if 'Male' == l[j][5] or 'Female' in l[j][5]:
        l[j][5] = l[j][5].replace('Male', '1').replace('Female','2')
    else:
        l[j][5] = '3'
    if 'Asian' in l[j][6]:
        l[j][6] = '1'
    elif 'White' in l[j][6] or 'Native' in l[j][6]:
        l[j][6] = '2'
    elif 'Black' in l[j][6]:
        l[j][6] = '3'
    elif 'Hispanic' in l[j][6]:
        l[j][6] = '4'
    else:
        l[j][6] = '5'
    if l[j][8] == 'Yes':
        l[j][8] = '1'
    else:
        l[j][8] = '0'
    if 'Regular' in l[j][9] or '' == l[j][9]:
        l[j][9] = '1'
    else:
        l[j][9] = '0'
f.close()
fw.writerows(l)
w.close()
