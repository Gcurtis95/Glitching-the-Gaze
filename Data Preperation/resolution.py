import os
from PIL import Image

def find_lowest_resolution_image(folder_path):
    lowest_resolution = None
    lowest_image = None

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    resolution = width * height
                    if lowest_resolution is None or resolution < lowest_resolution:
                        lowest_resolution = resolution
                        lowest_image = (filename, width, height)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if lowest_image:
        print(f"Lowest resolution image: {lowest_image[0]} ({lowest_image[1]}x{lowest_image[2]})")
    else:
        print("No valid images found in the folder.")

# Example usage
folder_path = "/Users/Garin/Downloads/Glitch_gaze_2/landscape"
find_lowest_resolution_image(folder_path)
