import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        sum = 0
        for val in z: 
            sum += np.exp(val - max(z))
        
        ans = np.exp(z - max(z)) / sum
        return np.round(ans, 4)
