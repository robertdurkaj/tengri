import sys
import os

# add project dir to sys.path
# allow testing without installing modules to site-packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
