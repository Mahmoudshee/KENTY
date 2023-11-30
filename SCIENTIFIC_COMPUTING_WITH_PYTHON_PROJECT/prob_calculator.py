import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if drawn balls match the expected_balls
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
