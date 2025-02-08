class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        """
        derivative x^2 = 2x

        x = x - learning_rate * derivative
        """
        if iterations == 0:
            return init
    
        for i in range(iterations):
            init = init - learning_rate * 2 * init

        return round(init, 5)