import os

def clean_filenames(folder_path):
    for filename in os.listdir(folder_path):
        new_name = filename.replace("_", "").replace(" ", "")
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        if new_name != filename:
            if os.path.exists(new_path):
                print(f"Skipping: {new_name} already exists.")
                continue

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

# Set your folder path here
folder = "C:/Users/Garin/Downloads/Glitch_gaze_2"
clean_filenames(folder)

