import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.publisher = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)

    def listener_callback(self, msg):
        self.get_logger().info('Turtle is at: x=%f, y=%f' % (msg.x, msg.y))
        
        distance = (msg.x**2 + msg.y**2)**0.5
        
        dist_msg = Float32()
        dist_msg.data = distance
        self.publisher.publish(dist_msg)
        
        self.get_logger().info('Publishing Distance: %f' % dist_msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
