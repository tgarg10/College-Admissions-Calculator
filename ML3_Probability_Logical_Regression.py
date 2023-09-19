import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

#marketing_df = pd.read_csv('https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/marketing_cva_f.csv')
#marketing_df=marketing_df.drop(['Customer','Vehicle_Class','avg_vehicle_age','months_last_claim','Total_Claim_Amount'],axis=1)

marketing_df = pd.read_csv('profiles_sorted_2 - Copy.csv')
#marketing_df=marketing_df.drop(['Id','Class'],axis=1)
mark_array=marketing_df.values
mark_array[:, 0] = mark_array[:, 0].astype(int)
mark_array[:, 1] = mark_array[:, 1].astype(float)
mark_array[:, 2] = mark_array[:, 2].astype(int)
mark_array[:, 3] = mark_array[:, 3].astype(int)
mark_array[:, 4] = mark_array[:, 4].astype(int)
mark_array[:, 5] = mark_array[:, 5].astype(int)

X = np.array(mark_array)
Y = [1]*359

clf = LogisticRegression()
clf.fit(X, Y)
pred = clf.predict_proba([[1480,5.0,1,0,1,1]])
print(pred[0])
#1: asian, 2: black, 3: Hispanic, 4: Others, 5: White
