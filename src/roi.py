import cv2
import numpy as np

def apply_region_of_interest(image, vertices):
    """
    Applies an image mask.
    Only keeps the region of the image defined by the polygon formed from `vertices`.
    The rest of the image is set to black.
    """
    mask = np.zeros_like(image)
    
    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(image.shape) > 2:
        channel_count = image.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def get_roi_vertices(image):
    """
    Returns the vertices for the Region of Interest based on the image size.
    Assumes camera is mounted on the dashboard and lanes are at the bottom half.
    """
    height, width = image.shape[:2]
    # These coordinates are typical for a dashboard camera.
    bottom_left = [width * 0.1, height * 0.95]
    top_left = [width * 0.45, height * 0.6]
    top_right = [width * 0.55, height * 0.6]
    bottom_right = [width * 0.9, height * 0.95]
    
    return np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
