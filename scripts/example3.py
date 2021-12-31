import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
sys.path.append(PROJECT_ROOT)

import utils
print(utils.get_length("From Example 3"))

# the what the fuck
utils.yolo(5)