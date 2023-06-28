#!/usr/bin/env python

import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int32
from .robotiq_gripper import *
from gripper_srv.srv import GripperService

class HandEGripper(Node):
    def __init__(self):
        super().__init__('hand_e_gripper_node')
        # get the IP
        self.declare_parameter('robot_ip')
        ip = self.get_parameter('robot_ip')
        # initialize the gripper
        self.gripper = RobotiqGripper()
        self.get_logger().info("Connecting to the gripper.....")
        self.gripper.connect(ip.value, 63352)
        self.get_logger().info("Activating the gripper.....")
        self.gripper.activate(auto_calibrate=False)
        # set up server
        self.gripper_server = self.create_service(GripperService, 'gripper_service', self.serverCallback)

        self.get_logger().info("Gripper ready to receive service request...")
    
    def serverCallback(self, request, response):
        pos = request.position
        speed = request.speed
        force = request.force
        if speed > 255 or speed <=0:
            response.response = 'invalid speed value. Valid in range (0,255]'
            return response
        if force > 255 or force <=0:
            response.response = 'invalid force value. Valid in range (0,255]'
            return response
        if pos > 255 or pos < 0:
            response.response = 'invalid position value. Valid in range (0,255]'
            return response

        self.get_logger().info("moving the gripper. positino = {}, speed={}, force={}".format(pos, speed, force))
        self.gripper.move_and_wait_for_pos(pos, speed, force)
        response.response = 'Done'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = HandEGripper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()