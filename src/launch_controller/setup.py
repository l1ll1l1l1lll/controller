from setuptools import setup
import os
from glob import glob

package_name = 'launch_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # 安装 package.xml
        (os.path.join('share', package_name), ['package.xml']),
        # 安装 resource 文件夹中的标记文件
        (os.path.join('share', 'ament_index', 'resource_index', 'packages'),
         [os.path.join('resource', package_name)]),
        # 安装 launch 文件夹中的所有 .py 文件
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A package to demonstrate ROS 2 launch files',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
