"""
split_portrait_landscape.py
---------------------------
Move images (and their matching .txt files) into /portrait or /landscape
based on image orientation.

* Assumes the text file shares the same base-name as the image.
  e.g.  flower.jpg  ->  flower.txt
* Creates the destination folders if they don’t exist.
* Works only in the top-level folder (no recursion). 
  Change `os.walk` if you want it recursive.
"""

import os
import shutil
from PIL import Image   # pip install pillow

# 1) >>>> SET THIS TO YOUR SOURCE FOLDER <<<<
SOURCE_DIR = "C:/Users/Garin/Downloads/Glitch_gaze_2"

# 2) OPTIONAL: customise which image extensions to process
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

# -------------------------------------------------------------------

def ensure_dir(path: str) -> None:
    """Create folder if it doesn’t exist."""
    os.makedirs(path, exist_ok=True)

def orientation(img_path: str) -> str:
    """Return 'portrait' or 'landscape' for the given image file."""
    with Image.open(img_path) as im:
        w, h = im.size
    return "portrait" if h > w else "landscape"

def move_pair(img_path: str, dest_folder: str) -> None:
    """Move image and its matching .txt file into dest_folder."""
    ensure_dir(dest_folder)

    # Move the image itself
    shutil.move(img_path, os.path.join(dest_folder, os.path.basename(img_path)))
    print(f"Moved image     → {dest_folder}")

    # Move companion text file if it exists
    base, _ = os.path.splitext(img_path)
    txt_path = f"{base}.txt"
    if os.path.exists(txt_path):
        shutil.move(txt_path, os.path.join(dest_folder, os.path.basename(txt_path)))
        print(f"Moved text file → {dest_folder}")
    else:
        print(f"⚠️  No text file found for {os.path.basename(img_path)}")

def main() -> None:
    for entry in os.listdir(SOURCE_DIR):
        path = os.path.join(SOURCE_DIR, entry)

        if not os.path.isfile(path):
            continue  # skip subfolders

        ext = os.path.splitext(entry)[1].lower()
        if ext not in IMAGE_EXTS:
            continue  # skip non-image files

        try:
            dest = os.path.join(SOURCE_DIR, orientation(path))
            move_pair(path, dest)
        except Exception as e:
            print(f"Error processing {entry}: {e}")

if __name__ == "__main__":
    main()
