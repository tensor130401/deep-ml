import numpy as np
def precision(y_true, y_pred):
    # Your code here
    TP=np.where((y_true==y_pred) & (y_pred==1),1,0)
    if np.sum(y_pred)==0:
        return 0.0
    return np.sum(TP)/np.sum(y_pred)
    pass
