from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'week6_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Register the launch folder so ROS can find launch files 
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='man6',
    maintainer_email='abdullahnisar1122@gmail.com',
    description='MCT-454L Mobile Robotics Lab 6 - Lidar Navigation',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # Link the command to your specific file [cite: 151, 239]
            'lidar_navigator = week6_pkg.initial_code:main',
        ],
    },
)
