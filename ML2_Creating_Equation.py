'''
  A*SAT = 30%
+ B*GPA = 22%
+ C*gender = 12%
+ D*Etnicity = 15%
+ E*First_Gen = 5%
+ F*Decision = 16%

#0.3*SAT + 0.22 * GPA + 0.12 * gender + 0.15 * Ethnicity + .05 * First_Gen + 0.16 * Decision >= 0.8

____________________________________________________________
if the values satisfy equation or yield anwer greater than 0.8, no change

else add to list of exceptions

at the end, check manually if exceptions are outliers
____________________OR____________________

we mutate the constants; if the value lies below 0.8, increase constants and try again
if higher, decrease them and try again
try getting value in range (0.9-1.1)
if more than a specific amount of iterations to increase/decrease, put it on outlier
'''
################### __________________________________ ###################
import csv

f = open('D:/ML with Profiles/Harvard Student Profiles/profiles___1.csv','r',newline='')
r = csv.reader(f)
d = []
for i in r:
    d+=[i]
l = d[1:]   
SAT = {1300: 0.026, 1310: 0.026, 1320: 0.026, 1330: 0.026, 1340: 0.026, 1350: 0.026, 1360: 0.026, 1370: 0.026, 1380: 0.026, 1390: 0.026, 1400: 0.026, 1410: 0.04, 1420: 0.045, 1430: 0.05, 1440: 0.055, 1450: 0.064, 1460: 0.073, 1470: 0.097, 1480: 0.13, 1490: 0.15, 1500: 0.2, 1510: 0.24, 1520: 0.34, 1530: 0.4, 1540: 0.46, 1550: 0.57, 1560: 0.67, 1570: 0.78, 1580: 0.86, 1590: 0.95, 1600: 1}
GPA = {3.4: 0.01, 3.5: 0.01, 3.6: 0.01, 3.7: 0.02, 3.8: 0.06, 3.9: 0.1, 4.0: 0.38, 4.1: 0.39, 4.2: 0.48, 4.3: 0.55, 4.4: 0.75, 4.5: 0.96, 4.6: 0.96, 4.7: 0.97, 4.8: 0.98, 4.9: 0.99, 5.0: 1}
gender = {'M':1, 'F': 0.91, 'O': 0.81}
Ethnicity = {'W': 1, 'A': 0.8, 'H': 0.3, 'B': 0.1, 'AW':0.1, 'O': 0.1} #W: white; A: Asian; H: Hispanic; B: Black; AW: Asian White; O: Others;
First_Gen = {'Y': 0.52, 'N': 1}
Decision = {'R': 1, 'E': 0.75}

s = 0.38
g = 0.30
c = 0.12
e = 0.03
f = 0.05
d = 0.12

vd = [s, g, c, e, f, d]
vl = [{1300: 0.026, 1310: 0.026, 1320: 0.026, 1330: 0.026, 1340: 0.026, 1350: 0.026, 1360: 0.026, 1370: 0.026, 1380: 0.026, 1390: 0.026, 1400: 0.026, 1410: 0.04, 1420: 0.045, 1430: 0.05, 1440: 0.055, 1450: 0.064, 1460: 0.073, 1470: 0.097, 1480: 0.13, 1490: 0.15, 1500: 0.2, 1510: 0.24, 1520: 0.34, 1530: 0.4, 1540: 0.46, 1550: 0.57, 1560: 0.67, 1570: 0.78, 1580: 0.86, 1590: 0.95, 1600: 1},
{3.4: 0.01, 3.5: 0.01, 3.6: 0.01, 3.7: 0.02, 3.8: 0.06, 3.9: 0.1, 4.0: 0.38, 4.1: 0.39, 4.2: 0.48, 4.3: 0.55, 4.4: 0.75, 4.5: 0.96, 4.6: 0.96, 4.7: 0.97, 4.8: 0.98, 4.9: 0.99, 5.0: 1},
{'M': 1, 'F': 0.91, 'O': 0.81},
{'W': 1, 'A': 0.8, 'H': 0.3, 'B': 0.1, 'AW': 0.1, 'O': 0.1},
{'Y': 0.52, 'N': 1},
{'R': 1, 'E': 0.75}]
n = 100000
for j in l:
    r = (vd[0] * SAT[int(j[0])] + vd[1] * GPA[float(j[1])] + vd[2] * gender[j[2]] + vd[3] * Ethnicity[j[3]] + vd[4] * First_Gen[j[4]] + vd[5] *Decision[j[5]])
    if r < 0.8 or r > 0.98:
        h1 = vd.copy()
        h2 = vl.copy()
        x = 0
        while x < n and r < 0.7:
            test = [SAT[int(j[0])], GPA[float(j[1])], gender[j[2]], Ethnicity[j[3]], First_Gen[j[4]], Decision[j[5]]]
            min_diff = test.index(min(test))
            max_diff = test.index(max(test))            
            vd[max_diff] += 0.000005
            try:
                vl[min_diff][float(j[min_diff])] += 0.000005
            except:
                vl[min_diff][j[min_diff]] += 0.000005
            r = (vd[0] * SAT[int(j[0])] + vd[1] * GPA[float(j[1])] + vd[2] * gender[j[2]] + vd[3] * Ethnicity[j[3]] + vd[4] * First_Gen[j[4]] + vd[5] *Decision[j[5]])
            x+=1
        else:
            if x == n:
                vd = h1.copy()
                vl = h2.copy()
        while x < n and r > 1.05:
            test = [SAT[int(j[0])], GPA[float(j[1])], gender[j[2]], Ethnicity[j[3]], First_Gen[j[4]], Decision[j[5]]]
            min_diff = test.index(min(test))
            try:
                vl[min_diff][float(j[min_diff])] -= 0.000005
            except:
                vl[min_diff][j[min_diff]] -= 0.000005
            vd[max_diff] -= 0.000005
            r = (vd[0] * SAT[int(j[0])] + vd[1] * GPA[float(j[1])] + vd[2] * gender[j[2]] + vd[3] * Ethnicity[j[3]] + vd[4] * First_Gen[j[4]] + vd[5] *Decision[j[5]])
            x+=1
        else:
            if x == n:
                vd = h1.copy()
                vl = h2.copy()

print(vd)
print(vl)


'''
[0.31351999999993846, 0.2549650000000074, 0.07212999999995212, 0.1546000000000046, 0.03313000000000655, 0.17537000000001537]
[{1300: 0.07600000000000298, 1310: 0.026, 1320: 0.026, 1330: 0.026, 1340: 0.026, 1350: 0.026, 1360: 0.07600000000000298, 1370: 0.07600000000000298, 1380: 0.07600000000000298, 1390: 0.026, 1400: 0.126000000000053, 1410: 0.18748000000011625, 1420: 0.045, 1430: 0.08552000000001818, 1440: 0.1550000000000896, 1450: 0.11400000000005, 1460: 0.1730000000001, 1470: 0.23756500000014058, 1480: 0.14537000000001538, 1490: 0.17277000000002277, 1500: 0.2600200000000044, 1510: 0.23646999999999646, 1520: 0.28146000000026644, 1530: 0.3370800000002864, 1540: 0.4092000000002312, 1550: 0.27947500000054504, 1560: 0.5716799999993559, 1570: 0.7223999999996227, 1580: 0.86, 1590: 0.95, 1600: 1}, {3.4: 0.06728999999999723, 3.5: 0.01, 3.6: 0.07717500000000711, 3.7: 0.18459500000011342, 3.8: 0.1132650000000498, 3.9: 0.31403999999985854, 4.0: 0.38, 4.1: 0.39, 4.2: 0.48, 4.3: 0.55, 4.4: 0.7181399999997913, 4.5: 0.9447849999999003, 4.6: 0.96, 4.7: 0.97, 4.8: 0.98, 4.9: 0.99, 5.0: 1}, {'M': 1, 'F': 0.8176199999993948, 'O': 0.81}, {'W': 1, 'A': 0.753749999999697, 'H': 0.369874999999682, 'B': 0.2508500000001461, 'AW': 0.1, 'O': 0.11352000000001353}, {'Y': 0.5193199999999956, 'N': 1}, {'R': 1, 'E': 0.75}]
'''


























