import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    # acc=y_true-y_pred
    # correct=acc.count(0)
    # return correct/len(y_true)
    evaluation=(y_true==y_pred)
    return np.sum(evaluation)/len(y_true)
    pass