import argparse
import cv2
import sys
import os
from src.pipeline import process_frame

def process_video(input_path, output_path):
    """
    Processes a video file frame by frame.
    """
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return

    # Get video properties for output
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print(f"Processing video: {input_path}")
    while cap.isOpened():
        ret, frame = cap.retrive() if hasattr(cap, 'retrive') else cap.read()
        if not ret:
            break
        
        # Process the frame
        processed_frame = process_frame(frame)
        
        # Write to output video
        out.write(processed_frame)
        
        # Display the frame (optional, uncomment to see while processing)
        # cv2.imshow('Lane Detection', processed_frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Output saved to: {output_path}")

def process_image(input_path, output_path):
    """
    Processes a single image file.
    """
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Could not read image {input_path}")
        return
        
    print(f"Processing image: {input_path}")
    processed_image = process_frame(image)
    cv2.imwrite(output_path, processed_image)
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lane Detection System")
    parser.add_argument("--input", required=True, help="Path to input video or image")
    parser.add_argument("--output", default="output.mp4", help="Path to save output video or image")
    parser.add_argument("--image", action="store_true", help="Set this flag if the input is an image")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        sys.exit(1)
        
    if args.image:
        # If output wasn't specified but input is image, change default output extension
        if args.output == "output.mp4":
            args.output = "output.jpg"
        process_image(args.input, args.output)
    else:
        process_video(args.input, args.output)
