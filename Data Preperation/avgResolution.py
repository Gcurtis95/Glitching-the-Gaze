import os
from PIL import Image
import statistics

def calculate_median_resolution(folder_path):
    widths = []
    heights = []
    pixel_counts = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    widths.append(width)
                    heights.append(height)
                    pixel_counts.append(width * height)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if widths:
        median_width = statistics.median(widths)
        median_height = statistics.median(heights)
        median_pixels = statistics.median(pixel_counts)
        print(f"Median resolution: {median_width}x{median_height} ({median_pixels} pixels)")
    else:
        print("No valid images found in the folder.")

# Example usage
folder_path = "/Users/Garin/Downloads/Glitch_gaze_2/landscape"
calculate_median_resolution(folder_path)
