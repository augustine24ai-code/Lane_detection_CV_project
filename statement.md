# Project Statement: Lane Detection System

## Problem Statement
Autonomous and semi-autonomous driving systems require a robust understanding of their environment to navigate safely. One of the most fundamental tasks for an autonomous vehicle is to identify lane boundaries on the road. This ensures the vehicle remains within its designated lane and avoids collisions. Current systems need to process visual data in real-time under varying conditions. The objective of this project is to develop a Computer Vision-based Lane Detection System that accurately identifies and highlights lane boundaries from a dashcam video feed in real-time.

## Scope of the Project
This project focuses on identifying visible lane markings (both solid and dashed) on standard roads and highways during relatively clear weather conditions. 

The scope includes:
1. Processing pre-recorded video files or static images.
2. Enhancing visual features using image processing techniques like Gaussian Blur and Canny Edge Detection.
3. Isolating the road area using Region of Interest (ROI) masking.
4. Extracting and drawing lane lines using the Hough Line Transform.

The scope excludes:
- Night-time lane detection without adequate street lighting.
- Handling extreme weather conditions (heavy snow, fog).
- Complex curve detection (currently optimized for straight or slightly curved lanes using linear approximations).

## Target Users
- **Automotive Engineers:** Can use this as a foundational module for Advanced Driver Assistance Systems (ADAS).
- **Computer Vision Students/Researchers:** Can use this repository to understand the practical applications of classic computer vision algorithms (Hough Transform, Canny Edge Detection).
- **Hobbyists:** Can deploy this script to process their own dashcam footage for analytics.

## High-level Features
1. **Real-time Video Processing:** Processes dashcam video feeds frame-by-frame and outputs a video with highlighted lane boundaries.
2. **Modular Computer Vision Pipeline:** Code is broken down into distinct stages (edge detection, ROI, line extrapolation) for easy maintenance and tweaking.
3. **Configurable Thresholds:** Easily adjust Canny Edge Detection and Hough Transform parameters via a central configuration file (`config.py`).
4. **Image & Video Support:** Includes CLI options to process either a static image or a video stream.
