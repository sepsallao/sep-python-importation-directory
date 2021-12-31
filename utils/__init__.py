# from length import get_length
# from lower import to_lower
# from upper import to_upper

# Relative Imports (not recomended): Specify the path realtive to the path of the calling script.

# from .upper import to_upper
# from .lower import to_lower
# from .length import get_length

# We use the dot notation( . or ..) in specifying relative imports. 
# The single dot before lower refers to the same directory as the one from which the import is called. 
# This can be visualized as importing to_lower() from ./lower.py. 
# Similarly, double dots before a module name means moving up two levels from the current level.



# Absolute imports (better choice): specify the absolute path of the imported module from the project 
# root (or any other dir which sys.path has access to).

from utils.length import get_length
from utils.upper import to_upper
from utils.lower import to_lower

from scripts.example1 import yolo