import os
import re
import shutil


def append_data_to_total_dataset(counter,src_dir,dst_dir):
    file_names=os.listdir(src_dir)
    print(file_names[0])
    for file_name in file_names:
        match=re.match(r'image \((\d+)\)',file_name)
        if match:
            #print("hhh")
            original_number=int(match.group(1))
            new_number=original_number+counter
            new_file_name=f"image({new_number}).jpg"
            shutil.copy(os.path.join(src_dir,file_name),os.path.join(dst_dir,new_file_name))

src_dir="/mnt/d/life/grade_two_2/yolo8/Plant_leave_diseases_dataset_without_augmentation/Tomato___Late_blight"
dst_dir="/mnt/d/life/grade_two_2/yolo8/plant_dataset/coco128/images/train"
append_data_to_total_dataset(1000,src_dir,dst_dir)
