# Strix-Interceptor

The Strix Interceptor Drone is an open-source, multi-functional UAV designed to intercept other drones and defend against anti-drone RF systems. Features Pixhawk autonomous flight, matrix motor config, and multi RF spoofing capabilities.

## Features

- Intercepts other drones in flight
- Autonomous flight using the Pixhawk flight controller
- Multi RF spoofing against anti-drone RF systems
- Matrix motor configuration for improved stability and maneuverability
- Open-source design and code

## Getting Started

To get started with the Strix drone, follow these steps:

1. Clone the Strix repository to your local machine.
2. Install the required dependencies, including the ArduPilot libraries and OpenCV.
3. Connect the Strix drone to your computer using a USB cable.
4. Build and upload the Strix code to the drone using the ArduPilot IDE.
5. Connect the drone to a radio control (RC) transmitter for manual control, or use the autonomous flight capabilities.

### Dependencies

To build and run the Strix code, you'll need to have the following libraries installed:

- [ArduPilot](https://github.com/ArduPilot/ardupilot)
- [OpenCV](https://opencv.org/releases/)

## Contributing

If you'd like to contribute to the Strix project, please follow these steps:

1. Fork the Strix repository to your own account.
2. Make any desired changes or additions to the code.
3. Submit a pull request to the main Strix repository.
4. The Strix development team will review your changes and merge them if they are accepted.

## Usage

To use the Strix drone, you will need to run the `strix_swarm_node.py` ROS node, which handles communication with the drone and coordinates its actions with the rest of the swarm. You can run the node using the following command:

rosrun strix_swarm_node strix_swarm_node.py


The Strix drone is also designed to work seamlessly with other UAVs in an ROS swarm. To coordinate the Strix drone with an ROS swarm, you can use the ROS Navigation Stack to perform localization, path planning, and obstacle avoidance. You can also use the ROS topics and messages provided by the `strix_swarm_node` node to coordinate the actions of the individual drones in the swarm.

## Docker

To make it easier to deploy the Strix drone to the cloud, we've provided a Dockerfile that packages the `strix_swarm_node.py` node into a Docker container. You can use the following commands to build and push the Docker image to a registry like Docker Hub:

mkdir build
cd build
cmake ..
make build_and_push

This will build the Docker image using the Dockerfile, tag it with the specified name and version, and push it to the Docker Hub registry.

## License

The Strix drone is released under the terms of the MIT License, a free and open-source software license. You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions of the license. See the LICENSE file for details.

We encourage contributions and collaborations to improve the Strix drone, and welcome feedback from the community.