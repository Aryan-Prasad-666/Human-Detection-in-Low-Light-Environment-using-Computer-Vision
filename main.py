import os
import shutil
import random

def split_dataset(
    source_dir, output_dir, train_ratio=0.8, seed=42
):
    random.seed(seed)
    
    classes = os.listdir(source_dir)
    for cls in classes:
        cls_path = os.path.join(source_dir, cls)
        if not os.path.isdir(cls_path):
            continue

        images = os.listdir(cls_path)
        random.shuffle(images)

        train_count = int(len(images) * train_ratio)

        train_images = images[:train_count]
        test_images = images[train_count:]

        train_cls_path = os.path.join(output_dir, 'train', cls)
        test_cls_path = os.path.join(output_dir, 'test', cls)
        os.makedirs(train_cls_path, exist_ok=True)
        os.makedirs(test_cls_path, exist_ok=True)

        for img in train_images:
            shutil.copy(os.path.join(cls_path, img), train_cls_path)
        for img in test_images:
            shutil.copy(os.path.join(cls_path, img), test_cls_path)

        print(f"Processed class '{cls}': {len(train_images)} train, {len(test_images)} test")

split_dataset(
    source_dir='dataset',       
    output_dir='output',       
    train_ratio=0.8          
)
