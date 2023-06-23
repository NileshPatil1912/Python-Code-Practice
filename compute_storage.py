import os
import psutil

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            file_path = os.path.join(path, f)
            try:
                total_size += os.path.getsize(file_path)
            except FileNotFoundError:
                pass
    return total_size

def display_folder_sizes(root_folder):
    for path, dirs, files in os.walk(root_folder):
        folder_size = get_folder_size(path)
        folder_name = os.path.basename(path)
        print(f"{folder_name}: {folder_size} bytes")

def display_drive_sizes():
    drives = psutil.disk_partitions(all=True)
    for drive in drives:
        drive_name = drive.device
        drive_mount_point = drive.mountpoint
        try:
            drive_size = psutil.disk_usage(drive_mount_point).total
            print(f"Drive: {drive_name}, Size: {drive_size} bytes")
            display_folder_sizes(drive_mount_point)
        except FileNotFoundError:
            print(f"Drive: {drive_name} cannot be accessed.")

# Example usage
display_drive_sizes()
