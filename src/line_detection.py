import cv2
import numpy as np
import config

def get_hough_lines(edges_image):
    """
    Applies Hough Transform to find lines in an edge image.
    """
    lines = cv2.HoughLinesP(edges_image, 
                            config.HOUGH_RHO, 
                            config.HOUGH_THETA, 
                            config.HOUGH_THRESHOLD, 
                            np.array([]),
                            minLineLength=config.HOUGH_MIN_LINE_LEN, 
                            maxLineGap=config.HOUGH_MAX_LINE_GAP)
    return lines

def average_slope_intercept(image, lines):
    """
    Combines line segments into a single left and a single right lane line.
    """
    left_fit = []
    right_fit = []
    
    if lines is None:
        return None

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        # Ignore perfectly vertical or horizontal lines to avoid div by zero or extreme outliers
        if x1 == x2 or y1 == y2:
            continue
            
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        
        # Lanes normally have specific slopes depending on camera angle
        if slope < -0.3: # Left lane
            left_fit.append((slope, intercept))
        elif slope > 0.3: # Right lane
            right_fit.append((slope, intercept))
            
    # Calculate the average slope and intercept for left and right lines
    if len(left_fit) > 0:
        left_fit_average = np.average(left_fit, axis=0)
        left_line = make_coordinates(image, left_fit_average)
    else:
        left_line = None
        
    if len(right_fit) > 0:
        right_fit_average = np.average(right_fit, axis=0)
        right_line = make_coordinates(image, right_fit_average)
    else:
        right_line = None
        
    return [left_line, right_line]

def make_coordinates(image, line_parameters):
    """
    Creates x, y coordinates for a line given its slope and intercept.
    """
    slope, intercept = line_parameters
    y1 = image.shape[0] # Bottom of the image
    y2 = int(y1 * 0.6)  # Slightly lower than the middle
    
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    
    return np.array([x1, y1, x2, y2])

def draw_lines(image, lines):
    """
    Draws lines on a blank image of the same size as the input image.
    """
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            if line is not None:
                x1, y1, x2, y2 = line
                cv2.line(line_image, (x1, y1), (x2, y2), config.LANE_COLOR, config.LANE_THICKNESS)
    return line_image
