from tuning_module import tune_yolo

# กำหนดค่า config
pretrained = "yolo11n.pt"
data_yaml = "data.yaml"
output_dir = "yolo_tuning_results1"

img_sizes = [416, 640]
learning_rates = [0.001, 0.0005]
batch_sizes = [8, 16]
epochs = 50

# เรียกใช้ tuning
tune_yolo(pretrained, data_yaml, output_dir, img_sizes, learning_rates, batch_sizes, epochs)
