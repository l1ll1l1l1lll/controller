import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo, IncludeLaunchDescription, SetEnvironmentVariable
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():

    # 通过 SetEnvironmentVariable 设置环境变量
    return LaunchDescription([
        LogInfo(condition=None, msg="Launching multiple nodes..."),
        
        
	SetEnvironmentVariable('RMW_IMPLEMENTATION', 'rmw_cyclonedds_cpp'),
        # Launch joy node for joystick input
        Node(
            package='joy',
            executable='joy_node',
            output='screen'
        ),

        # Launch Xbox joystick node
        Node(
            package='my_xbox_joystick',
            executable='xbox_joystick',
            output='screen'
        ),
        
    ])

