#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from gripper_srv.srv import GripperService

def main(args=None):
    rclpy.init(args=args)
    node = Node('gripper_test_node')

    ## using ROS service
    node.get_logger().info("using service")
    gripper_srv = node.create_client(GripperService, 'gripper_service')
    while not gripper_srv.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')
    req = GripperService.Request()

    # open gripper
    req.position = 0
    req.speed = 255
    req.force = 255
    resp = gripper_srv.call_async(req)
    # close gripper
    req.position = 255
    req.speed = 255
    req.force = 255
    resp = gripper_srv.call_async(req)
    # open gripper small speed
    req.position = 0
    req.speed = 55
    req.force = 255
    resp = gripper_srv.call_async(req)
    # close gripper small speed
    req.position = 255
    req.speed = 55
    req.force = 255
    resp = gripper_srv.call_async(req)
    # open gripper small speed and force 
    req.position = 100
    req.speed = 5
    req.force = 5
    resp = gripper_srv.call_async(req)
    # close gripper small speed and force
    req.position = 150
    req.speed = 5
    req.force = 5
    resp = gripper_srv.call_async(req)

    rclpy.spin_until_future_complete(node, resp)
    rclpy.shutdown()

if __name__ == '__main__':
    main()