from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim',
            output='screen',
            parameters=[{
                'background_r': 69,
                'background_g': 86,
                'background_b': 255,
            }],
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim',
            output='screen',
            parameters=[{
                'background_r': 255,
                'background_g': 100,
                'background_b': 100,
            }],
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtle_teleop_key',
            name='teleop',
            output='screen',
            emulate_tty=True,
            prefix='gnome-terminal --',
        ),
        TimerAction(
            period=1.0,
            actions=[
                Node(
                    package='turtlesim',
                    executable='mimic',
                    name='mimic',
                    output='screen',
                    remappings=[
                        ('/input/pose', '/turtlesim1/turtle1/pose'),
                        ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
                    ],
                )
            ],
        ),
    ])