import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/man6/Desktop/week6/ros2_ws/src/install/week6_pkg'
