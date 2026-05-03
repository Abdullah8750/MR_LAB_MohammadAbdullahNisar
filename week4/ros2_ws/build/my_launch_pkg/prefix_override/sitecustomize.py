import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/man6/Desktop/week4/ros2_ws/install/my_launch_pkg'
