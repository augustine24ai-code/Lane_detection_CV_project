import cv2
import sys
import os

# Add parent directory to path to allow imports when running directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.edge_detector import apply_canny_edge_detection
from src.roi import apply_region_of_interest, get_roi_vertices
from src.line_detection import get_hough_lines, average_slope_intercept, draw_lines

def process_frame(frame):
    """
    Complete pipeline to process a single frame for lane detection.
    """
    # 1. Edge Detection
    edges = apply_canny_edge_detection(frame)
    
    # 2. Region of Interest Selection
    vertices = get_roi_vertices(frame)
    roi_edges = apply_region_of_interest(edges, vertices)
    
    # 3. Line Detection
    hough_lines = get_hough_lines(roi_edges)
    lane_lines = average_slope_intercept(frame, hough_lines)
    
    # 4. Draw Lines and Combine with Original Frame
    line_image = draw_lines(frame, lane_lines)
    final_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    
    return final_image
