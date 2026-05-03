import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class Task3Follower(Node):
    def __init__(self):
        super().__init__('task3_follower')

        self.turtle1_pose = None
        self.turtle2_pose = None

        # Subscribers
        self.create_subscription(Pose, '/turtle1/pose', self.pose1_callback, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.pose2_callback, 10)

        # Publisher
        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

    def pose1_callback(self, msg):
        self.turtle1_pose = msg
        self.move_turtle()

    def pose2_callback(self, msg):
        self.turtle2_pose = msg
        self.move_turtle()

    def move_turtle(self):
        if self.turtle1_pose is None or self.turtle2_pose is None:
            return

        dx = self.turtle1_pose.x - self.turtle2_pose.x
        dy = self.turtle1_pose.y - self.turtle2_pose.y

        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        angle_diff = angle - self.turtle2_pose.theta
        angle_diff = math.atan2(math.sin(angle_diff), math.cos(angle_diff))

        msg = Twist()
        msg.linear.x = 2.0 * distance
        msg.angular.z = 4.0 * angle_diff

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Task3Follower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
