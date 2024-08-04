# Strix Interceptor Post DEFCON31 Write Up

## Overview
The Strix Interceptor is an advanced, open-source UAV designed for drone interception and defense against anti-drone RF systems. It integrates autonomous flight capabilities, a matrix motor configuration for enhanced stability, and multiple RF spoofing features.

## Key Components
- **Pixhawk Flight Controller:** Central to autonomous flight operations.
- **Raspberry Pi/Nvidia Jetson Nano:** For processing and control.
- **HackRF One Module:** Enables RF spoofing and defense capabilities.
- **FPV or Modular Drone Platform:** Provides the physical framework for the UAV.

## Features
- **Autonomous and Manual Control:** Utilizes the Pixhawk for autonomous navigation and supports manual override.
- **ROS Integration for MAVLink:** Facilitates communication between the Pixhawk and other components.
- **Multi RF Spoofing:** Capable of mimicking various RF signals to disrupt or intercept other drones.

## Applications
The Strix Interceptor is suitable for security applications, including airspace defense and counter-drone operations. Its open-source nature allows for customization and expansion, making it versatile for various use cases.

## Project Successes
- **Successful Integration:** The Pixhawk controller interfaced well with the Raspberry Pi running DragonOS and the HackRF for SDR tools.
- **Proof of Concept:** Initial tests demonstrated successful concept validation.

## Challenges Encountered
- **Limited Flight Time:** The drone only flew for a few minutes before failing.
- **Restricted Flight Paths:** Only able to follow predetermined flight paths.
- **Unintended Disruptions:** Caused disruptions beyond the intended target area.
- **Mapping Limitations:** Code worked exclusively with Ardupilot for mapping.
- **Scalability Issues:** Difficulty in scaling the project beneficially.
- **High Costs:** Parts were too expensive for large-scale deployment.

## Technical Details
- **Interfacing and Communication:** Detailed the successful integration process, including configuration settings and communication protocols between the Pixhawk, Raspberry Pi, and HackRF.
- **Flight Control Algorithms:** Explained the algorithms used for autonomous navigation and how they were tested and refined.
- **RF Spoofing Techniques:** Described the methods and tools used for RF spoofing, including specific software and hardware configurations.
- **Safety and Compliance:** Outlined measures taken to ensure the drone operates within safety guidelines and regulatory compliance, including geofencing and fail-safe mechanisms.
- **Performance Metrics:** Provided data on flight performance, battery life, and the effectiveness of interception and spoofing capabilities.

## Future Work and Recommendations
- **Improving Flight Duration:** Research and implement ways to extend flight time, such as using more efficient power systems or lighter materials.
- **Enhanced Navigation:** Develop and integrate more advanced navigation systems that allow for dynamic and real-time path adjustments.
- **Minimizing Disruptions:** Implement more precise targeting mechanisms to reduce unintended disruptions.
- **Scalability Solutions:** Explore cost-effective alternatives for parts and materials to facilitate scaling.
- **Broader Compatibility:** Expand compatibility beyond Ardupilot for more versatile mapping and control options.
- **Upgraded Hardware:** Plan to use smaller, more usable boards like BeagleBone Blue or Black for better integration with Raspberry Pi and drone systems.
- **Swarm Capabilities:** Develop swarm features for coordinated drone operations.
- **Encrypted Communication:** Utilize a 5.8GHz connection for secure and encrypted communication.

For more detailed information and to access the project files, visit the [Strix Interceptor GitHub page](https://github.com/Lexicon121/Strix-Interceptor).
