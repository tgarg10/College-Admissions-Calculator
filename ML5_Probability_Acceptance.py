import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

#marketing_df = pd.read_csv('https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/marketing_cva_f.csv')
#marketing_df=marketing_df.drop(['Customer','Vehicle_Class','avg_vehicle_age','months_last_claim','Total_Claim_Amount'],axis=1)
#'''
marketing_df = pd.read_csv('D:/ML with Profiles/Stanford Student Profiles/profiles___3.csv')
#marketing_df=marketing_df.drop(['Id','Class'],axis=1)
mark_array=marketing_df.values
mark_array[:, 0] = mark_array[:, 0].astype(int)
mark_array[:, 1] = mark_array[:, 1].astype(float)
mark_array[:, 2] = mark_array[:, 2].astype(int)
mark_array[:, 3] = mark_array[:, 3].astype(int)
mark_array[:, 4] = mark_array[:, 4].astype(int)
mark_array[:, 5] = mark_array[:, 5].astype(int)
mark_array[:, 6] = mark_array[:, 6].astype(int)

X = np.array(mark_array)
Y = [0]*7+[1]*242

clf = LogisticRegression(max_iter=400)
clf.fit(X, Y)
pickle.dump(clf, open('model.sav','wb'))
#'''
loaded_model = pickle.load(open('model.sav','rb'))

pred = loaded_model.predict_proba([[1480,5.0,72-30,1,1,0,1]])
if float(pred[0][1])> 0.9:
    print(((float(pred[0][1]))-0.9)*1000)
else:
    print(pred[0][1]-0.6)
#1: asian, 2: black, 3: Hispanic, 4: Others, 5: White
