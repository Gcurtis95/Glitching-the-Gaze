import os
from PIL import Image

def find_highest_resolution_image(folder_path):
    highest_resolution = 0
    highest_image = None

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    resolution = width * height
                    if resolution > highest_resolution:
                        highest_resolution = resolution
                        highest_image = (filename, width, height)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if highest_image:
        print(f"Highest resolution image: {highest_image[0]} ({highest_image[1]}x{highest_image[2]})")
    else:
        print("No valid images found in the folder.")

# Example usage
folder_path = "/Users/Garin/Downloads/Glitch_gaze_2/landscape"
find_highest_resolution_image(folder_path)
