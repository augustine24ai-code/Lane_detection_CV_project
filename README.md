# Lane Detection System

A computer vision-based lane detection system built using Python and OpenCV. The project processes dashcam images and video feeds to identify and highlight lane markings.

This project was developed as part of the **Flipped Course Evaluation for the Computer Vision subject**.

---

## Overview

Lane detection is an important computer vision technique used in applications such as **Advanced Driver Assistance Systems (ADAS)** and autonomous driving.

This project uses a classic computer vision pipeline to detect lane markings from road images or video frames. The pipeline applies multiple image processing techniques, including grayscale conversion, Gaussian blurring, Canny edge detection, Region of Interest (ROI) masking, and Hough Line Transform.

The project is designed with a modular structure, making individual stages of the pipeline easier to understand, test, and modify.

---

## Features

- **Video Processing:** Highlights lane boundaries on pre-recorded video feeds.
- **Image Processing:** Supports processing of individual dashcam images.
- **Classic Computer Vision Pipeline:** Uses Grayscale Conversion, Gaussian Blur, Canny Edge Detection, and Hough Line Transform.
- **Configurable:** Image processing parameters such as thresholds and kernel sizes can be modified through `config.py`.
- **Modular Design:** The pipeline is divided into separate modules for different processing stages.
- **Testing:** Includes unit tests for the image processing pipeline.

---

## Technologies and Tools Used

- **Python 3.x** - Core programming language.
- **OpenCV** - Used for image and video processing.
- **NumPy** - Used for array operations and mathematical calculations.
- **Unittest** - Python's standard library for automated testing.

---

## Project Structure

```text
Lane-Detection_Computer-Vision/
│
├── src/
│   ├── edge_detector.py
│   ├── line_detection.py
│   ├── pipeline.py
│   └── roi.py
│
├── tests/
│   └── test_pipeline.py
│
├── config.py
├── main.py
├── requirements.txt
├── dashcam.jpg
├── processed_image.jpg
├── statement.md
├── README.md
└── .gitignore
```

---

## How the System Works

The lane detection system processes the input through several stages:

### 1. Input

The system takes a road image or video frame captured from a vehicle's dashcam.

### 2. Grayscale Conversion

The input image is converted from its original color format into grayscale. This simplifies the image and makes further processing easier.

### 3. Gaussian Blur

Gaussian Blur is applied to reduce image noise and smooth the image before detecting edges.

### 4. Canny Edge Detection

The Canny Edge Detection algorithm is used to identify important edges in the road image.

### 5. Region of Interest

A Region of Interest (ROI) is applied to focus the processing on the area of the image where lane markings are expected to appear.

### 6. Hough Line Transform

The Hough Line Transform is used to detect line segments corresponding to lane markings.

### 7. Lane Visualization

The detected lane lines are drawn over the original image to produce the final processed output.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/augustine24ai-code/Lane_detection_CV_project.git
cd Lane_detection_CV_project
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment for the project.

On Windows:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the main program using:

```bash
python main.py
```

The program processes the input and generates the lane-detected output.

---

## Example

### Input

The project includes an example dashcam image:

```text
dashcam.jpg
```

### Output

The processed image containing the detected lane markings is saved as:

```text
processed_image.jpg
```

---

## Testing

The project includes unit tests for the processing pipeline.

Run the tests using:

```bash
python -m unittest discover tests
```

---

## Configuration

Image processing parameters can be modified in:

```text
config.py
```

This allows parameters such as detection thresholds and kernel sizes to be adjusted without changing the core processing modules.

---

## Future Improvements

Some possible improvements for the project include:

- Real-time lane detection using a webcam.
- Improved detection of curved lane markings.
- Better performance under different lighting and weather conditions.
- Improved lane detection on roads with faded or partially visible markings.
- Real-time video output with continuous lane tracking.
- Integration with additional ADAS features.

---

## Author

**Augustine M Mathew**

Computer Science Engineering - Artificial Intelligence & Machine Learning

---

## License

This project was developed for academic purposes as part of the Computer Vision course evaluation.
