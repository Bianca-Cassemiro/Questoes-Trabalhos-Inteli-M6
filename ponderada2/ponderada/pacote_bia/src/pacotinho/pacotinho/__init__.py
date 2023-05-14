import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

dist = 0.3

route = [
    [2.0, 1.0],
    [1.5, 1.0],
    [2.5, 2.5],
    [2.0, 3.5],
    [1.0, 3.0]
]

class TurtleController(Node):

    def __init__(self, time=0.05):

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, '/odom', self.pose_callback, 10)
        self.control_timer = self.create_timer(timer_period_sec=time, callback=self.control_callback)

        super().__init__('turtle_controller')
        self.pose_index = 1

        self.actualpose_x = route[self.pose_index - 1][0]
        self.actualpose_y = route[self.pose_index - 1][1]

        self.setpoint_x = route[self.pose_index][0]
        self.setpoint_y = route[self.pose_index][1]
        print(f'Starting point: x={self.actualpose_x}, y={self.actualpose_y}')

        

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        _, _, self.theta = euler_from_quaternion([
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w
        ])
        self.actualpose_x = x
        self.actualpose_y = y
        self.get_logger().info(f"The robot is at x={round(x, 2)}, y={round(y, 2)}, theta={round(math.degrees(self.theta), 2)}")

    def control_callback(self):
        msg = Twist()
        self.setpoint_x = route[self.pose_index][0]
        self.setpoint_y = route[self.pose_index][1]

        dist_x = self.setpoint_x - self.actualpose_x
        dist_y = self.setpoint_y - self.actualpose_y
        angle_needed = math.atan2(dist_y, dist_x)
        theta_diff = angle_needed - self.theta
        

        if abs(dist_x) < dist and abs(dist_y) < dist:
            self.pose_index += 1

        if abs(theta_diff) > dist - 0.05:
            msg.linear.x = 0.0
            msg.angular.z = 0.2 if theta_diff > 0 else -0.2
        elif abs(dist_x) > dist:
            msg.linear.x = 0.2
        print(f"self.pose_index={self.pose_index}, x_setpoint={route[self.pose_index][0]}, y_setpoint={route[self.pose_index][1]}")

        if self.pose_index == len(route) - 2:
            msg.linear.x = 0.0
            msg.linear.y = 0
