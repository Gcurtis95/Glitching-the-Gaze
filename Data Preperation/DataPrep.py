import os

def rename_files_in_folder(folder_path, base_name="image", start_count=1, zero_padding=4):
    files = sorted([
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')
    ])

    for idx, filename in enumerate(files, start=start_count):
        ext = os.path.splitext(filename)[1]  # Get the file extension
        new_name = f"{base_name}_{str(idx).zfill(zero_padding)}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
folder = "./birme-615x768"  # Replace with your folder path
rename_files_in_folder(folder, base_name="GLITCHINGTHEGAZE")