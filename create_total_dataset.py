import os
import shutil

def copy_dataset(src_dir,dst_dir):
    #print(os.getcwd())
    #print("\n")
    #print(src_dir)
    #print(dst_dir)
    picture_name=os.listdir(src_dir)
    print(os.path.join(src_dir,picture_name[0]))
    for picture in picture_name:
        shutil.copy(os.path.join(src_dir, picture),dst_dir)

src_dir="/mnt/d/life/grade_two_2/yolo8/Plant_leave_diseases_dataset_without_augmentation/Tomato___Early_blight"
dst_dir="/mnt/d/life/grade_two_2/yolo8/plant_dataset/coco128/images/train"
copy_dataset(src_dir,dst_dir)