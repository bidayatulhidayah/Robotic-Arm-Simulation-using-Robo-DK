# Robotic Arm Simulation Project using Robot DK

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Components](#components)
- [Control Flow](#control-flow)
- [Video and Images](#video-and-images)
- [Libraries Required](#libraries-required)
- [Installation](#installation)
- [Modes and Commands](#modes-and-commands)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview
This mini project is dedicated to the exploration of a **6-DOF (Degrees of Freedom)** robotic arm, a sophisticated mechanism renowned for its versatility and precision in executing complex tasks. Our objective is to derive fundamental representations crucial for understanding and controlling the robotic arm's movements. The project consists of two parts: theoretical derivations and a simulation implementation using RoboDK software.

### Project Goals:
- **Forward and Inverse Kinematics**: Derive the kinematic equations for determining the position and orientation of the robotic arm.
- **Linear and Angular Velocity**: Derive the equations governing the arm’s linear and angular velocities.
- **Simulation**: Implement a simulation of the robotic arm using RoboDK, with Python integration to control the arm and perform tasks.

### Simulation Task:
The simulation task involves using the RoboDK software to make the robotic arm draw at least three letters on a board. These letters are predefined in an SVG file, converted into coordinates, and used in the Python script to control the arm's movement.

## Features
- **6-DOF Robot Arm Simulation**: A sophisticated model capable of executing a wide range of tasks with precision.
- **Real-time Kinematic Simulation**: Includes forward and inverse kinematics calculations for accurate arm control.
- **Dynamic Task Execution**: Supports the derivation and simulation of the arm’s velocities (linear and angular).
- **Python Integration**: Allows Python scripting for automated robot control in RoboDK.
- **SVG-to-Coordinates Conversion**: Converts letter drawings into robot movement commands via CSV file input.

## Components
The project is divided into two parts:
1. **Theoretical Derivations (MATLAB)**: Involves computing forward and inverse kinematics and deriving the velocity equations for the robot.
2. **RoboDK Simulation**: The simulation of the robotic arm involves generating coordinates from an SVG file and using Python code to control the arm.

### Part 1: Theoretical Derivations
- **Forward Kinematics**: Mathematical model to map joint angles to end-effector position.
- **Inverse Kinematics**: Derivation of the equations for computing joint angles from a given end-effector position.
- **Linear and Angular Velocity**: Derivation of equations governing the velocities of the robot’s joints and end-effector.

### Part 2: Simulation with RoboDK
The simulation involves the robotic arm drawing letters based on coordinates extracted from an SVG file.

## Control Flow
1. **Theoretical Derivations (MATLAB)**:
   - Compute kinematic equations (forward and inverse) and linear/angular velocities.
   
2. **Simulation Setup (RoboDK)**:
   - Convert the SVG file to points using a path-to-point converter.
   - Import the points into the Python script to control the robotic arm’s movements.
   
3. **Execution**:
   - Load the simulation in RoboDK and use the Python script to control the robot.
   - The arm will move to each point sequentially, drawing the specified letters.

## Video and Images

<img src="https://github.com/bidayatulhidayah/Robotic-Arm-Simulation-using-Robot-DK/blob/d2eb7be8a8dd83bf4331824d3fbbef5a61dccfac/Images%20and%20Video/Full%20Assembly%20in%20RoboDK.png" alt="Full Assembly in RoboDK" width="400" />
<img src="https://github.com/bidayatulhidayah/Robotic-Arm-Simulation-using-Robot-DK/blob/d2eb7be8a8dd83bf4331824d3fbbef5a61dccfac/Images%20and%20Video/Mitsubishi%20RV-7FR%20.png" alt="Mitsubishi RV-7FR " width="400" />
<img src="https://github.com/bidayatulhidayah/Robotic-Arm-Simulation-using-Robot-DK/blob/d2eb7be8a8dd83bf4331824d3fbbef5a61dccfac/Images%20and%20Video/Simulation%20RoboDK.png" alt="Simulation RoboDK" width="400" />

- [Youtube Video](https://youtu.be/DrzBRtHIL2w)

## Libraries Required
- **RoboDK Python API**: For controlling the robot and interfacing with RoboDK.
  - Install it using:
    ```bash
    pip install robodk
    ```
- **MATLAB**: For the theoretical derivations.
- **Path-to-Point Converter**: Online tool for converting SVG files into CSV points.

## Installation

### 1. **Install RoboDK**:
   - Visit the [RoboDK website](https://www.robodk.com/download) to download and install the RoboDK software.
   - Follow the instructions on the website to set up RoboDK on your computer.

### 2. **MATLAB**:
   - Install MATLAB if you haven’t already.
   - Load the provided MATLAB code for the theoretical derivations and kinematic computations.

### 3. **Python and Required Libraries**:
   - Install Python from [python.org](https://www.python.org/downloads/).
   - Install the RoboDK API using the command:
     ```bash
     pip install robodk
     ```

### 4. **Coordinate Conversion**:
   - Convert your SVG file into a CSV using an online path-to-point converter.

## Modes and Commands

- **RoboDK Interface**: 
  - **MoveJ**: Move the robotic arm to a specific target position.
  - **Render**: Turn on or off the visualization of the simulation in RoboDK.
  - **Pose Reference**: Set the reference frame for the robot’s movements.

- **Python Mode**:
  - Control the arm via the `robodk` API by specifying coordinates in the Python script.
  - The robot follows the given points sequentially and performs the task (e.g., drawing letters).

## Troubleshooting
- **Robot Not Moving**: Ensure the robot is properly selected and connected in RoboDK.
- **Incorrect Movements**: Double-check the coordinates in the CSV file for correctness and ensure the scale matches the robot’s environment.
- **Installation Issues**: If RoboDK is not installing properly, check the system requirements or reinstall the software following the installation guide.

## License
This project is open-source under the MIT License.
