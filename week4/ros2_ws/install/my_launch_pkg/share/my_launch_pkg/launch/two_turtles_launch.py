from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        # Start turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Teleop
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            prefix='xterm -e'
        ),

        # Spawn second turtle using service call
        ExecuteProcess(
            cmd=[
                'ros2', 'service', 'call', '/spawn',
                'turtlesim/srv/Spawn',
                "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
            ],
            output='screen'
        ),
    ])
