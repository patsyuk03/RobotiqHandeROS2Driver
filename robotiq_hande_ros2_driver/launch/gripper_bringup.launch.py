from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = LaunchDescription()  
    
    ld.add_action(DeclareLaunchArgument("robot_ip", default_value="xxx.xxx.x.xxx"))
    robot_ip = LaunchConfiguration("robot_ip")

    ld.add_action(Node(
        package="robotiq_hande_ros2_driver",
        executable="gripper_node",
        output="screen",
        parameters=[{"robot_ip": robot_ip}],   
    ))

    return ld