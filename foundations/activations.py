import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        ans = []
        for x in z: 
            temp = 1 / (1 + np.exp(-x))
            ans.append(round(temp, 5))
        return ans

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        ans = []
        for x in z: 
            ans.append(float(round(max(0, x), 5)))
        return ans
        
