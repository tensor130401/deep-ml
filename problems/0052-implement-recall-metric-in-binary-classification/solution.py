import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    TP=np.where((y_pred==y_true)&(y_true==1),1,0)
    if np.sum(y_true)==0:
        return 0.0
    return np.sum(TP)/np.sum(y_true)
    pass
