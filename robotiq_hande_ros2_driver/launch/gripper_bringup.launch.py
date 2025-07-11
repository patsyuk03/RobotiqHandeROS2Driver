from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    # Declare both IP arguments
    ld.add_action(DeclareLaunchArgument("left_gripper_ip", default_value="192.168.0.120"))
    ld.add_action(DeclareLaunchArgument("right_gripper_ip", default_value="192.168.0.124"))

    gripper_1 = LaunchConfiguration("left_gripper_ip")
    gripper_2 = LaunchConfiguration("right_gripper_ip")

    # Launch left gripper node
    ld.add_action(Node(
        package="robotiq_hande_ros2_driver",
        executable="gripper_node",
        name="gripper_1",
        namespace="gripper_1",
        output="screen",
        parameters=[{"robot_ip": gripper_1}],
    ))

    # Launch right gripper node
    ld.add_action(Node(
        package="robotiq_hande_ros2_driver",
        executable="gripper_node",
        name="gripper_2",
        namespace="gripper_2",
        output="screen",
        parameters=[{"robot_ip": gripper_2}],
    ))

    return ld
