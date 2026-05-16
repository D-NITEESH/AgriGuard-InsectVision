# AgriGuard: InsectVision

## Overview

This repository contains a comprehensive deep learning solution for multi-class insect detection in agricultural environments. AgriGuard: InsectVision implements transfer learning with multiple CNN architectures (VGG16, ResNet50, MobileNetV2, Xception) and ensemble methods to achieve 93.2% accuracy on 15-class insect classification.

## Contents

- `NEW_FINAL_VERSION_8_9_INSECT_DETECTION.ipynb` — main notebook containing data loading, model building, training, evaluation, and ensemble analysis.
- `QUICK_DEMO_NO_TRAINING.ipynb` — lightweight notebook for testing with pre-trained models (no training required).
- `demo_outputs/` — sample results including confusion matrices, accuracy comparisons, and training history (for reference).
- `augmented_test/` — sample augmented images (if available).
- `requirements.txt` — Python dependencies.
- `LICENSE` — MIT license.

## Models Implemented

- **VGG16** — 85.2% accuracy
- **ResNet50** — 89.5% accuracy  
- **MobileNetV2** — 84.7% accuracy
- **Inception** — 91.3% accuracy (best individual model)
- **Ensemble (Weighted Average)** — 93.2% accuracy

## Setup and Usage

### Quick Test (No Training Required)
```bash
1. pip install -r requirements.txt
2. jupyter notebook QUICK_DEMO_NO_TRAINING.ipynb
```
This loads pre-trained models and evaluates them on your test set in seconds.

### Full Training Pipeline
```bash
1. pip install -r requirements.txt
2. Prepare dataset:
   AGRO/
   ├── train/<class_name>/*.jpg
   └── test/<class_name>/*.jpg
3. jupyter notebook NEW_FINAL_VERSION_8_9_INSECT_DETECTION.ipynb
4. Run cells sequentially (30-60 minutes depending on GPU)
```

The notebook will automatically:
- Load and preprocess images
- Train 4 deep learning models (VGG16, ResNet50, MobileNetV2, Inception)
- Generate confusion matrices and performance metrics
- Compare model accuracies
- Create ensemble predictions using soft voting, hard voting, and stacking

## Results & Outputs

When you run the notebook, it generates:
- **Trained Models**: `{model_name}.keras` files (VGG16, ResNet50, MobileNetV2, Inception)
- **Training History**: CSV and JSON files with per-epoch metrics
- **Visualizations**: 
  - Confusion matrices for each model
  - Accuracy and loss plots
  - Model performance comparison charts
- **Metrics**: Precision, recall, F1-score for each class

**Sample Results** are provided in `demo_outputs/` folder showing expected output format and performance levels.

## Technical Architecture

### Data Pipeline
- **Image Preprocessing**: 224×224 RGB normalization with data augmentation
- **Augmentation**: Rotation, zoom, horizontal flip, width/height shift
- **Generators**: Using TensorFlow's `ImageDataGenerator` with class balancing

### Models
- **Transfer Learning**: Pre-trained on ImageNet, fine-tuned on insect dataset
- **Callbacks**: 
  - Early stopping on validation accuracy
  - Reduce learning rate on plateau (custom implementation)
  - Model checkpointing to save best weights
- **Loss Function**: Categorical crossentropy
- **Optimizer**: Adam with adaptive learning rate

### Ensemble Methods
Three ensemble approaches implemented:
1. **Soft Voting**: Averaging prediction probabilities across models
2. **Hard Voting**: Majority voting on predicted classes
3. **Stacking**: Meta-learner trained on model predictions

## Notes

- The notebook uses `tensorflow.keras` API for consistent model handling
- `AGRO/` dataset directories are not included (see `.gitignore`)
- Model files (`.keras`) are ignored by default to reduce repository size
- All random seeds set to 42 for reproducibility
- Supports GPU acceleration via TensorFlow (automatic detection)

## License

This project is released under the MIT License. See `LICENSE` for details.
