from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Starts the Turtlesim Simulator
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # Starts the Teleop Key node for control
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e' # Opens teleop in a separate window so you can type
        ),
        # Starts rqt_plot specifically for Task 4
        Node(
            package='rqt_plot',
            executable='rqt_plot',
            name='plot',
            arguments=['/turtle1/cmd_vel/linear/x', '/turtle1/cmd_vel/angular/z']
        )
    ])
