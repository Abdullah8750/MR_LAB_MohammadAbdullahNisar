import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TriangleMover(Node):
    def __init__(self):
        super().__init__('triangle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_triangle()

    def draw_triangle(self):
        sides = 3
        linear_speed = 1.5     # forward speed
        angular_speed = 2.0    # turning speed
        side_length = 4.0      # units in turtlesim
        turn_angle = 2 * math.pi / 3  # 120 degrees

        side_duration = side_length / linear_speed
        turn_duration = turn_angle / angular_speed

        for i in range(sides):
            # Move forward
            msg = Twist()
            msg.linear.x = linear_speed
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info(f"Moving forward side {i+1}")
            time.sleep(side_duration)

            # Stop before turning
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.1)

            # Turn
            msg.linear.x = 0.0
            msg.angular.z = angular_speed
            self.publisher_.publish(msg)
            self.get_logger().info(f"Turning 120° for side {i+1}")
            time.sleep(turn_duration)

            # Stop after turn
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.1)

        self.get_logger().info("Triangle completed!")

def main(args=None):
    rclpy.init(args=args)
    node = TriangleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()