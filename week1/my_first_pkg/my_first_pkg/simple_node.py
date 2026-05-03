import rclpy
from rclpy.node import Node

class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        # Declare a parameter named 'student_name' with default empty string
        self.declare_parameter('student_name', '')

        # Get the parameter value
        student_name = self.get_parameter('student_name').get_parameter_value().string_value

        # Print based on whether parameter is set
        if student_name:
            self.get_logger().info(f'Student Name: {student_name}')
        else:
            self.get_logger().info('student_name not set')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()

    # Spin once so the node prints and exits
    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
