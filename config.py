# Configuration Parameters for Lane Detection System

# Image processing configuration
GAUSSIAN_KERNEL_SIZE = 5

# Canny Edge Detection
CANNY_LOW_THRESHOLD = 50
CANNY_HIGH_THRESHOLD = 150

# Hough Line Transform
HOUGH_RHO = 2
HOUGH_THETA = 3.141592653589793 / 180  # np.pi / 180
HOUGH_THRESHOLD = 50
HOUGH_MIN_LINE_LEN = 40
HOUGH_MAX_LINE_GAP = 100

# Color definitions (B, G, R)
LANE_COLOR = (0, 255, 0)
LANE_THICKNESS = 10
