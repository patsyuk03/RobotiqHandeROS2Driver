import os
from glob import glob
from setuptools import setup

package_name = 'robotiq_hande_ros2_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', 'gripper_srv', 'srv'), glob('srv/*.srv')),
        (os.path.join('share', 'gripper_srv', 'srv'), glob('srv/*.msg')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gurovaid',
    maintainer_email='iryna.gurova@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gripper_node = robotiq_hande_ros2_driver.gripper_node:main',
            'test = robotiq_hande_ros2_driver.test:main',
        ],
    },
)
