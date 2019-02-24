import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def scale_data():
    # ignore the datetime column
    filename = 'occupancy_data/datatraining.txt'
    df_training = pd.read_csv(filename)
    X_train = df_training.iloc[:,1:6].values
    scaler = StandardScaler()
    scaler.fit(X_train)
    return scaler


