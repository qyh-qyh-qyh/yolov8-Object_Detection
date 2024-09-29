import os
import random
import shutil

def move_image(src_dir, dst_dir):
    image_files=os.listdir(src_dir)
    rate=0.2
    num_images=len(image_files)
    pick_number=int(rate*num_images)
    sample=random.sample(image_files,pick_number)
    for i in sample:
        shutil.move(os.path.join(src_dir,i),os.path.join(dst_dir,i))

def move_labels(file_list,src_dir,dst_dir):
    for file in file_list:
        if file.endswith('.JPG'):
            file_name=file[:-4]+".txt"
            shutil.move(os.path.join(src_dir,file_name),os.path.join(dst_dir,file_name))

src_dir_images="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/images/train"
dst_dir_images="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/images/val"
move_image(src_dir_images,dst_dir_images)
file_list=os.listdir(dst_dir_images)
src_dir_labels="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/labels/train"
dst_dir_labels="/mnt/d/life/grade_two_2/yolo8/plant_dataset_for_auto_tag/coco128/labels/val"
move_labels(file_list,src_dir_labels,dst_dir_labels)