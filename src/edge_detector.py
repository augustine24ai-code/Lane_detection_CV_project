import cv2
import config

def apply_canny_edge_detection(image):
    """
    Applies Gaussian Blur and Canny Edge Detection to the input image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (config.GAUSSIAN_KERNEL_SIZE, config.GAUSSIAN_KERNEL_SIZE), 0)
    edges = cv2.Canny(blur, config.CANNY_LOW_THRESHOLD, config.CANNY_HIGH_THRESHOLD)
    return edges
