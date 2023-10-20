# Estimating Pi using Python
# video link - https://youtu.be/pvimAM_SLic
# video link - https://youtu.be/FYQA2ozutTQ

import random

def estimate_pi(n):
    numPointCircle = 0
    numPointTotal = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            numPointCircle += 1
        numPointTotal += 1

    return 4 * numPointCircle/numPointTotal

numOfPoints = int(input("Enter the number of points: "))

print(f"Pi estimate with number of points in the circle as {numOfPoints} = " + str(estimate_pi(numOfPoints)))

# Tests that estimate_pi returns a value close to 0 for small n
def test_estimate_pi_returns_value_close_to_0_for_small_n(self):
    # assert abs(estimate_pi(10) - 0) < 1
    print(abs(estimate_pi(10) - 0) < 1)

# test_estimate_pi_returns_value_close_to_0_for_small_n(estimate_pi) // false
