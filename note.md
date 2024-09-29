### 数据集的准备工作

---

1. 获取数据：优先找数据集（阿里天池等等）；实在不行再爬虫（一般数据集不行的感觉不是很火热的图片爬虫也不凑效）；本次数据集获取来源[PlantVillage阿里天池云数据集](https://tianchi.aliyun.com/dataset/160100)（1+1知识点）
2. 将获取的数据做成完整的训练集：理解数据集组织的结构，比如YOLO组织的结构为；
![yolov8数据集组织形式](D:\life\grade_two_2\yolo8\note.assets\yolov8数据集组织结构.png)
将作为数据集的文件移动到数据集下面，用的os，shutil，re三个库