import numpy as np
def translate_object(points, tx, ty):
    dis=np.array([tx,ty])
    translated_points=points+dis
    return translated_points
