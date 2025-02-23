import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy  # 直接复用 Joy 消息类型
from std_srvs.srv import Trigger  # 服务

class XboxJoystickNode(Node):
    def __init__(self):
        super().__init__('xbox_joystick_node')

        # 订阅 `/joy` 话题（接收手柄数据）
        self.subscription = self.create_subscription(
            Joy,
            'joy',  # 监听 /joy 话题
            self.joy_callback,
            10
        )

        # **发布 `/xbox_joy_state` 话题**
        self.publisher = self.create_publisher(Joy, 'xbox_joy_state', 10)

        # 创建 `/get_joy_state` 服务
        self.srv = self.create_service(Trigger, 'get_joy_state', self.get_joy_state_callback)
        
        self.latest_joy_data = None

    def joy_callback(self, msg: Joy):
        """ 订阅 /joy 并发布到 /xbox_joy_state """
        self.latest_joy_data = msg
        self.get_logger().info(f'Received Joy Data: Buttons: {msg.buttons}, Axes: {msg.axes}')

        # **发布数据**
        self.publisher.publish(msg)

    def get_joy_state_callback(self, request, response):
        """ 提供服务返回当前手柄状态 """
        if self.latest_joy_data:
            response.success = True
            response.message = f'Buttons: {self.latest_joy_data.buttons}, Axes: {self.latest_joy_data.axes}'
        else:
            response.success = False
            response.message = 'No Joy data received yet'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = XboxJoystickNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

