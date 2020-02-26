import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy import stats

def scale_numeric(X,y, test_set=False):
    X_num = X.select_dtypes(exclude='object')
    
    ss = StandardScaler()
    X_num_stand = pd.DataFrame(ss.fit_transform(X_num))
    X_num_stand.set_index(X.index, inplace=True)
    X_num_stand.columns = X_num.columns
    
    X_num_stand = X_num_stand[(np.abs(X_num_stand) 
                              < 2.5).all(axis=1)]
    
    y = y.iloc[X_num_stand.index]

    return X_num_stand, y
