import os
import shutil
import re

def find_suffix_number(dir):
    suffix_list=[]
    labeled_files=os.listdir(dir)
    for file in labeled_files:
        match=re.match(r'image \((\d+)\)',file)
        if match:
            suffix_number=int(match.group(1))
            suffix_list.append(suffix_number)
    return suffix_list

def create_little_train_dataset_images(suffix_list,src_dir,dst_dir):
    all_train_files=os.listdir(src_dir)
    for file in all_train_files:
        match=re.match(r'image \((\d+)\)',file)
        if match:
            suffix_number=int(match.group(1))
            if suffix_number in suffix_list:
                shutil.move(os.path.join(src_dir,file),os.path.join(dst_dir,file))

def create_little_test_dataset_labels(suffix_list,src_dir,dst_dir):
    all_train_files=os.listdir(src_dir)
    for file in all_train_files:
        match=re.match(r'image \((\d+)\)',file)
        if match:
            suffix_number=int(match.group(1))
            if suffix_number in suffix_list:
                shutil.move(os.path.join(src_dir,file),os.path.join(dst_dir,file))

dir="/mnt/d/life/grade_two_2/yolo8/plant_dataset/coco128/labels/train"
src_dir_image="/mnt/d/life/grade_two_2/yolo8/plant_dataset/coco128/images/train"
dst_dir_image="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/images/train"
src_dir_label="/mnt/d/life/grade_two_2/yolo8/plant_dataset/coco128/labels/train"
dst_dir_label="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/labels/train"
suffix_list=find_suffix_number(dir)
create_little_train_dataset_images(suffix_list,src_dir_image,dst_dir_image)
create_little_test_dataset_labels(suffix_list,src_dir_label,dst_dir_label)