# Lane Detection System

## Overview
This project implements a Lane Detection System using Computer Vision techniques. It is designed to process video feeds (or static images) from a vehicle's dashcam and identify lane markings in real-time. This project serves as a foundational module for Advanced Driver Assistance Systems (ADAS) and Autonomous Vehicles.

This project was built for the Flipped Course Evaluation of the Computer Vision subject.

## Features
- **Real-time Video Processing:** Highlights lane boundaries on pre-recorded video feeds.
- **Image Processing:** Supports processing of single dashboard images.
- **Classic CV Pipeline:** Utilizes Grayscale conversion, Gaussian Blur, Canny Edge Detection, and Hough Line Transform.
- **Configurable:** All image processing parameters (thresholds, kernel sizes) are easily accessible in `config.py`.
- **Modular Design:** The pipeline is separated into distinct, testable modules.

## Technologies and Tools Used
- **Python 3.x:** Core programming language.
- **OpenCV (`opencv-python`):** Used for all image and video processing tasks.
- **NumPy (`numpy`):** Used for matrix/array operations and calculating mathematical averages for line slopes.
- **Unittest:** Standard Python library used for automated testing.

## Steps to Install & Run the Project

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd CV_project
```

### 2. Set up the environment
It is recommended to use a virtual environment.
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
To process a video file:
```bash
python main.py --input sample_video.mp4 --output output_video.mp4
```

To process a static image:
```bash
python main.py --input sample_image.jpg --output output_image.jpg --image
```

## Instructions for Testing
This project includes automated unit tests to ensure the image processing pipeline functions correctly.

To run the tests, execute the following command from the root directory:
```bash
python -m unittest discover tests
```
You should see an output indicating `OK` if all tests pass.

## Screenshots
*(Optional: Add your screenshots here after running the project on your own data. For example:)*
- **Original Frame vs Processed Frame**
- **Edge Detection Output**
