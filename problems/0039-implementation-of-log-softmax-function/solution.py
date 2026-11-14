import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    prob=np.log(np.exp(scores)/np.sum(np.exp(scores)))
    return prob
    pass