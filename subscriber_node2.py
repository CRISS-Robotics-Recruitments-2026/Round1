import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

class Subscriber(Node):
	
	def __init__(self):
		super().__init__('subscriber')
		self.subscription = self.create_subscription(Float32, '/turtle1/distance_from_origin', self.f1, 10)
	
	def f1(self, msg):
		self.get_logger().info('Distance from origin: %f' % (msg.data))
		
def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
