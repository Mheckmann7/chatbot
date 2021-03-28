# import sys
# import numpy as np
# import matplotlib

# print(sys.version)
# print(np.__version__)
# print('matplot', matplotlib.__version__)
inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

output = inputs[0]*weights[0] + inputs[1] * \
    weights[1] + inputs[2]*weights[2] + bias
print(output)
