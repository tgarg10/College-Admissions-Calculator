import numpy as np
import pandas as pd

from kmodes.kprototypes import KPrototypes

#marketing_df = pd.read_csv('https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/marketing_cva_f.csv')
#marketing_df=marketing_df.drop(['Customer','Vehicle_Class','avg_vehicle_age','months_last_claim','Total_Claim_Amount'],axis=1)

marketing_df = pd.read_csv('profiles_sorted_2.csv')
marketing_df=marketing_df.drop(['Id','Class'],axis=1)
mark_array=marketing_df.values

mark_array[:, 0] = mark_array[:, 0].astype(float)
mark_array[:, 1] = mark_array[:, 1].astype(float)
#mark_array[:, 2] = mark_array[:, 2].astype(float)
#mark_array[:, 6] = mark_array[:, 6].astype(float)

#print(marketing_df)

kproto = KPrototypes(n_clusters=3, verbose=2,max_iter=20)
clusters = kproto.fit_predict(mark_array, categorical=[2, 3, 4, 5])

print(kproto.cluster_centroids_)

cluster_dict=[]
for c in clusters:
    cluster_dict.append(c)

marketing_df['cluster']=cluster_dict

print(marketing_df[marketing_df['cluster']== 0].head(10))

print(marketing_df[marketing_df['cluster']== 1].head(10))

print(marketing_df[marketing_df['cluster']== 2].head(10))

#print(marketing_df)
