import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # --- TUNED FOR THE HEXAGON PILLAR ARENA ---
        self.front_threshold = 0.55   # Distance to trigger avoidance
        self.ideal_wall_dist = 0.4    # How close to stay to the wall
        self.max_linear_speed = 0.12  # Slow and steady to navigate tight gaps
        self.get_logger().info('Lidar Navigator: Arena Mode Started')

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)
        ranges = np.where(np.isfinite(ranges), ranges, 3.5)
        
        # --- TARGETED REGIONS ---
        # Narrower front cone (30 degrees total) to fit between pillars
        front = np.concatenate((ranges[0:15], ranges[345:360]))
        # Left side for wall following
        left_side = ranges[60:110]
        # Right side for emergency clearance
        right_side = ranges[250:300]
        
        front_dist = np.min(front)
        left_dist = np.min(left_side)
        right_dist = np.min(right_side)
        
        twist = Twist()

        # --- BEHAVIOR PRIORITIZATION ---
        
        # 1. OBSTACLE IN FRONT? (Turn but don't stop completely to avoid getting stuck)
        if front_dist < self.front_threshold:
            twist.linear.x = 0.04 # Keep a tiny bit of crawl to break out of "stuck" loops
            if left_dist > right_dist:
                twist.angular.z = 0.9 # Fast Turn Left
            else:
                twist.angular.z = -0.9 # Fast Turn Right
            self.get_logger().info('NAVIGATING PILLARS: Turning to clear path')

        # 2. WALL DETECTED ON LEFT? (Follow the wall)
        elif left_dist < 0.8:
            twist.linear.x = self.max_linear_speed
            # Proportional gain: Error * 1.5
            error = left_dist - self.ideal_wall_dist
            twist.angular.z = 1.5 * error 
            self.get_logger().info(f'WALL FOLLOWING: Distance {left_dist:.2f}m')

        # 3. NOTHING NEARBY? (Drive Straight)
        else:
            twist.linear.x = self.max_linear_speed
            twist.angular.z = 0.0
            self.get_logger().info('OPEN SPACE: Moving Forward')

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()