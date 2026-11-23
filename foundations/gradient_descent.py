class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        x = init
        for _ in range(iterations):
            # y = x^2
            g = 2 * x 
            # loss = y - 
            x = x - learning_rate * g
        
        return round(x,5)
