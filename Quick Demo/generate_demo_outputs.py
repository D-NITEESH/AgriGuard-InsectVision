import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("🚀 AgriGuard: InsectVision - Generating Demo Output Files...\n")

# 1. Create sample training history CSV files
np.random.seed(42)
epochs = np.arange(1, 21)

# VGG Training History
vgg_history = pd.DataFrame({
    'epoch': epochs,
    'accuracy': np.linspace(0.45, 0.88, 20) + np.random.normal(0, 0.02, 20),
    'loss': np.linspace(1.8, 0.35, 20) + np.random.normal(0, 0.05, 20),
    'val_accuracy': np.linspace(0.42, 0.85, 20) + np.random.normal(0, 0.025, 20),
    'val_loss': np.linspace(1.9, 0.42, 20) + np.random.normal(0, 0.06, 20)
})
vgg_history.to_csv('demo_outputs/vgg16_history.csv', index=False)
print("✓ vgg16_history.csv created")

# ResNet50 Training History
resnet_history = pd.DataFrame({
    'epoch': epochs,
    'accuracy': np.linspace(0.50, 0.91, 20) + np.random.normal(0, 0.015, 20),
    'loss': np.linspace(1.7, 0.28, 20) + np.random.normal(0, 0.04, 20),
    'val_accuracy': np.linspace(0.48, 0.89, 20) + np.random.normal(0, 0.02, 20),
    'val_loss': np.linspace(1.8, 0.35, 20) + np.random.normal(0, 0.05, 20)
})
resnet_history.to_csv('demo_outputs/resnet50_history.csv', index=False)
print("✓ resnet50_history.csv created")

# 2. Create accuracy comparison PNG
models = ['VGG16', 'ResNet50', 'MobileNetV2', 'Xception']
accuracies = [85.2, 89.5, 84.7, 91.3]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(10, 6))
bars = plt.bar(models, accuracies, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
plt.ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
plt.xlabel('Model', fontsize=12, fontweight='bold')
plt.title('Model Performance Comparison (Demo Results)', fontsize=14, fontweight='bold')
plt.ylim([75, 95])
plt.grid(axis='y', alpha=0.3)
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, acc + 0.5, f'{acc:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('demo_outputs/model_accuracy_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ model_accuracy_comparison.png created")

# 3. Create confusion matrix PNG
classes = ['Pests_Grasshopper', 'Pests_Locust', 'Benign_Bee', 'Benign_Butterfly', 'Disease_Leaf_Spot',
           'Disease_Powdery_Mildew', 'Disease_Rust', 'Beneficial_Ladybug', 'Beneficial_Spider', 
           'Crop_Health_Good', 'Crop_Health_Average', 'Crop_Health_Poor', 'Weed_Broadleaf', 
           'Weed_Grassy', 'Other']

np.random.seed(42)
cm = np.random.randint(5, 25, size=(15, 15))
np.fill_diagonal(cm, np.random.randint(60, 95, 15))

plt.figure(figsize=(14, 10))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes, cbar_kws={'label': 'Count'})
plt.title('VGG16 - Confusion Matrix (Demo)', fontsize=16, fontweight='bold')
plt.ylabel('True Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('demo_outputs/confusion_matrix_demo.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ confusion_matrix_demo.png created")

# 4. Create training curves
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Accuracy plot
axes[0].plot(vgg_history['epoch'], vgg_history['accuracy'], label='VGG16 - Train', linewidth=2)
axes[0].plot(vgg_history['epoch'], vgg_history['val_accuracy'], label='VGG16 - Val', linewidth=2, linestyle='--')
axes[0].plot(resnet_history['epoch'], resnet_history['accuracy'], label='ResNet50 - Train', linewidth=2)
axes[0].plot(resnet_history['epoch'], resnet_history['val_accuracy'], label='ResNet50 - Val', linewidth=2, linestyle='--')
axes[0].set_xlabel('Epoch', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Accuracy', fontsize=11, fontweight='bold')
axes[0].set_title('Training Accuracy', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Loss plot
axes[1].plot(vgg_history['epoch'], vgg_history['loss'], label='VGG16 - Train', linewidth=2)
axes[1].plot(vgg_history['epoch'], vgg_history['val_loss'], label='VGG16 - Val', linewidth=2, linestyle='--')
axes[1].plot(resnet_history['epoch'], resnet_history['loss'], label='ResNet50 - Train', linewidth=2)
axes[1].plot(resnet_history['epoch'], resnet_history['val_loss'], label='ResNet50 - Val', linewidth=2, linestyle='--')
axes[1].set_xlabel('Epoch', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Loss', fontsize=11, fontweight='bold')
axes[1].set_title('Training Loss', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('demo_outputs/training_curves.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ training_curves.png created")

# 5. Create metrics CSV
metrics_data = {
    'Model': ['VGG16', 'ResNet50', 'MobileNetV2', 'Xception'],
    'Accuracy': [0.852, 0.895, 0.847, 0.913],
    'Precision': [0.854, 0.897, 0.843, 0.915],
    'Recall': [0.852, 0.894, 0.847, 0.913],
    'F1-Score': [0.853, 0.895, 0.845, 0.914]
}
metrics_df = pd.DataFrame(metrics_data)
metrics_df.to_csv('demo_outputs/model_metrics.csv', index=False)
print("✓ model_metrics.csv created")

# 6. Create ensemble results
ensemble_data = {
    'Method': ['Soft Voting', 'Hard Voting', 'Weighted Average'],
    'Accuracy': [0.928, 0.915, 0.932],
    'Precision': [0.928, 0.915, 0.932],
    'Recall': [0.927, 0.913, 0.931],
    'F1-Score': [0.927, 0.914, 0.931]
}
ensemble_df = pd.DataFrame(ensemble_data)
ensemble_df.to_csv('demo_outputs/ensemble_results.csv', index=False)
print("✓ ensemble_results.csv created")

print("\n✅ All demo files created successfully!")
