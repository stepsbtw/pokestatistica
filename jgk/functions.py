import numpy as np

def sturges_rule(n):
    return int(1 + 3.322 * np.log10(n))