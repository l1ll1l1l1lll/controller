from setuptools import setup

package_name = 'my_xbox_joystick'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='y',
    maintainer_email='Yuhao_cao@Outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'xbox_joystick = my_xbox_joystick.xbox_joystick_node:main',
        ],
    },
)
