import unittest
import numpy as np
import cv2
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.edge_detector import apply_canny_edge_detection
from src.roi import apply_region_of_interest, get_roi_vertices
from src.pipeline import process_frame

class TestLaneDetectionPipeline(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy image (black with a white line)
        self.image = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.line(self.image, (100, 480), (300, 240), (255, 255, 255), 5)
        
    def test_edge_detection(self):
        edges = apply_canny_edge_detection(self.image)
        self.assertEqual(edges.shape, (480, 640))
        self.assertEqual(len(edges.shape), 2) # Should be single channel
        
    def test_roi(self):
        vertices = get_roi_vertices(self.image)
        # Should return an array with shape (1, 4, 2)
        self.assertEqual(vertices.shape, (1, 4, 2))
        
        edges = apply_canny_edge_detection(self.image)
        roi_edges = apply_region_of_interest(edges, vertices)
        self.assertEqual(roi_edges.shape, (480, 640))

    def test_process_frame(self):
        processed = process_frame(self.image)
        # Processed image should have same dimensions and 3 channels
        self.assertEqual(processed.shape, (480, 640, 3))

if __name__ == '__main__':
    unittest.main()
