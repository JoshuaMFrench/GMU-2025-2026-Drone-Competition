from pathlib import Path

import_folder = "C:/Users/conno/Python Files/Python Project/Work/Drone Competiton/Object Tracking/YOLO Files/V4 Detection/V4_YOLO_circle_detection/val/images" # val images
pulling_folder = "C:/Users/conno/Python Files/Python Project/Work/Drone Competiton/Object Tracking/YOLO Files/V4 Detection/V4_YOLO_circle_detection/train/labels" # train labels
output_folder = "C:/Users/conno/Python Files/Python Project/Work/Drone Competiton/Object Tracking/YOLO Files/V4 Detection/V4_YOLO_circle_detection/val/labels" # val labels

import_folder_path_object = Path(import_folder)
pulling_folder_path_object = Path(pulling_folder)
output_folder_path_object = Path(output_folder)

moved_files_counter = 0

for import_file_path in import_folder_path_object.iterdir():
    import_file_name = import_file_path.stem
    for pulling_file_path in pulling_folder_path_object.iterdir():
        pulling_file_name = pulling_file_path.stem
        if (pulling_file_name == import_file_name):
            pulling_file_path.rename(output_folder_path_object / pulling_file_path.name)
            print(f"Moved {pulling_file_path.name} successfully")
            moved_files_counter += 1

print(f"All {moved_files_counter} files moved")